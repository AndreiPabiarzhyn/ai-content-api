from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class CorrectResponse(BaseModel):
    original: str
    corrected: str
