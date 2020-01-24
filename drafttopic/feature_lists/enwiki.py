from revscoring.datasources.meta import vectorizers, mappers
from revscoring.features import modifiers
from revscoring.features import wikitext
from revscoring.features.meta import aggregators


enwiki_kvs = vectorizers.word2vec.load_gensim_kv(
    filename="enwiki-20191201-learned_vectors.50_cell.100k.kv", mmap="r")


def vectorize_words(words):
    return vectorizers.word2vec.vectorize_words(enwiki_kvs, words)


revision_text_vectors = vectorizers.word2vec(
    mappers.lower_case(wikitext.revision.datasources.words),
    vectorize_words,
    name="revision.text.en_vectors")

w2v = aggregators.mean(
    revision_text_vectors,
    vector=True,
    name="revision.text.en_vectors_mean"
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
    female_pronouns_count / modifiers.max(
        female_pronouns_count + male_pronouns_count, 1)
]

drafttopic = [w2v] + pronoun_features
articletopic = drafttopic
