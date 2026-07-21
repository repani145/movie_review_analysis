import numpy as np

from fastapi import APIRouter

from app.schemas import (
    ReviewRequest,
    PredictionResponse
)

from app.preprocessing import get_sentence_vector
from app.model_loader import classifier, glove


router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_sentiment(data: ReviewRequest):

    vector = get_sentence_vector(
        data.review,
        glove
    )

    vector = np.array(vector).reshape(1, -1)

    prediction = classifier.predict(vector)[0]

    probability = classifier.predict_proba(vector)

    confidence = float(np.max(probability) * 100)

    return PredictionResponse(
        prediction="Positive" if prediction == 1 else "Negative",
        confidence=round(confidence, 2)
    )