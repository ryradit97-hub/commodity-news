#!/usr/bin/env python3
"""Test script to verify Google Gemini API functionality"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_gemini_api():
    """Test basic Gemini API functionality"""
    try:
        import google.generativeai as genai
        
        # Get API key
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ GEMINI_API_KEY not found in environment")
            return False
            
        print(f"✅ API Key found: {api_key[:10]}...{api_key[-5:]}")
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Test with simple prompt
        test_prompt = "Write a short paragraph about copper mining in 100 words."
        print(f"🔄 Testing with prompt: {test_prompt}")
        
        response = model.generate_content(
            test_prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=150,
                temperature=0.7
            )
        )
        
        print("✅ Gemini API response received:")
        print(response.text.strip())
        print(f"📊 Response length: {len(response.text.strip())} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Gemini API error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Google Gemini API...")
    success = test_gemini_api()
    if success:
        print("\n✅ Gemini API test completed successfully!")
    else:
        print("\n❌ Gemini API test failed!")