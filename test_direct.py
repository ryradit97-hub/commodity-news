#!/usr/bin/env python3
"""Direct test of the synthesis function"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import synthesize_articles
from models import ParaphraseRequest

def test_direct_synthesis():
    """Test synthesis function directly"""
    
    import signal
    import time
    
    def timeout_handler(signum, frame):
        raise TimeoutError("Test timed out after 60 seconds")
    
    # Set timeout for Windows (signal doesn't work the same way)
    start_time = time.time()
    
    # Create test data
    test_request = ParaphraseRequest(
        articles=[
            {
                "title": "China steel production declines",
                "content": "China's steel production experienced a decline on Wednesday, 19 November 2025, according to Reuters. This contraction occurred concurrently with iron ore imports trending towards record levels.",
                "url": "https://example.com/1",
                "published_date": "2024-11-19"
            },
            {
                "title": "Iron ore prices surge",
                "content": "Iron ore prices reached a two-week high on Wednesday, 19 November 2025, as reported by Seeking Alpha. The price increase was attributed to firm demand and reduced supply from China.",
                "url": "https://example.com/2", 
                "published_date": "2024-11-19"
            },
            {
                "title": "Market analysis shows trends",
                "content": "S&P Global published data, analysis, and prices for the non-ferrous metals sector showing continued market volatility and supply chain disruptions.",
                "url": "https://example.com/3",
                "published_date": "2024-11-19"
            }
        ]
    )
    
    try:
        print("🔄 Testing direct synthesis...")
        result = synthesize_articles(test_request.articles)
        
        print("✅ Synthesis completed!")
        print(f"📰 Headline: {result['headline']}")
        print(f"📊 Character count: {len(result['synthesized_article'])}")
        
        # Check paragraphs
        paragraphs = [p.strip() for p in result['synthesized_article'].split('\n\n') if p.strip()]
        print(f"📝 Paragraph count: {len(paragraphs)}")
        
        print("\n📄 Article content:")
        print("=" * 60)
        for i, para in enumerate(paragraphs, 1):
            print(f"Paragraph {i}:")
            print(para)
            print()
        
        if len(paragraphs) >= 3:
            print("🎉 SUCCESS: Generated 3+ paragraphs!")
            return True
        else:
            print(f"❌ FAILED: Only {len(paragraphs)} paragraphs generated")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_direct_synthesis()
    if success:
        print("\n✅ Direct synthesis test PASSED!")
    else:
        print("\n❌ Direct synthesis test FAILED!")