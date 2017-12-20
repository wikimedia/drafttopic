import os

from gensim.models.keyedvectors import KeyedVectors
import numpy as np

from revscoring.languages import english
from revscoring.features import FeatureVector
from revscoring.datasources import Datasource

word2vec = None
VECTORS_DIM = 300
w2v_path = os.environ.get('WORD2VEC')


def load_word2vec(filepath):
    global word2vec
    if word2vec is not None:
        return word2vec
    word2vec = KeyedVectors.load_word2vec_format(
        filepath, binary=True, limit=100000)
    return word2vec


def get_word_vectors(non_stop_tokens):
    word2vec = load_word2vec(w2v_path)
    return np.mean(
        [word2vec[w] for w in non_stop_tokens if w in word2vec] or
        [np.zeros(VECTORS_DIM)], axis=0
    )


word_vectors = Datasource(
    "word_vectors", get_word_vectors,
    depends_on=[english.stopwords.revision.datasources.non_stopwords]
)

w2v = FeatureVector(
    "word2vec", get_word_vectors,
    depends_on=[english.stopwords.revision.datasources.non_stopwords],
    returns=np.float32
)

drafttopic = [w2v]
