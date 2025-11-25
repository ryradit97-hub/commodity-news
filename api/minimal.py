from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class NewsArticle(BaseModel):
    title: str
    content: str
    url: str
    published_date: Optional[str] = None
    source: Optional[str] = None

class ParaphraseRequest(BaseModel):
    articles: List[NewsArticle]

class ParaphraseResponse(BaseModel):
    synthesized_article: str
    title: str
    summary: str
    source_articles: List[NewsArticle]

@app.get("/api")
def root():
    return {"message": "API Working", "status": "ok"}

@app.post("/api/news/paraphrase")
def paraphrase(request: ParaphraseRequest):
    return ParaphraseResponse(
        synthesized_article="Test synthesis result with multiple paragraphs.\n\nSecond paragraph here.\n\nThird paragraph here.",
        title="Test Article",
        summary="Test summary",
        source_articles=request.articles
    )

# Vercel handler
from mangum import Mangum
handler = Mangum(app)