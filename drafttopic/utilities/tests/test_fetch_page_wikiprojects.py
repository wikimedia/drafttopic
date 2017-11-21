from ..fetch_page_wikiprojects import extract_mid_level_categories
from ..fetch_page_wikiprojects import extract_wikiproject_templates
from ..fetch_page_wikiprojects import build_fetch_wikiprojects_info
from unittest.mock import patch


def test_extract_mid_level_categories():
    inverse_wp_map = {'Wikipedia:WikiProject Songs': 'Performing arts',
                      'Wikipedia:WikiProject Science': 'Science'}
    templates = ['Template:WikiProject Songs', 'Template:WikiProject Songs',
                 'Template:WikiProject Science', 'Template:xyz']
    mid_level_set = extract_mid_level_categories(templates, inverse_wp_map)
    actual_mid_level_set = ['Performing arts', 'Science']
    assert sorted(actual_mid_level_set) == sorted(mid_level_set)


def test_extract_wikiproject_templates():
    templates = [{'title': 'Template:WikiProject Songs'},
                 {'title': 'Template:xyz'},
                 {'title': 'Template:WikiProject Albums'},
                 {'title': 'Template:123'}]
    wp_templates_actual = ['Template:WikiProject Songs',
                           'Template:WikiProject Albums']
    wp_templates = extract_wikiproject_templates(templates)
    assert sorted(wp_templates_actual) == sorted(wp_templates)


mwapi_responses = [{'query': {'pages': [
    {'pageid': 123, 'templates': [], 'lastrevid': 121, 'title': 'Page A'},
    {'pageid': 456, 'templates': [
        {'title': 'Template:WikiProject abc'}, {'title': 'xyz'}],
        'lastrevid': 111, 'title': 'Page B'}
]}}, {'query': {'pages': [
    {'pageid': 123, 'templates': [
        {'title': 'Template:WikiProject xyz'}, {'title': 'abc'}]},
    {'pageid': 456, 'templates': []}
]}}]


def mwapi_generator(num_responses=2):
    i = 0
    while i < num_responses:
        yield mwapi_responses[i]
        i = i + 1


@patch('mwapi.Session')
def test_fetch_page_wikiprojects(mock_session):
    mock_session.get.return_value = mwapi_generator()
    mid_level_wp = {'inverse_wp': {}}
    _fetch_wikiprojects_info = build_fetch_wikiprojects_info(mock_session,
                                                             mid_level_wp)
    obs = [{'talk_page_id': 123}, {'talk_page_id': 456}, {'talk_page_id': 789}]
    observations = _fetch_wikiprojects_info(obs)
    actual_observations = [
        {'talk_page_id': 123, 'rev_id': 121, 'templates':
         ['Template:WikiProject xyz'], 'mid_level_categories': [],
            'talk_page_title': 'Page A'},
        {'talk_page_id': 456, 'rev_id': 111, 'templates':
         ['Template:WikiProject abc'], 'mid_level_categories': [],
         'talk_page_title': 'Page B'}
    ]
    assert observations == actual_observations
