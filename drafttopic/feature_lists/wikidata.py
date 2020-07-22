import re

from revscoring.datasources import Datasource
from revscoring.datasources.meta import vectorizers
from revscoring.features import wikibase
from revscoring.features.meta import aggregators


QID_RE = re.compile('Q[0-9]+')

wikidata_kvs = vectorizers.word2vec.load_gensim_kv(
    filename="wikidata-20200501-learned_vectors.50_cell.10k.kv", mmap="r")

def process_claims_to_words(claims):
    words = []
    for pid, value in claims:
        words.append(pid)
        if QID_RE.match(value) is not None:
            words.append(value)
    return words

def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(wikidata_kvs, words)


claim_words = Datasource(
    "wikidata.revision.claim_words",
    process_claims_to_words,
    depends_on=[wikibase.revision.datasources.claims])

revision_claim_words_vectors = vectorizers.word2vec(
    claim_words,
    vectorize_words,
    name="revision.text.wikidata_vectors")

w2v = aggregators.mean(
    revision_claim_words_vectors,
    vector=True,
    name="revision.text.wikidata_vectors_mean"
)

articletopic = [w2v]
