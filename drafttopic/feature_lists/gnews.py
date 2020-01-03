from revscoring.datasources.meta import vectorizers
from revscoring.features.meta import aggregators
from revscoring.languages import english


google_news_kvs = vectorizers.word2vec.load_kv(
    filename="GoogleNews-vectors-negative300.bin.gz", binary=True, limit=150000)

def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(google_news_kvs, words)


revision_text_vectors = vectorizers.word2vec(
    english.stopwords.revision.datasources.non_stopwords,
    vectorize_words,
    name="revision.text.google_news_vectors")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.google_news_vector_mean"
)

drafttopic = [w2v]
articletopic = drafttopic
