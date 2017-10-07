from nose.tools import eq_
from ..fetch_wikiprojects import WikiProjectsParser
from ..fetch_wikiprojects import wpd_page
from ..wikiprojects_common import is_cached, fetch_section_text, cache_text
import logging
import json
import os

logger = logging.getLogger(__name__)

excluded_keys = ['topics', 'root_url', 'index', 'name', 'url']


def test_wiki_projects_from_table():
    table = fetch_section_text('performing_arts.test', logger)
    parser = WikiProjectsParser(wpd_page)
    topics = parser.get_wikiprojects_from_table(table)
    topics = {'topics': topics}
    actual_topics = {
        'topics':
        {
            'Circus': {'name': 'Wikipedia:WikiProject Circus'},
            'Magic (close-up magic)':
            {'name': 'Wikipedia:WikiProject Magic'},
            'Magic (stage magic)':
            {'name': 'Wikipedia:WikiProject Magic'},
            'Reenactment':
            {'name': 'Wikipedia:WikiProject Reenactment'}
        }
    }
    wp_topics_compare(actual_topics, topics)


def test_get_wikiprojects_from_section_intro_text():
    parser = WikiProjectsParser(wpd_page)
    wikitext = fetch_section_text('television.test', logger)
    topics = parser.get_wikiprojects_from_section_intro_text(wikitext)
    topics = {'topics': topics}
    actual_topics = {
        'topics':
        {
            'Television': {'name': 'Wikipedia:WikiProject Television'},
            'Australian television':
            {'name': 'Wikipedia:WikiProject Australian television'},
            'Television Game Shows':
            {'name': 'Wikipedia:WikiProject Television Game Shows'},
            'Television Stations':
            {'name': 'Wikipedia:WikiProject Television Stations'}
        }
    }
    wp_topics_compare(actual_topics, topics)


def test_get_sub_categories():
    parser = WikiProjectsParser(wpd_page)
    page_sections = parser.get_sections(
        'Wikipedia:WikiProject_Council/Directory/Culture')
    parsed_file = 'culture_parsed.json'
    topics = {}
    if is_cached(parsed_file):
        topics = json.loads(fetch_section_text(parsed_file, logger))
    else:
        topics, _ = parser.get_sub_categories(
            'Wikipedia:WikiProject_Council/Directory/Culture',
            page_sections, 0, 0)
        cache_text(parsed_file, topics, logger)
    actual_sections = json.loads(
        fetch_section_text('culture_toc.json', logger))['sections']
    wp_topics_compare_with_toc(actual_sections, topics, 0, 0)


def wp_topics_compare_with_toc(toc_topics, parsed_wp_tree, index, level):
    """
    Helper method that takes a tocTopic as got from
    api?action=parse&prop=sections and a parsed WikiProjects tree and
    compares the nested structure of topics
    """
    prev_topic = None
    logger.info("Index:{}, Level:{}".format(index, level))
    idx = index
    while idx < len(toc_topics):
        if toc_topics[idx]['toclevel'] - 1 > level:
            idx = wp_topics_compare_with_toc(
                toc_topics,
                parsed_wp_tree[prev_topic]['topics'],
                idx, level+1)
            continue
        elif toc_topics[idx]['toclevel'] - 1 < level:
            return idx
        else:
            eq_(toc_topics[idx]['line'] in parsed_wp_tree.keys(), True)
        prev_topic = toc_topics[idx]['line']
        idx += 1
    return len(toc_topics)


def wp_topics_compare(actual_wp_tree, parsed_wp_tree):
    """
    Helper method compares the topic hierarchy of WikiProjects
    """
    for key in actual_wp_tree.keys():
        if key not in excluded_keys:
            logger.info('Comparing:{}'.format(key))
            eq_(actual_wp_tree[key]['name'], parsed_wp_tree[key]['name'], True)
    if 'topics' in actual_wp_tree:
        wp_topics_compare(actual_wp_tree['topics'], parsed_wp_tree['topics'])
