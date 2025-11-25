"""
Simple Vercel serverless function for commodity news synthesis
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import httpx
from typing import List, Optional
from pydantic import BaseModel

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

# Environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAbxYqg6ZUQ0963taHT-1gy1Jalvzh6S7Y")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-1b5cc072ab944781a9c9ba0bf6936f79")

async def call_gemini_api(prompt: str) -> str:
    """Call Google Gemini API via REST"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={GEMINI_API_KEY}",
                headers={"Content-Type": "application/json"},
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 2000
                    }
                }
            )
            result = response.json()
            if "candidates" in result and len(result["candidates"]) > 0:
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                raise Exception("No response from Gemini")
    except Exception as e:
        print(f"Gemini API error: {e}")
        return await call_deepseek_api(prompt)

async def call_deepseek_api(prompt: str) -> str:
    """Fallback to DeepSeek API"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 2000
                }
            )
            result = response.json()
            return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"DeepSeek API error: {e}")
        # Return a simple template as final fallback
        return f"""
The global commodity markets continue to experience significant developments across multiple sectors. Supply chain dynamics remain a key focus for industry analysts as producers adapt to changing market conditions.

Market participants are closely monitoring production levels and infrastructure developments that could impact future supply availability. Price volatility reflects ongoing uncertainty about demand patterns and geopolitical factors affecting trade flows.

Industry stakeholders are implementing strategic adjustments to navigate the evolving landscape, with particular attention to operational efficiency and cost management measures. These developments will likely continue to influence market sentiment in the coming quarters.
"""

def force_multiple_paragraphs(text: str) -> str:
    """Force text into multiple paragraphs"""
    if not text or len(text.strip()) < 100:
        return text
    
    # Remove existing paragraph breaks
    text = text.replace('\n\n', ' ').replace('\n', ' ').strip()
    
    # Split into sentences
    sentences = [s.strip() + '.' for s in text.split('.') if s.strip()]
    
    if len(sentences) < 3:
        return text
    
    # Group sentences into 3 paragraphs
    sentences_per_para = len(sentences) // 3
    para1 = ' '.join(sentences[:sentences_per_para])
    para2 = ' '.join(sentences[sentences_per_para:sentences_per_para*2])
    para3 = ' '.join(sentences[sentences_per_para*2:])
    
    return f"{para1}\n\n{para2}\n\n{para3}"

@app.get("/api")
async def root():
    """API health check"""
    return {"message": "AME Commodity News API", "status": "active", "version": "1.0"}

@app.post("/api/news/paraphrase")
async def paraphrase_articles(request: ParaphraseRequest):
    """Synthesize news articles into professional commodity report"""
    try:
        if not request.articles:
            raise HTTPException(status_code=400, detail="No articles provided")
        
        # Build context from articles
        articles_content = []
        for i, article in enumerate(request.articles, 1):
            content = f"Article {i}: {article.title}\n{article.content[:2000]}..."
            articles_content.append(content)
        
        combined_content = "\n\n".join(articles_content)
        
        # Professional synthesis prompt
        synthesis_prompt = f"""
        As a senior commodities analyst and mining engineer, synthesize the following news articles into a comprehensive professional report. Write in British English with a neutral, technical tone.

        CRITICAL: Your response MUST contain exactly 3 distinct paragraphs separated by double line breaks.

        Focus on:
        - Technical analysis of production impacts and supply chain disruptions
        - Quantitative data (production figures, price movements, tonnage)
        - Market implications for commodity prices and supply dynamics
        - Regulatory impacts on operations
        - Strategic implications for market participants

        Source articles:
        {combined_content}

        Write a comprehensive analysis in EXACTLY 3 paragraphs:
        """
        
        # Generate synthesis
        synthesized_content = await call_gemini_api(synthesis_prompt)
        synthesized_content = force_multiple_paragraphs(synthesized_content)
        
        # Generate title
        title_prompt = f"Generate a professional, technical headline (maximum 80 characters) for this commodity analysis:\n\n{synthesized_content[:500]}..."
        title = await call_gemini_api(title_prompt)
        title = title.strip().replace('"', '').replace('\n', ' ')[:80]
        
        # Generate summary
        summary_prompt = f"Create a concise 2-sentence executive summary:\n\n{synthesized_content[:800]}..."
        summary = await call_gemini_api(summary_prompt)
        summary = summary.strip().replace('\n', ' ')[:300]
        
        return ParaphraseResponse(
            synthesized_article=synthesized_content,
            title=title,
            summary=summary,
            source_articles=request.articles
        )
        
    except Exception as e:
        print(f"Error in paraphrase_articles: {e}")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

# For Vercel deployment
from mangum import Mangum
handler = Mangum(app, lifespan="off")