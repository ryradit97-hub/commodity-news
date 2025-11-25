#!/usr/bin/env python3
"""Test the fallback system - Gemini -> DeepSeek -> Template"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from main import generate_text_with_llm

def test_fallback_system():
    """Test the LLM fallback system"""
    
    test_prompt = """Write a short commodity market news article about copper prices rising due to supply concerns. 
    Format as 3 paragraphs separated by blank lines. Keep it under 500 characters total."""
    
    print("🧪 Testing LLM Fallback System")
    print("=" * 50)
    
    try:
        print("🔄 Attempting synthesis with fallback system...")
        result = generate_text_with_llm(test_prompt, max_tokens=300)
        
        print("✅ Synthesis successful!")
        print(f"📊 Length: {len(result)} characters")
        
        # Check paragraphs
        paragraphs = [p.strip() for p in result.split('\n\n') if p.strip()]
        print(f"📝 Paragraphs: {len(paragraphs)}")
        
        print("\n📄 Generated content:")
        print("-" * 30)
        print(result)
        print("-" * 30)
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_fallback_system()
    if success:
        print("\n🎉 Fallback system test PASSED!")
    else:
        print("\n❌ Fallback system test FAILED!")
    
    print("\n💡 Note: If you have a DeepSeek API key, add it to .env file:")
    print("   DEEPSEEK_API_KEY=your_key_here")
    print("   Get a key from: https://platform.deepseek.com/")