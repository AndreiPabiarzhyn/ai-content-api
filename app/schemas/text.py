from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class CorrectRespanse(BaseModel):
    original: str
    corrected: str
