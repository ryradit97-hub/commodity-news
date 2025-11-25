#!/usr/bin/env python3
"""Test just the paragraph forcing logic"""

def test_paragraph_forcing():
    """Test paragraph forcing with sample text"""
    
    # Sample long text without paragraph breaks (like what the LLM returns)
    sample_text = "China's steel production declined on Wednesday, 19 November 2025, according to a Reuters report. The contraction in steel output coincided with a trend of increasing iron ore imports into China, potentially nearing record levels. The precise figures for the decline in steel production and the volume of iron ore imports were not specified in the source material. Iron ore prices experienced a surge, reaching a two-week high on the same day, Wednesday, 19 November 2025, as noted by Seeking Alpha. The price increase was attributed to a combination of factors: robust demand and a reduction in supply originating from China. The specifics of the demand drivers and the reasons for the supply reduction within China were not elaborated upon in the source. S&P Global provided market data, analyses, and pricing information concerning the non-ferrous metals sector. Their publications offer comprehensive coverage of market trends and price movements."
    
    print(f"📝 Original text: {len(sample_text)} characters")
    print(f"🔍 Original paragraphs: {len([p for p in sample_text.split('\\n\\n') if p.strip()])}")
    
    # Apply the paragraph forcing logic
    clean_text = sample_text.replace('\n\n', ' ').replace('\n', ' ').strip()
    
    # Split into sentences more aggressively
    sentences = []
    temp_sentences = clean_text.split('.')
    for s in temp_sentences:
        s = s.strip()
        if len(s) > 20:  # Only keep substantial sentences
            sentences.append(s)
    
    print(f"📝 Extracted {len(sentences)} substantial sentences")
    
    # FORCE exactly 3 paragraphs
    if len(sentences) >= 3:
        if len(sentences) <= 6:
            # Small number: distribute evenly
            para1 = sentences[0] + '.'
            if len(sentences) == 3:
                para2 = sentences[1] + '.'
                para3 = sentences[2] + '.'
            elif len(sentences) == 4:
                para2 = sentences[1] + '.'
                para3 = '. '.join([sentences[2], sentences[3]]) + '.'
            elif len(sentences) == 5:
                para2 = '. '.join([sentences[1], sentences[2]]) + '.'
                para3 = '. '.join([sentences[3], sentences[4]]) + '.'
            else:  # 6 sentences
                para2 = '. '.join([sentences[1], sentences[2]]) + '.'
                para3 = '. '.join([sentences[3], sentences[4], sentences[5]]) + '.'
        else:
            # Many sentences: create balanced paragraphs
            third = len(sentences) // 3
            remainder = len(sentences) % 3
            
            if remainder == 1:
                p1_end = third + 1
                p2_end = p1_end + third
            elif remainder == 2:
                p1_end = third + 1
                p2_end = p1_end + third + 1
            else:
                p1_end = third
                p2_end = p1_end + third
            
            para1 = '. '.join(sentences[:p1_end]) + '.'
            para2 = '. '.join(sentences[p1_end:p2_end]) + '.'
            para3 = '. '.join(sentences[p2_end:]) + '.'
    
    # Reconstruct article with proper paragraph breaks
    result = f"{para1}\n\n{para2}\n\n{para3}".strip()
    
    # Check results
    final_paragraphs = [p.strip() for p in result.split('\n\n') if p.strip()]
    
    print(f"✅ Final text: {len(result)} characters")
    print(f"✅ Final paragraphs: {len(final_paragraphs)}")
    
    print("\n📄 Result:")
    print("=" * 60)
    for i, para in enumerate(final_paragraphs, 1):
        print(f"Paragraph {i}: {para}")
        print()
    
    return len(final_paragraphs) >= 3

if __name__ == "__main__":
    success = test_paragraph_forcing()
    if success:
        print("🎉 Paragraph forcing test PASSED!")
    else:
        print("❌ Paragraph forcing test FAILED!")