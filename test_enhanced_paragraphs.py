#!/usr/bin/env python3
"""Test the enhanced paragraph forcing system"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import synthesize_articles

def test_paragraph_forcing():
    """Test that synthesis ALWAYS creates 3+ paragraphs"""
    
    test_articles = [
        {
            "title": "Copper prices rise on supply concerns",
            "content": "Copper futures increased 2.5% yesterday as mining disruptions in Chile raised supply concerns. The London Metal Exchange saw significant trading activity.",
            "url": "https://example.com/1",
            "published_date": "2024-11-25"
        },
        {
            "title": "Mining companies report earnings",
            "content": "Several major mining companies reported quarterly earnings that exceeded analyst expectations. Strong demand for metals supported higher revenues.",
            "url": "https://example.com/2", 
            "published_date": "2024-11-25"
        },
        {
            "title": "Market outlook remains positive",
            "content": "Industry analysts forecast continued demand growth for copper and other base metals through 2025. Infrastructure projects drive consumption.",
            "url": "https://example.com/3",
            "published_date": "2024-11-25"
        }
    ]
    
    print("🧪 Testing Enhanced Paragraph Forcing System")
    print("=" * 60)
    
    try:
        print("🔄 Running synthesis with enhanced paragraph forcing...")
        result = synthesize_articles(test_articles)
        
        article = result["synthesized_article"]
        headline = result["headline"]
        
        print(f"📰 Headline: {headline}")
        print(f"📊 Total Length: {len(article)} characters")
        
        # Count paragraphs
        paragraphs = [p.strip() for p in article.split('\n\n') if p.strip()]
        print(f"📝 Paragraph Count: {len(paragraphs)}")
        
        print("\n📄 Generated Article:")
        print("=" * 40)
        for i, para in enumerate(paragraphs, 1):
            print(f"Paragraph {i} ({len(para)} chars):")
            print(para)
            print()
        
        # Verify success
        if len(paragraphs) >= 3:
            print("🎉 SUCCESS: Generated 3+ paragraphs!")
            return True
        else:
            print(f"❌ FAILED: Only {len(paragraphs)} paragraphs generated")
            return False
            
    except Exception as e:
        print(f"❌ Error during test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_paragraph_forcing()
    if success:
        print("\n✅ Enhanced paragraph forcing test PASSED!")
    else:
        print("\n❌ Enhanced paragraph forcing test FAILED!")