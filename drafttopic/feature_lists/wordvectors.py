from revscoring.datasources.meta import vectorizers
from revscoring.features.meta import aggregators
from revscoring.languages import english


google_news_kvs = vectorizers.word2vec.load_kv(
    filename="GoogleNews-vectors-negative300.bin", limit=150000)

revision_text_vectors = vectorizers.word2vec(
    english.stopwords.revision.datasources.non_stopwords,
    google_news_kvs,
    name="revision.text.google_news_vectors")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.google_news_vector_mean"
)

drafttopic = [w2v]
