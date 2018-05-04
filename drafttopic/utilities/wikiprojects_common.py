import os
import json
import logging
logger = logging.getLogger(__name__)


WIKIPROJECT_FETCH_THREADS = 1000


def wptemplate2directory(template_name, wikiprojects, directory=[]):
    """
    Convert a WikiProject template name to a path within the
    WikiProject Directory hierarchy.

    :Parameters:
    template_name : str
      The name of a template (or redirected template) used to tag an article
    wikiprojects : dict
      The wikiprojects directory tree

    :Returns:
    A directory path as a list of strings ordered from top to bottom.
    E.g. "maths rating" returns ["stem", "mathematics"]
    """
    for key in wikiprojects:
        val = wikiprojects[key]
        if 'name' in val and val['name'] == template_name:
            if 'root_url' in val and val['root_url'].endswith('Directory'):
                path_new = directory[:]
                path_new.append(key)
                path = wptemplate2directory(
                    template_name, val['topics'], path_new)
                if path is not None:
                    return path
            return directory
        if 'topics' in val:
            path_new = directory[:]
            path_new.append(key)
            path = wptemplate2directory(template_name, val['topics'], path_new)
            if path is not None:
                return path
    return None


def invert_mid_level_projects(wp):
    # Generates inverse mappings
    wprojects = wp['wikiprojects']
    wp['inverse_wp'] = {}
    for cat in wprojects:
        wps = wprojects[cat]
        for wikiproject in wps:
            wp['inverse_wp'][wikiproject] = cat
    return wp


def is_cached(filename):
    return os.path.exists('testfiles/{}'.format(filename))


def cache_text(filename, result, logger):
    try:
        f = open('testfiles/{}'.format(filename), 'w')
        f.write(json.dumps(result))
        f.close()
    except IOError as e:
        logger.warn("Failed to write to cache file: {}".format(filename))


def fetch_section_text(filename):
    try:
        f = open('testfiles/{}'.format(filename), 'r')
        wikitext = f.read()
        f.close()
    except IOError as e:
        logger.warn("Failed to read test file: {}".format(filename))
        return None
    return wikitext
