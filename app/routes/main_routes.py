from fastapi import APIRouter
from app.schemas.text import TextRequest, CorrectResponse
from app.services.text_service import correct_text_logic
from app.schemas.text import SimplifyResponse
from app.services.text_service import simplify_text_logic

#мини APi внутри api
router = APIRouter()


@router.get("/")
def root():
    return {"message": "AI Content API is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/correct", response_model=CorrectResponse)
def correct_text(request: TextRequest):
    corrected = correct_text_logic(request.text)

    return {
        "original": request.text,
        "corrected": corrected
    }

@router.post("/simplify", response_model=SimplifyResponse)
def simplify_text(request:TextRequest):
    simplified = simplify_text_logic(request.text)

    return {
        "original": request.text,
        "simplifield": simplified
    }
