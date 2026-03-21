from fastapi import APIRouter
from app.schemas.text import TextRequest, CorrectRespanse

#мини APi внутри api
router = APIRouter()


@router.get("/")
def root():
    return {"message": "AI Content API is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/correct", response_model=CorrectRespanse)
def correct_text(request: TextRequest):
    text = request.text

    corrected = text.replace("i ", "I ")
    corrected = corrected.replace("has", "have")
    corrected = corrected.replace("a apple", "an apple")

    return {
        "original": text,
        "corrected": corrected
    }
