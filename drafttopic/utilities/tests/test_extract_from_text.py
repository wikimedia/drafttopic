from revscoring.features import wikitext
from ..extract_from_text import LabelingDependentExtractor

labelings = [{'title': 'abc', 'text': 'hi, this is some sample text'},
             {'title': 'xyz', 'text': 'hi, this is another sample text'}]


def test_extractor():
    dependents = [wikitext.revision.chars]
    extractor = LabelingDependentExtractor(dependents)
    key = str(dependents[0])
    observation = extractor.extract_and_cache(labelings[0])
    assert observation['cache'][key] == 28
    observation = extractor.extract_and_cache(labelings[1])
    assert observation['cache'][key] == 31
