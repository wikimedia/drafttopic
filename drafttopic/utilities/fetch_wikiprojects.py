"""
``$ drafttopic fetch_wikiprojects -h``
::

    Generates a machine readable WikiProjects directory as:

    Example output:

        'culture': {
            'name': 'Culture',
            'url':
                'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Council/Directory/Culture',
            'root_url': <root_url>
            'index': <index>
            'topics': {
                'arts': {'name':..., 'url': culture_url+'#arts',
                    topics:{
                        'Architecture': {'name':
                            'Wikipedia:WikiProject_Architecture','url':...}
                    }
                }
            }
        }

    * root_url: Url of page from which this entry was parsed
    * index: sections index to which this entry belongs to
    * name: name of entry

    All the above mentioned fields will be absent from the base entry
    which contain actual WikiProjects name and has only three fields:
        name, shortname, active

    Usage:
        fetch_wikiprojects [--output=<path>] [--debug]

    Options:
        --output=<path>       Path to an file to write output to
                              [default: <stdout>]
        --debug               Print debug logging
"""
import datetime
import json
import logging
import re
import sys
import time
import traceback

import docopt
import mwapi

from .wikiprojects_common import wptemplate2directory

wpd_page = 'Wikipedia:WikiProject_Council/Directory'
wp_main_heading_regex =\
        r'\[\[Wikipedia:WikiProject Council/Directory/([A-Za-z_, ]+)\|([A-Za-z_, ]+)\]\]='  # noqa: E501
wp_listing_regex =\
        r'See the full listing \[\[Wikipedia:WikiProject Council/Directory/([A-Za-z_,/ ]+)'  # noqa: E501

wp_section_nextheading_regex = r'(.+)[=]{2,}'

wp_section_regex =\
    r'{{Wikipedia:WikiProject Council/Directory/WikiProject\n'\
    '[ \t]*\|project[ \t]*=[ \t]*([^\n/#]*)\n'\
    '[ \t]*\|shortname[ \t]*=[ \t]*([^\n]*)\n'\
    '[ \t]*\|active[ \t]*=[ \t]*(yes|no)\n([^}]*)}}'
# To check listing in other wikiprojects
wp_section_regex_listed =\
    r'listed-in[ \t]*=[ \t]*([^\s][^n]*)'

wp_main_links_regex1 =\
    r'\[\[Wikipedia:WikiProject Council/Directory/([A-Za-z_ ]+)/([A-Za-z_ ]+)\|([A-Za-z ]+)\]\]'  # noqa: E501
wp_main_links_regex2 =\
    r'\[\[Wikipedia:WikiProject Council/Directory/([A-Za-z_ ]+)#([A-Za-z_ ]+)\|([A-Za-z ]+)\]\]'  # noqa: E501


# Below is just a hard coding between top-level categories on
# Wikipedia:WikiProject_Council/Directory and their respective indexes on the
# page to add prefixes to mid-level categories. This should be changed in case
# the respective indexes change.  To get indexes use:
# https://en.wikipedia.org/w/api.php?action=parse&page=Wikipedia:WikiProject_Council/Directory&prop=sections  # noqa: E501
INDEX_TO_TOPLEVEL_MAP = {'2': 'Culture', '3': 'Geography',
                         '4': 'History_And_Society', '5': 'STEM',
                         '6': 'Assistance', '7': 'Admin'}


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.DEBUG if args['--debug'] else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    if args['--output'] == "<stdout>":
        output_f = sys.stdout
    else:
        output_f = args['--output']
        ts = time.time()
        curr_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        output_f = output_f + '_' + curr_time
        output_f = open(output_f, "w")

    run(output_f)


def run(output):
    logger = logging.getLogger(__name__)
    parser = WikiProjectsParser(wpd_page, logger)
    wps = {}
    wps = parser.parse_wp_directory()
    output.write(json.dumps(wps, indent=4))


