"""Emotion Engine API routes.

POST /api/v1/emotion/classify  — Interpret freeform text into structured emotion data.
"""

from fastapi import APIRouter, HTTPException

from models.emotion import EmotionClassifyInput, EmotionOutput
from services.emotion_service import classify_emotion

router = APIRouter(prefix="/emotion", tags=["emotion"])


@router.post("/classify", response_model=EmotionOutput)
def classify(input_data: EmotionClassifyInput):
    """Classify freeform memory/mood text into a structured EmotionOutput.

    Security: the Anthropic API key never leaves the server.
    """
    try:
        return classify_emotion(input_data)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Emotion classification failed: {str(exc)}",
        ) from exc
