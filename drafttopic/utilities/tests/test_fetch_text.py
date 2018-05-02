from ..fetch_text import build_fetch_text_extractor
from unittest.mock import patch

long_text = 'a' * 100

mwapi_responses = [{'query': {'pages': [
    {'title': 'A', 'ns': 0, 'revisions': [{'content': 'sometext'}]},
    {},
    {'title': 'B', 'ns': 0, 'revisions': [{'content': long_text}]}
]}}]


def mwapi_generator(num_responses=1):
    i = 0
    while i < num_responses:
        yield mwapi_responses[i]
        i = i + 1


@patch('mwapi.Session')
def test_get_rev_from_title(mock_session):
    mock_session.get.return_value = mwapi_generator()
    obs = [{'talk_page_title': 'A'},
           {'talk_page_title': 'B'},
           {'talk_page_title': 'C'}]
    _fetch_text = build_fetch_text_extractor(mock_session)
    observations = _fetch_text(obs)
    actual_observations = [
        {'talk_page_title': 'A', 'text': ''},
        {'talk_page_title': 'B', 'text': long_text},
        {'talk_page_title': 'C', 'text': ''}
    ]
    assert actual_observations == observations
