from revscoring.datasources.meta import vectorizers
from revscoring.features import wikibase
from revscoring.features.meta import aggregators


wikidata_kvs = vectorizers.word2vec.load_gensim_kv(
    filename="wikidata-20200501-learned_vectors.50_cell.10k.kv", mmap="r")


def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(wikidata_kvs, words)


revision_text_vectors = vectorizers.word2vec(
    wikibase.revision.datasources.claims,
    vectorize_words,
    name="revision.text.wikidata_vectors")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.wikidata_vectors_mean"
)

articletopic = [w2v]