class WikiProjectsParser:
    def __init__(self, wpd_page, logger=None):
        self.root_dir = wpd_page
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)
        self.session = mwapi.Session('https://en.wikipedia.org',
                                     user_agent='WikiProject directory \
                                     parser. #wikimedia-ai')

    def parse_mid_level(self, wp_directory):
        """
        Parses and generates the mapping of mid level WikiProject topics
        to actual active WikiProjects cotained in them by reading the
        full WikiProjects directory
        """
        dirname = self.root_dir
        self.logger.info("Starting WikiProjects mid-level parsing")
        mid_level_wp = {'wikiprojects': {}}
        sections = None
        try:
            sections = self.get_sections(dirname)
        except IOError as e:
            self.logger.warn(
                "Failed to get sections in root ,directory, exiting...")
            return None
        projects_started = False
        mid_level_coll = {}
        for sec in sections:
            # Ignore starting sections
            if sec['toclevel'] == 1:
                if projects_started:
                    break
                else:
                    continue
            projects_started = True
            section = self.get_section_text(dirname, sec['index'])
            if section:
                # Extract and store the name of the mid-level section
                # which can be indexed in the wikiprojects data structure
                links_type_1 = re.findall(wp_main_links_regex1, section)
                for entities in links_type_1:
                    mid_level_coll[entities[2]] = \
                        INDEX_TO_TOPLEVEL_MAP[sec['index']]
                links_type_2 = re.findall(wp_main_links_regex2, section)
                for entities in links_type_2:
                    mid_level_coll[entities[1]] = \
                        INDEX_TO_TOPLEVEL_MAP[sec['index']]

        # Now proceed to fetch leaf level wikiprojects within each mid-level
        # topic
        for project in mid_level_coll:
            path = wptemplate2directory(project, wp_directory)
            if path is None or len(path) == 0:
                self.logger.warn("Path not found for {}".format(project))
                continue
            path.append(project)
            wp_topics = self.get_topics_from_wp_directory(wp_directory, path)
            common_wp_name = mid_level_coll[project] + '.' + project
            mid_level_wp['wikiprojects'][common_wp_name] = wp_topics

        self.logger.info("Finished mid-level WikiProjects parsing")
        return mid_level_wp

    def get_topics_from_wp_directory(self, wp, path):
        """
        Give a path, returns all the contained the leaf level
        WikiProject topics
        """
        path.reverse()
        while len(path) > 0:
            entry = path.pop()
            wp = wp[entry]['topics']
        # by now wp contains the relevant WikiProject category sub structure
        names = self.get_leaf_nodes(wp)
        return names

    def get_leaf_nodes(self, wp):
        """
        Accepts a WikiProject directory substructure and returns all contained
        leaf nodes, i.e. all contained WikiProjects
        """
        names = []
        for name in wp:
            if 'topics' not in wp[name]:
                if wp[name]['active'] == 'yes':
                    names.append(wp[name]['name'])
            else:
                child_names = self.get_leaf_nodes(wp[name]['topics'])
                # To avoid nested lists
                if child_names:
                    for child in child_names:
                        names.append(child)
        return names

    def parse_wp_directory(self):
        """
        Parses the top level WikiProjects directory
        Entry point for WikiProjects parsing
        """
        dirname = self.root_dir
        self.logger.info("Starting WikiProjects directory parsing")
        wp = {}
        sections = None
        try:
            sections = self.get_sections(dirname)
        except IOError as e:
            self.logger.warn(
                "Failed to get sections in root ,directory, exiting...")
            return None
        projects_started = False
        for sec in sections:
            # Ignore starting sections
            if sec['toclevel'] == 1:
                if projects_started:
                    break
                else:
                    continue
            projects_started = True
            name = sec['line'].replace('&nbsp;', '')
            wp[name] = {'name': name,
                        'root_url': sec['fromtitle'],
                        'index': sec['index']}
            section = self.get_section_text(dirname, sec['index'])
            main_heading = None
            if section:
                main_heading = re.search(wp_main_heading_regex, section)
            if section and main_heading:
                try:
                    wp[name]['url'] = wpd_page + '/' +\
                        main_heading.group(1)
                    # Get entries in this section
                    self.logger.info(
                        "Fetching entries for section: {}".format(name))
                    sub_page_sections =\
                        self.get_sections(wp[name]['url'])
                    wp[name]['topics'], _ = self.get_sub_categories(
                        wp[name]['url'],
                        sub_page_sections,
                        0, 0)
                except IOError as e:
                    self.logger.warn("Skipping: {}".
                                     format(wp[name]['url']))
                    pass
                except:  # noqa: E722
                    self.logger.warn("Unexpected error: ",
                                     traceback.format_exc())
                    pass
        print("Ended WikiProjects parsing")
        return wp

    def get_sub_categories(self, page, sections, index, level):
        wp = {}
        prev_topic = None
        self.logger.info("Index:{}, Level:{}".format(index, level))
        idx = index
        while idx < len(sections):
            if sections[idx]['toclevel'] - 1 > level:
                sub_categories, new_idx = self.get_sub_categories(
                    page, sections, idx, level + 1)
                idx = new_idx
                if sub_categories:
                    wp[prev_topic]['topics'].update(sub_categories)
                continue
            elif sections[idx]['toclevel'] - 1 < level:
                return wp, idx
            else:
                entry = {}
                entry['name'] = sections[idx]['line']
                entry['root_url'] = sections[idx]['fromtitle']
                entry['index'] = sections[idx]['index']
                entry['topics'] = {}
                intro_projects = self.get_wikiprojects_from_section_intro(
                    page, idx + 1)
                if intro_projects:
                    entry['topics'] = intro_projects
                wp[entry['name']] = entry
            prev_topic = sections[idx]['line']
            idx += 1
        return wp, len(sections)

    def get_wikiprojects_from_section_intro(self, page, index):
        """
        Only gets wikiprojects in intro part of sections, or if this is the
        leaf section, WikiProjects in subsequent subsections not handled here
        """
        wikitext = self.get_section_text(page, index)
        return self.get_wikiprojects_from_section_intro_text(wikitext)

    def get_wikiprojects_from_section_intro_text(self, wikitext):
        wp = {}
        # remove first heading
        wikitext = wikitext.split('\n')
        wikitext = '\n'.join(wikitext[1:])
        match = re.search(wp_section_nextheading_regex, wikitext,
                          re.MULTILINE)
        if match:
            wikitext = wikitext[:match.start()]
            wp = self.get_wikiprojects_from_table(wikitext)
        else:
            wp = self.get_wikiprojects_from_table(wikitext)
        if not wp:
            # Try to match a 'See full listing here' entry
            match = re.search(wp_listing_regex, wikitext)
            if match:
                page_url = wpd_page + '/' + match.group(1)
                sections = self.get_sections(page_url)
                wp, _ = self.get_sub_categories(page_url, sections, 0, 0)
        return wp

    def get_section_text(self, page, section):
        self.logger.info("Fetching section {} from page {}".format(section,
                                                                   page))
        try:
            section = self.session.get(action='parse', page=page,
                                       prop='wikitext', section=section)
            return section['parse']['wikitext']['*']
        except IOError as e:
            self.logger.warn("Failed to request section: {} from {}".
                             format(section, page))
            self.logger.warn(traceback.format_exc())
        return None

    def get_sections(self, page):
        """
        Takes an api session and a page title and returns the sections on a
        page
        """
        self.logger.info("Fetching sections of {}".format(page))
        try:
            sections = self.session.get(action='parse', page=page,
                                        prop='sections')
            return sections['parse']['sections']
        except IOError as e:
            self.logger.warn("Failed to fetch sections for {}".format(page))
            self.logger.warn(traceback.format_exc())
            raise IOError

    def get_wikiprojects_from_table(self, wikitext):
        """
        Takes a WikiProjects table listing, and returns individual WikiProjects
        """
        wp = {}
        matches = re.findall(wp_section_regex, wikitext)
        for match in matches:
            remaining = match[3]
            listed_in = re.search(wp_section_regex_listed, remaining)
            # Listed somewhere else, so skip
            if listed_in:
                continue
            wp[match[1]] = {'name': match[0], 'shortname': match[1], 'active':
                            match[2]}
        return wp
