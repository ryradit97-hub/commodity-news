# AME Commodity News - Deployment Guide

## Architecture Overview

```
Frontend (UI) -> Vercel
Backend (API) -> Railway/Render/Heroku
```

## Part 1: Frontend Deployment to Vercel

### Step 1: Create Separate Frontend Repository

Create a new repository for the UI only:

1. Create `frontend/` directory structure:
```
frontend/
├── index.html          # Your UI file
├── package.json        # For Vercel deployment
├── vercel.json        # Vercel configuration
└── README.md          # Frontend documentation
```

### Step 2: Prepare Frontend Files

**package.json** (for Vercel):
```json
{
  "name": "ame-commodity-news-frontend",
  "version": "1.0.0",
  "description": "AME Commodity News Frontend",
  "main": "index.html",
  "scripts": {
    "build": "echo 'No build required for static HTML'",
    "start": "echo 'Static site - no start command needed'"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

**vercel.json** (Vercel configuration):
```json
{
  "functions": {},
  "rewrites": [
    {
      "source": "/",
      "destination": "/index.html"
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Access-Control-Allow-Methods", 
          "value": "GET, POST, PUT, DELETE, OPTIONS"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "Content-Type, Authorization"
        }
      ]
    }
  ]
}
```

### Step 3: Update Frontend API URLs

In your `index.html`, update the API endpoints to point to your deployed backend:

```javascript
// Replace localhost URLs with your deployed API URL
const API_BASE_URL = 'https://your-api-domain.railway.app'; // or your chosen platform

// Update all fetch calls
fetch(`${API_BASE_URL}/news/search?commodity=${commodity}&provider=rss`)
fetch(`${API_BASE_URL}/news/paraphrase`, {...})
fetch(`${API_BASE_URL}/export/docx`, {...})
```

### Step 4: Deploy to Vercel

1. Push frontend to GitHub repository
2. Connect to Vercel: https://vercel.com/
3. Import your frontend repository
4. Deploy automatically

## Part 2: Backend API Deployment

### Option 1: Railway (Recommended - Free Tier)

**Why Railway:**
- Free tier: $5 credit monthly
- Easy Python deployment
- Automatic HTTPS
- Environment variables support
- Database hosting available

**Deployment Steps:**

1. **Prepare for Railway:**
   - Create `Procfile`:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

   - Create `runtime.txt`:
   ```
   python-3.11
   ```

   - Update `requirements.txt` (add gunicorn):
   ```
   fastapi==0.104.1
   uvicorn[standard]==0.24.0
   gunicorn==21.2.0
   pydantic==2.5.0
   requests==2.31.0
   python-dotenv==1.0.0
   python-dateutil==2.8.2
   feedparser==6.0.10
   google-generativeai>=0.3.0
   python-docx>=0.8.11
   reportlab>=3.6.0
   ```

2. **Railway Deployment:**
   - Go to https://railway.app/
   - Connect GitHub repository
   - Select your backend repository
   - Add environment variables:
     - `GEMINI_API_KEY=your_key`
     - `DEEPSEEK_API_KEY=your_key`
     - `PORT=8001`
   - Deploy automatically

### Option 2: Render (Free Tier Alternative)

**Deployment Steps:**

1. **Create `render.yaml`:**
```yaml
services:
  - type: web
    name: ame-commodity-api
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: GEMINI_API_KEY
        sync: false
      - key: DEEPSEEK_API_KEY
        sync: false
```

2. **Deploy on Render:**
   - Go to https://render.com/
   - Connect GitHub repository
   - Configure environment variables
   - Deploy

### Option 3: Heroku (Paid)

**Deployment Steps:**

1. **Create `Procfile`:**
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
release: echo "Release phase"
```

2. **Deploy to Heroku:**
   - Install Heroku CLI
   - `heroku create your-app-name`
   - `heroku config:set GEMINI_API_KEY=your_key`
   - `git push heroku main`

## Step-by-Step Complete Deployment

### Phase 1: Separate Repositories

1. **Create frontend repository:**
```bash
mkdir ame-commodity-frontend
cd ame-commodity-frontend
# Copy index.html and create package.json, vercel.json
git init
git add .
git commit -m "Frontend for AME Commodity News"
git remote add origin https://github.com/ryradit97-hub/commodity-news-frontend.git
git push -u origin main
```

2. **Create backend repository:**
```bash
mkdir ame-commodity-backend  
cd ame-commodity-backend
# Copy main.py, models.py, requirements.txt
# Create Procfile, runtime.txt
git init
git add .
git commit -m "Backend API for AME Commodity News"
git remote add origin https://github.com/ryradit97-hub/commodity-news-backend.git
git push -u origin main
```

### Phase 2: Deploy Backend

1. **Choose platform:** Railway (recommended)
2. **Connect repository** to chosen platform
3. **Set environment variables:**
   - GEMINI_API_KEY
   - DEEPSEEK_API_KEY
   - PORT (if required)
4. **Deploy and get URL:** e.g., `https://your-app.railway.app`

### Phase 3: Deploy Frontend

1. **Update API URLs** in index.html to backend URL
2. **Deploy to Vercel:**
   - Connect GitHub repository
   - Configure project settings
   - Deploy automatically
3. **Get frontend URL:** e.g., `https://your-app.vercel.app`

## Environment Variables Setup

### Backend Environment Variables:
```
GEMINI_API_KEY=your_gemini_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
SEARCH_PROVIDER=rss
PORT=8001
```

### CORS Configuration

Update your FastAPI CORS settings for production:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend.vercel.app",
        "http://localhost:3000",  # for local development
        "http://localhost:8001"   # for local testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Cost Breakdown

### Free Tier Options:
- **Vercel (Frontend):** Free for personal projects
- **Railway (Backend):** $5 monthly credit (usually sufficient)
- **Render (Backend Alternative):** Free tier with limitations

### Total Monthly Cost: ~$0-5

## Testing Deployment

1. **Test backend API:** `https://your-api.railway.app/docs`
2. **Test frontend:** `https://your-app.vercel.app`
3. **Test integration:** Search -> Synthesize -> Export workflow

## Monitoring & Maintenance

1. **Railway Dashboard:** Monitor API usage and performance
2. **Vercel Analytics:** Track frontend usage
3. **Error Logging:** Check platform logs for issues
4. **API Keys:** Monitor usage limits for Gemini/DeepSeek

## Troubleshooting

### Common Issues:
1. **CORS errors:** Update CORS origins in FastAPI
2. **API timeouts:** Check hosting platform limits
3. **Large file exports:** Consider file size limits
4. **Environment variables:** Verify all keys are set correctly

---

**Ready to deploy your professional AME Commodity News system to production!**