# AME Commodity News - Frontend for Vercel

Professional frontend interface for the AME Commodity News Synthesis API.

## Features

- 🔍 **Multi-source news search** (RSS, NewsAPI, SerpAPI)
- 🤖 **AI-powered synthesis** with professional formatting
- 📊 **Real-time character/word counting** with validation
- 📤 **Export capabilities** (DOCX and PDF with references)
- 🎨 **Professional UI** with responsive design
- ⚡ **Fast performance** with optimized loading

## Deployment

This frontend is designed to be deployed on Vercel and connect to the AME Commodity News API backend.

### Backend API Connection

The frontend connects to the backend API. Update the API base URL in the JavaScript section:

```javascript
// Update this URL to your deployed backend
const API_BASE_URL = 'https://your-api-domain.railway.app';
```

### Local Development

1. Open `index.html` in your browser
2. Ensure backend API is running on `localhost:8001`
3. Test the complete workflow: Search → Synthesize → Export

### Production Deployment

1. Deploy backend API to Railway/Render/Heroku
2. Update `API_BASE_URL` in index.html to production backend URL
3. Deploy to Vercel by connecting this repository

## Architecture

```
User Browser → Vercel (Frontend) → Railway (Backend API) → AI Services
```

## Professional Standards

- British English terminology
- Engineering and analyst reporting standards
- Technical focus on CAPEX, production targets, resource estimates
- Professional document formatting with references
- Industry-standard export capabilities

## Support

For issues related to:
- **Frontend/UI**: Check browser console for errors
- **API connectivity**: Verify backend deployment status
- **Export functionality**: Ensure backend has proper dependencies
- **Search issues**: Check search provider configuration

---

**Professional commodity news synthesis interface for industry analysis.**