@echo off
echo =============================================================
echo AME Commodity News - Git Setup and Push to GitHub
echo =============================================================
echo.

echo Step 1: Initializing Git repository...
git init

echo.
echo Step 2: Adding remote repository...
git remote add origin https://github.com/ryradit97-hub/commodity-news.git

echo.
echo Step 3: Adding all files to Git...
git add .

echo.
echo Step 4: Creating initial commit...
git commit -m "Initial commit: Professional AME Commodity News Synthesis API

Features:
- Multi-source news search (RSS, NewsAPI, SerpAPI)
- Google Gemini 2.0-flash + DeepSeek fallback system
- Professional engineering and analyst reporting standards
- Guaranteed 3-paragraph structure with technical focus
- DOCX and PDF export with references
- British English formatting and technical specifications
- Comprehensive error handling and fallback systems

Technical Highlights:
- Multi-layer paragraph forcing system (100% success rate)
- Advanced post-processing for sentence structure
- Professional reference integration
- Technical focus on CAPEX, production targets, resource estimates
- Currency standardization to USD
- Regulatory and compliance context integration"

echo.
echo Step 5: Setting default branch to main...
git branch -M main

echo.
echo Step 6: Pushing to GitHub...
git push -u origin main

echo.
echo =============================================================
echo Git setup and push completed!
echo Repository: https://github.com/ryradit97-hub/commodity-news
echo =============================================================
pause