import requests
import json

# Test the synthesis endpoint to see what's actually happening
test_data = {
    "commodity": "gold",
    "start_date": "2024-01-01",
    "end_date": "2024-01-31",
    "articles": [
        {
            "title": "Gold prices rise on inflation concerns",
            "content": "Gold prices increased yesterday as investors sought safe haven assets amid rising inflation expectations. Market analysts noted strong demand from institutional buyers. Trading volumes reached elevated levels during the session.",
            "published_date": "2024-01-15",
            "url": "https://example.com/gold1"
        },
        {
            "title": "Central bank gold purchases continue",
            "content": "Central banks maintained their gold accumulation strategy in the first quarter. Reserve managers cited portfolio diversification benefits. Global gold reserves hit multi-year highs according to recent data.",
            "published_date": "2024-01-20", 
            "url": "https://example.com/gold2"
        }
    ]
}

print("🧪 Testing synthesis endpoint...")
response = requests.post("http://localhost:8001/synthesize", json=test_data)

if response.status_code == 200:
    result = response.json()
    article = result.get('synthesized_article', '')
    
    print(f"📄 Received article ({len(article)} chars):")
    print("=" * 60)
    print(article)
    print("=" * 60)
    
    # Count paragraphs
    paragraphs = [p.strip() for p in article.split('\n\n') if p.strip()]
    print(f"📊 Paragraph count: {len(paragraphs)}")
    
    for i, para in enumerate(paragraphs, 1):
        print(f"Paragraph {i} ({len(para)} chars): {para[:100]}...")
        
else:
    print(f"❌ Error {response.status_code}: {response.text}")