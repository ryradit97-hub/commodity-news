@echo off
echo =============================================================
echo AME Commodity News - Complete Deployment Setup
echo =============================================================
echo.

echo Creating deployment structure...
echo.

REM Create frontend directory
echo [1/6] Setting up frontend structure...
mkdir frontend 2>nul
copy /Y "static\index.html" "frontend\index.html"
copy /Y "frontend-package.json" "frontend\package.json"
copy /Y "vercel.json" "frontend\vercel.json"
copy /Y "frontend-README.md" "frontend\README.md"

REM Create backend directory  
echo [2/6] Setting up backend structure...
mkdir backend 2>nul
copy /Y "main.py" "backend\main.py"
copy /Y "models.py" "backend\models.py"
copy /Y "requirements.txt" "backend\requirements.txt"
copy /Y "Procfile" "backend\Procfile"
copy /Y "runtime.txt" "backend\runtime.txt"
copy /Y "render.yaml" "backend\render.yaml"
copy /Y ".env" "backend\.env" 2>nul
copy /Y ".gitignore" "backend\.gitignore"

echo [3/6] Creating backend README...
echo # AME Commodity News - Backend API > backend\README.md
echo. >> backend\README.md
echo Professional FastAPI backend for commodity news synthesis. >> backend\README.md
echo. >> backend\README.md
echo ## Deployment Platforms >> backend\README.md
echo - Railway: Connect this repository and deploy >> backend\README.md
echo - Render: Use render.yaml configuration >> backend\README.md
echo - Heroku: Use Procfile configuration >> backend\README.md
echo. >> backend\README.md
echo ## Environment Variables Required: >> backend\README.md
echo - GEMINI_API_KEY=your_gemini_key >> backend\README.md
echo - DEEPSEEK_API_KEY=your_deepseek_key >> backend\README.md
echo - ALLOWED_ORIGINS=https://your-frontend.vercel.app >> backend\README.md

echo [4/6] Creating deployment instructions...
echo.
echo =============================================================
echo DEPLOYMENT INSTRUCTIONS CREATED
echo =============================================================
echo.
echo FRONTEND (UI) - Deploy to Vercel:
echo 1. Push 'frontend' folder to: https://github.com/ryradit97-hub/commodity-news-frontend
echo 2. Connect to Vercel and deploy
echo 3. Get your frontend URL: https://your-app.vercel.app
echo.
echo BACKEND (API) - Deploy to Railway (Recommended):
echo 1. Push 'backend' folder to: https://github.com/ryradit97-hub/commodity-news-backend  
echo 2. Connect to Railway: https://railway.app/
echo 3. Set environment variables:
echo    - GEMINI_API_KEY=your_gemini_api_key_here
echo    - DEEPSEEK_API_KEY=your_deepseek_api_key_here
echo    - ALLOWED_ORIGINS=https://your-frontend.vercel.app
echo 4. Deploy and get API URL: https://your-api.railway.app
echo.
echo [5/6] IMPORTANT: Update API URL in frontend
echo After backend deployment, update the API_BASE_URL in:
echo frontend\index.html (line ~480)
echo Change: const API_BASE_URL = 'http://localhost:8001';
echo To: const API_BASE_URL = 'https://your-api.railway.app';
echo.
echo [6/6] Cost Estimate:
echo - Vercel (Frontend): FREE
echo - Railway (Backend): ~$5/month 
echo - Total: ~$5/month
echo.
echo =============================================================
echo READY FOR DEPLOYMENT!
echo =============================================================
echo.
echo Next Steps:
echo 1. Create two GitHub repositories (frontend and backend)
echo 2. Push respective folders to each repository
echo 3. Deploy frontend to Vercel
echo 4. Deploy backend to Railway
echo 5. Update API URLs and test
echo.
pause