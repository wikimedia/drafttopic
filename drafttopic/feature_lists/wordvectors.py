from revscoring.datasources.meta import vectorizers
from revscoring.features import wikitext
from revscoring.features.meta import aggregators
from revscoring.languages import english


google_news_kvs = vectorizers.word2vec.load_kv(
    filename="GoogleNews-vectors-negative300.bin.gz",
    binary=True, limit=150000)


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

female_pronouns = wikitext.revision.datasources.tokens_matching(
    r"\b(she|her|hers)\b")
male_pronouns = wikitext.revision.datasources.tokens_matching(
    r"\b(he|him|his)\b")
female_pronouns_count = aggregators.len(female_pronouns)
male_pronouns_count = aggregators.len(male_pronouns)

pronoun_features = [
    female_pronouns_count,
    male_pronouns_count,
    female_pronouns_count + male_pronouns_count,
    female_pronouns_count / (female_pronouns_count + male_pronouns_count)
]

drafttopic = [w2v] + pronoun_features
articletopic = drafttopic
