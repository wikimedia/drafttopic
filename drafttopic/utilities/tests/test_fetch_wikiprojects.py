from nose.tools import eq_
from ..fetch_wikiprojects import WikiProjectsParser
from ..fetch_wikiprojects import WPDPage
import logging
import json
import os
import pdb

logger = logging.getLogger( __name__ )
logging.basicConfig(level=logging.INFO)

excluded_keys = ['topics', 'root_url', 'index', 'name', 'url']

def test_WikiProjectsFromTable():
    table = fetchTestSectionText('performing_arts.test')
    parser = WikiProjectsParser(WPDPage)
    topics = parser.getWikiProjectsFromTable(table)
    topics = {'topics': topics}
    actualTopics = {'topics':
                    {
                        'Circus': {'name': 'Wikipedia:WikiProject Circus'},
                        'Magic (close-up magic)':
                            {'name': 'Wikipedia:WikiProject Magic'},
                        'Magic (stage magic)': {'name': 'Wikipedia:WikiProject Magic'},
                        'Reenactment': {'name': 'Wikipedia:WikiProject Reenactment'}
                    }
                   }
    wpTopicsCompare(actualTopics, topics)

def test_getWikiProjectsFromSectionIntroText():
    parser = WikiProjectsParser(WPDPage)
    wikitext = fetchTestSectionText('television.test')
    topics = parser.getWikiProjectsFromSectionIntroText(wikitext)
    topics = {'topics': topics}
    actualTopics = {'topics':
                    {
                        'Television': {'name': 'Wikipedia:WikiProject Television'},
                        'Australian television': {'name': 'Wikipedia:WikiProject Australian television'},
                        'Television Game Shows': {'name': 'Wikipedia:WikiProject Television Game Shows'},
                        'Television Stations': {'name': 'Wikipedia:WikiProject Television Stations'}
                    }
                   }
    wpTopicsCompare(actualTopics, topics)

def test_getSubCategories():
    parser = WikiProjectsParser(WPDPage)
    pageSections = parser.getSections(parser.session, 'Wikipedia:WikiProject_Council/Directory/Culture')
    parsed_file = 'culture_parsed.json'
    topics = {}
    if isCached(parsed_file):
        topics = json.loads(fetchTestSectionText(parsed_file))
    else:
        topics, _ = parser.getSubCategories(parser.session,
                                      'Wikipedia:WikiProject_Council/Directory/Culture',
                                        pageSections, 0, 0)
        cacheText(parsed_file, topics)
    actualSections = json.loads(fetchTestSectionText('culture_toc.json'))['sections']
    wpTopicsCompareWithToc(actualSections, topics, 0, 0)

def isCached(filename):
    return os.path.exists('testfiles/{}'.format(filename))

def cacheText(filename, result):
    try:
        f = open('testfiles/{}'.format(filename), 'w')
        f.write(json.dumps(result))
        f.close()
    except IOError as e:
        logger.warn("Failed to write to cache file: {}".format(filename))

def fetchTestSectionText(filename):
    try:
        f = open('testfiles/{}'.format(filename), 'r')
        wikitext = f.read()
        f.close()
    except IOError as e:
        logger.warn("Failed to read test file: {}".format(filename))
    return wikitext

def wpTopicsCompareWithToc(tocTopics, parsedWpTree, index, level):
    """
    Helper method that takes a tocTopic as got from api?action=parse&prop=sections and
    a parsed WikiProjects tree and compares the nested structure of topics
    """
    prevTopic = None
    logger.info("Index:{}, Level:{}".format(index, level))
    idx = index
    while idx < len(tocTopics):
        if tocTopics[idx]['toclevel'] - 1 > level:
            idx = wpTopicsCompareWithToc(tocTopics,
                                   parsedWpTree[prevTopic]['topics'],
                                   idx, level+1)
            continue
        elif tocTopics[idx]['toclevel'] - 1 < level:
            return idx
        else:
            eq_(tocTopics[idx]['line'] in parsedWpTree.keys(), True)
        prevTopic = tocTopics[idx]['line']
        idx += 1
    return len(tocTopics)


def wpTopicsCompare(actualWpTree, parsedWpTree):
    """
    Helper method compares the topic hierarchy of WikiProjects
    """
    for key in actualWpTree.keys():
        if key not in excluded_keys:
            logger.info('Comparing:{}'.format(key))
            eq_(actualWpTree[key]['name'], parsedWpTree[key]['name'], True)
    if 'topics' in actualWpTree:
        wpTopicsCompare(actualWpTree['topics'], parsedWpTree['topics'])    

