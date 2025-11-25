#!/usr/bin/env python3
"""Quick test for paragraph generation"""

import requests
import json

def test_paragraph_generation():
    """Test that synthesis always generates 3+ paragraphs"""
    
    test_articles = {
        "articles": [
            {
                "title": "Copper prices surge on supply fears",
                "content": "Copper futures climbed 3.2% on Tuesday as mining disruptions in Chile raised supply concerns. The three-month copper contract on the London Metal Exchange reached $8,950 per tonne.",
                "url": "https://example.com/1",
                "published_date": "2024-01-16"
            },
            {
                "title": "Mining companies report strong earnings", 
                "content": "Major mining companies reported better-than-expected quarterly results, with profits boosted by higher metal prices and operational improvements.",
                "url": "https://example.com/2",
                "published_date": "2024-01-16"
            },
            {
                "title": "Analysts forecast continued demand growth",
                "content": "Industry experts predict sustained demand for copper driven by renewable energy projects and electric vehicle production.",
                "url": "https://example.com/3", 
                "published_date": "2024-01-16"
            }
        ]
    }
    
    try:
        print("🔄 Testing synthesis endpoint...")
        response = requests.post(
            "http://localhost:8001/synthesize",
            headers={"Content-Type": "application/json"},
            json=test_articles,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            article = result.get("synthesized_article", "")
            headline = result.get("headline", "")
            
            print(f"✅ Synthesis successful!")
            print(f"📰 Headline: {headline}")
            print(f"📊 Character count: {len(article)}")
            
            # Count paragraphs
            paragraphs = [p.strip() for p in article.split('\n\n') if p.strip()]
            paragraph_count = len(paragraphs)
            
            print(f"📝 Paragraph count: {paragraph_count}")
            
            if paragraph_count >= 3:
                print("🎉 SUCCESS: Multiple paragraphs generated!")
                print("\n📄 Generated article:")
                print("-" * 50)
                for i, para in enumerate(paragraphs, 1):
                    print(f"Paragraph {i}: {para}")
                    print()
                return True
            else:
                print("❌ FAILED: Only generated {paragraph_count} paragraph(s)")
                print(f"Article content: {article}")
                return False
                
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_paragraph_generation()
    if success:
        print("\n✅ Paragraph generation test PASSED!")
    else:
        print("\n❌ Paragraph generation test FAILED!")