from revscoring.datasources.revision_oriented import revision
from revscoring.dependencies import solve

from .. import enwiki

revision_text = revision.text


def test_hashed_bow():
    text = "This is a sample article. Frequency of hashes will be generated for\
    this sample"
    hashes = list(solve(enwiki.hbow, cache={revision_text: text}))
    assert hashes == [{114466: 2, 384781: 1, 403532: 1, 578464: 1, 419682: 1,
                       219226: 1, 733488: 1, 757102: 1, 1046957: 1, 602220: 1,
                       278429: 1, 162438: 1, 942677: 1, 102772: 1}]
