from pathlib import Path
import joblib
from app.glove_loader import load_glove

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "sentiment_model.pkl"


print("Loading Logistic Regression model...")
classifier = joblib.load(MODEL_PATH)
print("Model loaded successfully.")

glove = load_glove()