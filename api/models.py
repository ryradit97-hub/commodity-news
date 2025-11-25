"""
Pydantic models for request and response validation
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class NewsSearchRequest(BaseModel):
    """Request model for news search endpoint"""
    commodity: str = Field(..., description="Commodity to search for (e.g., gold, oil, wheat)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "commodity": "gold"
            }
        }


class NewsArticle(BaseModel):
    """Model for a single news article"""
    title: str
    link: str
    snippet: str
    source: Optional[str] = None
    date: Optional[str] = Field(None, description="Publication date of the article")


class NewsSearchResponse(BaseModel):
    """Response model for news search endpoint"""
    query: str
    total_results: int
    articles: list[NewsArticle]


class ParaphraseRequest(BaseModel):
    """Request model for paraphrase endpoint - now supports multiple articles"""
    articles: list[dict] = Field(..., description="List of articles to synthesize and paraphrase")
    
    class Config:
        json_schema_extra = {
            "example": {
                "articles": [
                    {
                        "title": "Gold Prices Surge Amid Economic Uncertainty",
                        "content": "Gold prices reached a new high today as investors sought safe-haven assets during market turbulence."
                    },
                    {
                        "title": "Gold Hits Record High on Market Fears",
                        "content": "Precious metals rallied as global economic concerns drove investors to safe havens."
                    }
                ]
            }
        }


class ParaphraseResponse(BaseModel):
    """Response model for paraphrase endpoint with synthesized content"""
    synthesized_article: str = Field(..., description="Single synthesized article (1200-1500 characters)")
    headline: str = Field(..., description="Article headline (max 70 characters)")
    source_count: int = Field(..., description="Number of articles synthesized")
    word_counts: dict = Field(..., description="Character and word counts")
    source_articles: list[dict] = Field(default=[], description="Source articles information for references")


class ErrorResponse(BaseModel):
    """Standard error response model"""
    error: str
    detail: Optional[str] = None
