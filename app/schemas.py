from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str   # positive / negative / neutral
    score: int       # basit bir puan
