from revscoring.datasources.meta import vectorizers, mappers
from revscoring.features import wikitext
from revscoring.features.meta import aggregators


jawiki_kvs = vectorizers.word2vec.load_gensim_kv(
    filename="jawiki-20201201-learned_vectors.50_cell.10k.kv", mmap='r')


def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(jawiki_kvs, words)


revision_text_vectors = vectorizers.word2vec(
    wikitext.revision.datasources.cjk.cjks,
    vectorize_words,
    name="revision.text.ja_vectors")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.ja_vectors_mean"
)

drafttopic = [w2v]
articletopic = drafttopic
