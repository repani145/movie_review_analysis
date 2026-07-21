import re
import string
import joblib
import nltk
import gensim.downloader as api

import numpy as np
import pandas as pd

from pathlib import Path

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ---------------------------------------------------
# Download nltk resources (only first time)
# ---------------------------------------------------

nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "sentiment_data.csv"

data = pd.read_csv(csv_path)

print(data.head())

# ---------------------------------------------------
# Text Cleaning
# ---------------------------------------------------

def preprocess(text):

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

print("\nCleaning text...\n")

data["clean_review"] = data["content"].apply(preprocess)

# ---------------------------------------------------
# Load GloVe
# ---------------------------------------------------

print("Loading GloVe model...")

glove = api.load("glove-wiki-gigaword-100")

print("Done.")

# ---------------------------------------------------
# Sentence Embedding
# ---------------------------------------------------

def sentence_vector(sentence):

    vectors = [
        glove[word]
        for word in sentence.split()
        if word in glove
    ]

    if len(vectors) == 0:
        return np.zeros(glove.vector_size)

    return np.mean(vectors, axis=0)

print("Generating sentence embeddings...")

data["vector"] = data["clean_review"].apply(sentence_vector)

# ---------------------------------------------------
# Train Test Split
# ---------------------------------------------------

X = np.vstack(data["vector"].values)

y = data["is_positive"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ---------------------------------------------------
# Train Model
# ---------------------------------------------------

print("\nTraining Logistic Regression...\n")

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ---------------------------------------------------
# Evaluation
# ---------------------------------------------------

prediction = model.predict(X_test)

print("=" * 60)

print("Accuracy :", accuracy_score(y_test, prediction))

print("Precision :", precision_score(y_test, prediction))

print("Recall :", recall_score(y_test, prediction))

print("F1 Score :", f1_score(y_test, prediction))

print("=" * 60)

print(confusion_matrix(y_test, prediction))

print("=" * 60)

print(classification_report(y_test, prediction))

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

MODEL_DIR = BASE_DIR.parent / "models"

MODEL_DIR.mkdir(exist_ok=True)

joblib.dump(model, MODEL_DIR / "sentiment_model.pkl")

print("\nModel Saved Successfully.")

print(MODEL_DIR)