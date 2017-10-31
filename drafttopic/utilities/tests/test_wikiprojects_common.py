from ..wikiprojects_common import wptemplate2directory
from ..wikiprojects_common import fetch_section_text
import json


def test_wptemplate2directory():
    wp_name = 'Wikipedia:WikiProject The Apprentice UK'
    wikiprojects_file = 'culture_parsed.json'
    actual_path = ['Culture and the arts',
                   'Broadcasting', 'Television', 'Reality TV']
    wps = json.loads(fetch_section_text(wikiprojects_file))
    path = wptemplate2directory(wp_name, wps)
    assert path == actual_path
