"""
Generates a machine readable WikiProjects directory as:
{
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
}
Here:
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
import mwapi
import json
import re
import logging
import docopt
import pdb
import sys

def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.DEBUG if args['--debug'] else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )
    
    if args['--output'] == "<stdout>":
        output_f = sys.stdout
    else:
        output_f = open(args['--output'], "w")
    
    run(output_f)

WPDPage = 'Wikipedia:WikiProject_Council/Directory'
WPMainHeadingRegex =\
        r'\[\[Wikipedia:WikiProject Council/Directory/([A-Za-z_, ]+)\|([A-Za-z_, ]+)\]\]='
WPListingRegex =\
        r'See the full listing \[\[Wikipedia:WikiProject Council/Directory/([A-Za-z_,/ ]+)'
WPMainLinksRegex1 =\
        r'\[\[Wikipedia:WikiProject_Council/Directory/([A-Za-z_]+)/([A-Za-z_])\|([A-Za-z]+)\]\]'
WPMainLinksRegex2 =\
        r'\[\[Wikipedia:WikiProject_Council/Directory/([A-Za-z_]+)\|([A-Za-z]+)\]\]'

WPSectionNextHeadingRegex = r'(.+)[=]{2,}'

WPSectionRegex =\
        r'{{Wikipedia:WikiProject Council/Directory/WikiProject\n'\
        '\|project = ([a-zA-Z_: -]+)\n'\
        '\|shortname = ([a-zA-Z\(\) -]+)\n'\
        '\|active = (yes|no)\n([^}]*)}}'
# To check listing in other wikiprojects
WPSectionRegexListed =\
        r'listed-in = ([A-Za-z#/:_ ]+)'

def run(output):
    logger = logging.getLogger(__name__)
    parser = WikiProjectsParser(WPDPage, logger)
    wps = parser.parseWpDirectory()
    output.write(json.dumps(wps, indent=4))

class WikiProjectsParser:
    def __init__(self, WPDPage, logger=None):
        self.rootDir = WPDPage
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)
        self.session = mwapi.Session('https://en.wikipedia.org', user_agent='WP-dev')

    def parseWpDirectory(self):
        """
        Parses the top level WikiProjects directory
        Entry point for WikiProjects parsing
        """
        dirname = self.rootDir
        self.logger.info("Starting WikiProjects parsing")
        wp = {}
        topSections = self.getSections(self.session, dirname)
        projectsStarted = False
        for sec in topSections:
            # Ignore starting sections
            if sec['toclevel'] == 1:
                if projectsStarted:
                    break
                else:
                    continue
            projectsStarted = True
            name = sec['line'].replace('&nbsp;', '')
            wp[sec['line']] = {'name': name,
                                'root_url': sec['fromtitle'],
                                'index': sec['index']}
            # Get entries in this section
            self.logger.info("Fetching entries for section:{}".format(name))
            section = self.getSectionText(self.session, dirname, sec['index'])
            mainHeading = re.search(WPMainHeadingRegex, section)
            if mainHeading:
                wp[sec['line']]['url'] = WPDPage + '/' + mainHeading.group(1)
                pageSections = self.getSections(self.session, wp[sec['line']]['url'])
                wp[sec['line']]['topics'], _ = self.getSubCategories(self.session,
                                                                  wp[sec['line']]['url'],
                                                                  pageSections,
                                                                  0, 0)


        self.logger.info("Ended WikiProjects parsing")
        return wp

    def getSubCategories(self, session, page, sections, index, level):
        wp = {}
        prevTopic = None
        self.logger.info("Index:{}, Level:{}".format(index, level))
        idx = index
        while idx < len(sections):
            if sections[idx]['toclevel'] - 1 > level:
                subCategories, newIdx = self.getSubCategories(
                        session, page, sections, idx, level+1)
                idx = newIdx
                if subCategories:
                    wp[prevTopic]['topics'] = {**wp[prevTopic]['topics'],
                                            **subCategories}
                continue
            elif sections[idx]['toclevel'] - 1 < level:
                return wp, idx
            else:
                entry = {}
                entry['name'] = sections[idx]['line']
                entry['root_url'] = sections[idx]['fromtitle']
                entry['index'] = sections[idx]['index']
                entry['topics'] = {}
                introProjects = self.getWikiProjectsFromSectionIntro(
                                                session, page, idx + 1)
                if introProjects:
                    entry['topics'] = introProjects
                wp[entry['name']] = entry
            prevTopic = sections[idx]['line']
            idx += 1
        return wp, len(sections)
    
    def getWikiProjectsFromSectionIntro(self, session, page, index):
        """
        Only gets wikiprojects in intro part of sections, or if this is the leaf
        section, WikiProjects in subsequent subsections not handled here
        """
        wikitext = self.getSectionText(session, page, index)
        return self.getWikiProjectsFromSectionIntroText(wikitext)

    def getWikiProjectsFromSectionIntroText(self, wikitext):
        wp = {}
        # remove first heading
        wikitext = wikitext.split('\n')
        wikitext = '\n'.join(wikitext[1:])
        match = re.search(WPSectionNextHeadingRegex, wikitext, re.MULTILINE)
        if match:
            wikitext = wikitext[:match.start()]
            wp = self.getWikiProjectsFromTable(wikitext)
        else:
            wp = self.getWikiProjectsFromTable(wikitext)
        if not wp:
            # Try to match a 'See full listing here' entry
            match = re.search(WPListingRegex, wikitext)
            if match:
                pageUrl = WPDPage + '/' + match.group(1)
                sections = self.getSections(self.session, pageUrl)
                wp, _ = self.getSubCategories(self.session, pageUrl, sections, 0, 0)
        return wp

    def getSectionText(self, session, page, section):
        self.logger.info("Fetching section {} from page {}".format(section, page))
        section = session.get(action='parse', page=page, prop='wikitext',
                               section=section)
        return section['parse']['wikitext']['*']

    def getSections(self, session, page):
        """
        Takes an api session and a page title and returns the sections on a page
        """
        self.logger.info("Fetching sections of {}".format(page))
        sections = session.get(action='parse', page=page, prop='sections')
        return sections['parse']['sections']

    def getWikiProjectsFromTable(self,wikitext):
        """
        Takes a WikiProjects table listing, and returns individual WikiProjects
        """
        wp = {}
        matches = re.findall(WPSectionRegex, wikitext)
        for match in matches:
            remaining = match[3]
            listedIn = re.search(WPSectionRegexListed, remaining)
            # Listed somewhere else, so skip
            if listedIn:
                continue
            wp[match[1]] = {'name': match[0], 'shortname': match[1], 'active':
                            match[2]}
        return wp

