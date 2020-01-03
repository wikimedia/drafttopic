from revscoring.datasources.meta import vectorizers
from revscoring.features.meta import aggregators
from revscoring.languages import english


enwiki_skipgram_200 = vectorizers.word2vec.load_kv(
    filename="enwiki.vectors.20191201.skipgram_200.300k.vec.bz2")

def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(enwiki_skipgram_200, words)


revision_text_vectors = vectorizers.word2vec(
    english.stopwords.revision.datasources.non_stopwords,
    vectorize_words,
    name="revision.text.enwiki_skipgram_200")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.enwiki_skipgram_200.mean"
)

drafttopic = [w2v]
articletopic = drafttopic
