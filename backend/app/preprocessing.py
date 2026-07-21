import re
import nltk

import numpy as np

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download once (safe to call repeatedly)
# nltk.download("stopwords", quiet=True)
# nltk.download("wordnet", quiet=True)
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")



stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text: str) -> str:
    """
    Clean raw review text.
    """

    text = text.lower()

    text = re.sub(r"<.*?>", "", text)

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z ]", "", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def get_sentence_vector(sentence: str, glove_model):

    cleaned = clean_text(sentence)

    vectors = [
        glove_model[word]
        for word in cleaned.split()
        if word in glove_model
    ]

    if len(vectors) == 0:
        return np.zeros(glove_model.vector_size)

    return np.mean(vectors, axis=0)