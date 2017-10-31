from ..fetch_wikiprojects import WikiProjectsParser
from ..fetch_wikiprojects import wpd_page
from ..wikiprojects_common import is_cached, fetch_section_text, cache_text
import logging
import json

logger = logging.getLogger(__name__)

excluded_keys = ['topics', 'root_url', 'index', 'name', 'url']


def test_wiki_projects_from_table():
    table = fetch_section_text('performing_arts.test')
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
    wikitext = fetch_section_text('television.test')
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


def test_get_leaf_nodes():
    parser = WikiProjectsParser(wpd_page)
    page_sections = parser.get_sections(
        'Wikipedia:WikiProject_Council/Directory/Culture')
    parsed_file = 'culture_parsed.json'
    topics = {}
    if is_cached(parsed_file):
        topics = json.loads(fetch_section_text(parsed_file))
    else:
        topics, _ = parser.get_sub_categories(
            'Wikipedia:WikiProject_Council/Directory/Culture',
            page_sections, 0, 0)
        cache_text(parsed_file, topics, logger)
    music_topics = topics['Culture and the arts'][
        'topics']['Performing arts']['topics']['Music']['topics']
    actual_music_topics = [
        "Wikipedia:WikiProject Music",
        "Wikipedia:WikiProject Music theory",
        "Wikipedia:WikiProject Composers",
        "Wikipedia:WikiProject Richard Wagner",
        "Wikipedia:WikiProject Songs",
        "Wikipedia:WikiProject Alternative music",
        "Wikipedia:WikiProject Black Metal",
        "Wikipedia:WikiProject Christian music",
        "Wikipedia:WikiProject Electronic music",
        "Wikipedia:WikiProject Hip hop",
        "Wikipedia:WikiProject Industrial",
        "Wikipedia:WikiProject Metal",
        "Wikipedia:WikiProject Post-hardcore",
        "Wikipedia:WikiProject Progressive Rock",
        "Wikipedia:WikiProject Punk music",
        "Wikipedia:WikiProject Reggae",
        "Wikipedia:WikiProject Rock music",
        "Wikipedia:WikiProject Drum Corps",
        "Wikipedia:WikiProject Marching band",
        "Wikipedia:WikiProject Roots music",
        "Wikipedia:WikiProject Australian music",
        "Wikipedia:WikiProject Canadian music",
        "Wikipedia:WikiProject Indian music",
        "Wikipedia:WikiProject Musicians",
        "Wikipedia:WikiProject Guitarists",
        "Wikipedia:WikiProject Coldplay",
        "Wikipedia:WikiProject Katy Perry",
        "Wikipedia:WikiProject Madonna",
        "Wikipedia:WikiProject Pink Floyd",
        "Wikipedia:WikiProject Albums",
        "Wikipedia:WikiProject Discographies",
        "Wikipedia:WikiProject Record Production"
    ]
    wikiproject_topics = parser.get_leaf_nodes(music_topics)
    assert len(wikiproject_topics) == len(actual_music_topics) and\
        sorted(wikiproject_topics) == sorted(actual_music_topics)


def test_get_sub_categories():
    parser = WikiProjectsParser(wpd_page)
    page_sections = parser.get_sections(
        'Wikipedia:WikiProject_Council/Directory/Culture')
    parsed_file = 'culture_parsed.json'
    topics = {}
    if is_cached(parsed_file):
        topics = json.loads(fetch_section_text(parsed_file))
    else:
        topics, _ = parser.get_sub_categories(
            'Wikipedia:WikiProject_Council/Directory/Culture',
            page_sections, 0, 0)
        cache_text(parsed_file, topics, logger)
    actual_sections = json.loads(
        fetch_section_text('culture_toc.json'))['sections']
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
                idx, level + 1)
            continue
        elif toc_topics[idx]['toclevel'] - 1 < level:
            return idx
        else:
            assert toc_topics[idx]['line'] in parsed_wp_tree.keys()
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
            assert actual_wp_tree[key]['name'], parsed_wp_tree[key]['name']
    if 'topics' in actual_wp_tree:
        wp_topics_compare(actual_wp_tree['topics'], parsed_wp_tree['topics'])
