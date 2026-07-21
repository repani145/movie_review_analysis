from pathlib import Path

import joblib
import gensim.downloader as api


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "sentiment_model.pkl"


print("Loading Logistic Regression model...")
classifier = joblib.load(MODEL_PATH)
print("Model loaded successfully.")


print("Loading GloVe model...")
glove = api.load("glove-wiki-gigaword-100")
print("GloVe loaded successfully.")