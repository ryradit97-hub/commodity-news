# AME Commodity News - Vercel Deployment

A professional FastAPI application for synthesizing commodity news articles using AI, optimized for Vercel deployment.

## Features

- **News Search**: Search for commodity-related news using SerpAPI
- **Article Paraphrasing**: Paraphrase news articles using T5 transformer model from Hugging Face
- **RESTful API**: Built with FastAPI for high performance
- **Input Validation**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive error handling and logging

## Prerequisites

- Python 3.8 or higher
- **No API key required** for basic usage (uses free Google News RSS)
- Optional: NewsAPI key for more features (free tier available at https://newsapi.org/)
- Optional: SerpAPI key for advanced features (https://serpapi.com/)

## Installation

1. Clone the repository:
```bash
cd AME-CommodityNews
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure environment variables (optional):
```bash
# Copy the example env file
cp .env.example .env

# For FREE usage with Google News RSS (no API key needed):
# SEARCH_PROVIDER=rss (this is the default)

# For NewsAPI (FREE - 100 requests/day):
# Get key at https://newsapi.org/register
# SEARCH_PROVIDER=newsapi
# NEWSAPI_KEY=your_actual_newsapi_key

# For SerpAPI (PAID with free tier):
# SEARCH_PROVIDER=serpapi
# SERPAPI_API_KEY=your_actual_serpapi_key
```

## Running the Application

Start the FastAPI server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### 1. Search News - `GET /news/search`

Search for **global** commodity-related news articles **from the last 7 days** using multiple providers.

**⚠️ IMPORTANT**: 
- Only searches news from the past 7 days. News older than 7 days is not available.
- Searches globally across all countries - not limited to any specific region.

**Query Parameters:**
- `commodity` (required): The commodity to search for (e.g., "gold", "oil", "wheat", "copper")
- `provider` (optional): Search provider - `rss` (default, free), `newsapi` (free tier), or `serpapi` (paid)

**Example Requests:**
```bash
# Using free Google News RSS (default, no API key needed)
curl "http://localhost:8001/news/search?commodity=gold"

# Search for oil news
curl "http://localhost:8001/news/search?commodity=oil"

# Using NewsAPI (free tier - 100 requests/day)
curl "http://localhost:8001/news/search?commodity=copper&provider=newsapi"

# Using SerpAPI (paid)
curl "http://localhost:8001/news/search?commodity=wheat&provider=serpapi"
```

**Example Response:**
```json
{
  "query": "gold commodity news USA date:2025-11-24",
  "total_results": 10,
  "articles": [
    {
      "title": "Gold Prices Surge Amid Economic Uncertainty",
      "link": "https://example.com/article",
      "snippet": "Gold prices reached new highs...",
      "source": "Reuters"
    }
  ]
}
```

### 2. Synthesize & Paraphrase Articles - `POST /news/paraphrase`

**AME Research News Synthesizer**: Combines multiple news articles into one unified, publication-ready report.

**Features:**
- Synthesizes multiple articles into coherent narrative
- Removes duplicates and resolves conflicting data
- Produces factual, professional content
- Maintains global commodity and market context

**Output Format:**
1. Combined Summary (5-7 bullet points)
2. Unified Article (8-15 sentences, publication-ready)
3. Short Version (3-5 sentences, compact)

**Request Body:**
```json
{
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
```

**Example Request:**
```bash
curl -X POST "http://localhost:8001/news/paraphrase" \
  -H "Content-Type: application/json" \
  -d '{
    "articles": [
      {
        "title": "Gold Prices Surge",
        "content": "Gold prices reached a new high today."
      },
      {
        "title": "Gold Rally Continues",
        "content": "The precious metal extended gains."
      }
    ]
  }'
```

**Example Response:**
```json
{
  "combined_summary": [
    "Gold prices reached record highs",
    "Investors seeking safe-haven assets",
    "Market turbulence driving demand",
    "Precious metals showing strong gains",
    "Global economic concerns persist"
  ],
  "unified_article": "Gold prices have surged to new record highs as investors increasingly turn to safe-haven assets...",
  "paraphrased_short_version": "Gold hit record highs as economic uncertainty drove investors to safe-haven assets.",
  "source_count": 2
}
```

## Project Structure

```
AME-CommodityNews/
├── main.py              # FastAPI application and endpoints
├── models.py            # Pydantic models for validation
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .env                # Your environment variables (not in git)
└── README.md           # This file
```

## Search Provider Options

### 1. Google News RSS (FREE - Recommended for getting started)
- **Cost**: Completely free
- **Limits**: No registration or API key required
- **Pros**: Instant setup, reliable, good coverage
- **Cons**: Limited filtering options, no advanced features
- **Setup**: Works out of the box!

### 2. NewsAPI (FREE Tier)
- **Cost**: Free tier with 100 requests/day
- **Limits**: Developer plan limited to 100 requests/day
- **Pros**: Well-structured data, good filtering, free tier available
- **Cons**: Requires registration, free tier has limitations
- **Setup**: Register at https://newsapi.org/register

### 3. SerpAPI (PAID)
- **Cost**: Paid service with limited free tier (100 searches/month)
- **Limits**: Free tier: 100 searches/month, then paid plans
- **Pros**: Most comprehensive, Google Search quality, advanced features
- **Cons**: Requires payment for heavy use
- **Setup**: Register at https://serpapi.com/

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Transformers**: Hugging Face library for NLP models
- **T5**: Text-to-Text Transfer Transformer for paraphrasing
- **Feedparser**: RSS feed parsing for free Google News search
- **NewsAPI**: Optional free-tier news API
- **SerpAPI**: Optional paid Google search API wrapper
- **Uvicorn**: ASGI server for running FastAPI

## Error Handling

The API includes comprehensive error handling:
- Missing API keys return 500 with descriptive message
- Invalid requests return 422 with validation errors
- External API failures return 503 with error details
- Unexpected errors return 500 with error information

## Notes

- The paraphrasing model (T5-base) is loaded lazily on first use to improve startup time
- For production use, consider using a GPU for faster paraphrasing
- The T5 model input is limited to 400 characters for the content to ensure processing efficiency
- Content length can be adjusted in `main.py` based on your needs

## License

MIT License

## Support

For issues or questions, please open an issue in the repository.
