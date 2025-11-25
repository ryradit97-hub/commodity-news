"""
Ultra-simple Vercel function for testing
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json

# Data models
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

# Initialize FastAPI app
app = FastAPI(title="AME Commodity News API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def root():
    """API health check"""
    return {"message": "AME Commodity News API", "status": "active", "version": "2.0"}

@app.post("/api/news/paraphrase")
def paraphrase_articles(request: ParaphraseRequest):
    """Simple synthesis without external APIs for testing"""
    try:
        if not request.articles:
            return {"error": "No articles provided"}
        
        # Simple template response for testing
        synthesized_content = """The global commodity markets continue to experience significant developments across multiple sectors. Supply chain dynamics remain a key focus for industry analysts as producers adapt to changing market conditions and implement strategic operational adjustments.

Market participants are closely monitoring production levels and infrastructure developments that could impact future supply availability. Price volatility reflects ongoing uncertainty about demand patterns and geopolitical factors affecting international trade flows and market sentiment.

Industry stakeholders are implementing strategic adjustments to navigate the evolving landscape, with particular attention to operational efficiency and cost management measures. These developments will likely continue to influence market sentiment and investment decisions in the coming quarters."""
        
        title = "Commodity Markets Navigate Evolving Supply Chain Dynamics"
        summary = "Global commodity markets face ongoing supply chain challenges and price volatility. Industry participants implement strategic adjustments to manage operational efficiency."
        
        return ParaphraseResponse(
            synthesized_article=synthesized_content,
            title=title,
            summary=summary,
            source_articles=request.articles
        )
        
    except Exception as e:
        return {"error": f"Processing error: {str(e)}"}

# For Vercel deployment
from mangum import Mangum
handler = Mangum(app, lifespan="off")