from revscoring.languages import english
from revscoring.datasources.meta import (frequencies, gramming, hashing,
                                         mappers)

grams = [(0,), (0, 1), (0, 2)]

hashed_bow = frequencies.table(
    hashing.hash(gramming.gram(
        mappers.lower_case(
            english.stopwords.revision.datasources.non_stopwords,
            name="lower_non_stop_words"),
        grams=grams
    ), n=2**20))

hbow = [hashed_bow]
