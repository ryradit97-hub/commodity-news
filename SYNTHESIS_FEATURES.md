# AME Research News Synthesizer - Updated Features

## 🎯 Overview

The API has been upgraded to function as an **AME Research News Synthesizer** - a professional tool for combining multiple commodity news articles into unified, publication-ready reports.

## ✨ Key Features

### 1. Multi-Article Synthesis
- **Combines multiple news sources** into one coherent narrative
- **Removes duplicates** and repeated facts across articles
- **Resolves conflicts** in data (mentions ranges or most cited figures)
- **Maintains context** for global commodity and market news

### 2. Three Output Formats
Each synthesis produces:

1. **Combined Summary** (5-7 bullet points)
   - Key facts extracted from all sources
   - Easy to scan overview

2. **Unified Article** (8-15 sentences)
   - Professional, publication-ready news report
   - Flows like a real article
   - Neutral, factual tone

3. **Short Version** (3-5 sentences)
   - Compact summary
   - Perfect for quick updates or social media

### 3. AME Research Guidelines
The synthesizer follows professional journalism standards:
- ✅ **No hallucination** - Only includes facts from provided articles
- ✅ **Factual accuracy** - Mentions data ranges when sources differ
- ✅ **Coherent narrative** - Combines similar events smoothly
- ✅ **Professional tone** - Neutral, publication-ready style
- ✅ **Global context** - Maintains commodity and market perspective

## 🌐 Web Interface Features

### Search Tab
1. Search for global commodity news (last 7 days)
2. View results with titles, snippets, and sources
3. **NEW**: Click "Synthesize All Articles" button to automatically:
   - Collect all search results
   - Switch to synthesis tab
   - Generate unified report

### Synthesis Tab
1. Add multiple articles manually (title + content)
2. Click "+" to add more articles
3. Submit for AI synthesis
4. Receive three formatted outputs

## 📊 Typical Workflow

### Workflow 1: Automated (Recommended)
```
1. Search for commodity (e.g., "gold")
   ↓
2. Review search results
   ↓
3. Click "Synthesize All Articles"
   ↓
4. Receive unified report with:
   - Bullet summary
   - Full article
   - Short version
```

### Workflow 2: Manual
```
1. Go to "Paraphrase Article" tab
   ↓
2. Add article 1 (title + content)
   ↓
3. Click "+" to add more articles
   ↓
4. Click "Synthesize & Paraphrase Articles"
   ↓
5. Receive unified report
```

## 🔧 Technical Implementation

### Backend (FastAPI)
- `/news/search` - Search global news (7-day limit)
- `/news/paraphrase` - Synthesize multiple articles
- T5 transformer model for text generation
- Smart article combination logic

### Frontend (HTML/CSS/JS)
- Modern, responsive UI
- Dynamic article input forms
- One-click synthesis from search results
- Beautiful result presentation

### API Request Format
```json
{
  "articles": [
    {
      "title": "Article 1 Title",
      "content": "Article 1 content..."
    },
    {
      "title": "Article 2 Title", 
      "content": "Article 2 content..."
    }
  ]
}
```

### API Response Format
```json
{
  "combined_summary": ["Point 1", "Point 2", "..."],
  "unified_article": "Full synthesized article text...",
  "paraphrased_short_version": "Short summary...",
  "source_count": 2
}
```

## 🚀 Usage Examples

### Example 1: Gold Market News
**Input:** 3 articles about gold prices
**Output:**
- Summary: Key price movements, investor behavior, market drivers
- Article: 12-sentence unified report on gold market
- Short: 4-sentence quick update

### Example 2: Oil Supply Disruption
**Input:** 5 articles about oil supply issues
**Output:**
- Summary: Supply data, affected regions, price impacts
- Article: Comprehensive report combining all sources
- Short: Essential facts in brief format

## 💡 Best Practices

1. **Use 2-5 articles** for best synthesis results
2. **Include diverse sources** for comprehensive coverage
3. **Use recent articles** (within 7 days) for relevance
4. **Review output** before publication
5. **Combine search + synthesis** for fastest workflow

## 🎨 UI Improvements

- **Professional gradient design** (purple/blue)
- **Tabbed interface** for easy navigation
- **Loading indicators** with spinners
- **Color-coded sections** for clarity
- **Responsive layout** for all screen sizes
- **One-click synthesis** from search results

## 📝 Notes

- First synthesis may be slow (model loading)
- Subsequent syntheses are faster
- Works best with English content
- Output length adapts to input complexity
- Free to use with RSS provider (no API key)

## 🔗 Access

- **Web UI**: http://localhost:8001/
- **API Docs**: http://localhost:8001/docs
- **Alternative Docs**: http://localhost:8001/redoc
