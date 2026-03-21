from fastapi import APIRouter

#мини APi внутри api
router = APIRouter()


@router.get("/")
def root():
    return {"message": "AI Content API is running"}


@router.get("/health")
def health():
    return {"status": "ok"}