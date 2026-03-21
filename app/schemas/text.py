from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class CorrectResponse(BaseModel):
    original: str
    corrected: str


class SimplifyResponse(BaseModel):
    original: str
    simplifield: str


class GenerateResponse(BaseModel):
    prompt: str
    generated: str
