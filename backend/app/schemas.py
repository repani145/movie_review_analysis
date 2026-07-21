from pydantic import BaseModel


class ReviewRequest(BaseModel):
    review: str


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float