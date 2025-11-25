@echo off
echo ========================================
echo   AME Commodity News - Vercel Deploy
echo ========================================
echo.

echo 1. Initializing Git repository...
git init

echo 2. Adding all files...
git add .

echo 3. Creating initial commit...
git commit -m "Initial commit - AME Commodity News System ready for Vercel"

echo 4. Setting main branch...
git branch -M main

echo.
echo ========================================
echo          DEPLOYMENT READY!
echo ========================================
echo.
echo Next steps:
echo 1. Create GitHub repository: https://github.com/new
echo 2. Copy the repository URL
echo 3. Run: git remote add origin YOUR_REPO_URL
echo 4. Run: git push -u origin main
echo 5. Go to https://vercel.com and import your repository
echo 6. Add environment variables in Vercel dashboard:
echo    - GEMINI_API_KEY = your_gemini_api_key_here
echo    - DEEPSEEK_API_KEY = your_deepseek_api_key_here
echo 7. Deploy!
echo.
echo Your app will be available at: https://your-app-name.vercel.app
echo API endpoints at: https://your-app-name.vercel.app/api/
echo.
echo Cost: FREE on Vercel (generous free tier)
echo.
pause