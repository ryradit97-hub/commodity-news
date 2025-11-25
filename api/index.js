export default async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight OPTIONS request
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // Get the path
  const path = req.url;

  // Simple routing
  if (path === '/api' && req.method === 'GET') {
    res.status(200).json({
      message: "AME Commodity News API",
      status: "active",
      version: "1.0",
      timestamp: new Date().toISOString()
    });
    return;
  }

  if (path === '/api/news/paraphrase' && req.method === 'POST') {
    try {
      const { articles } = req.body || {};
      
      if (!articles || articles.length === 0) {
        res.status(400).json({ error: "No articles provided" });
        return;
      }

      // Build context from articles
      const articlesContent = articles.map((article, i) => 
        `Article ${i + 1}: ${article.title}\n${article.content.substring(0, 2000)}...`
      ).join('\n\n');

      // Professional synthesis prompt
      const synthesisPrompt = `As a senior commodities analyst and mining engineer, synthesize the following news articles into a comprehensive professional report. Write in British English with a neutral, technical tone.

CRITICAL: Your response MUST contain exactly 3 distinct paragraphs separated by double line breaks.

Focus on:
- Technical analysis of production impacts and supply chain disruptions
- Quantitative data (production figures, price movements, tonnage)
- Market implications for commodity prices and supply dynamics
- Regulatory impacts on operations
- Strategic implications for market participants

Source articles:
${articlesContent}

Write a comprehensive analysis in EXACTLY 3 paragraphs:`;

      // Try AI synthesis
      let synthesizedContent = await callAI(synthesisPrompt);
      synthesizedContent = forceMultipleParagraphs(synthesizedContent);

      // Generate title and summary
      const title = await generateTitle(synthesizedContent);
      const summary = await generateSummary(synthesizedContent);

      const response = {
        synthesized_article: synthesizedContent,
        title: title,
        summary: summary,
        source_articles: articles
      };

      res.status(200).json(response);
      return;

    } catch (error) {
      console.error('Synthesis error:', error);
      res.status(500).json({ error: `Processing error: ${error.message}` });
      return;
    }
  }

  // Default response
  res.status(200).json({
    message: "Hello from Node.js!",
    status: "working",
    path: path
  });
}

// AI Integration Functions
async function callAI(prompt) {
  const geminiKey = process.env.GEMINI_API_KEY;
  const deepseekKey = process.env.DEEPSEEK_API_KEY;

  // Try Gemini first
  if (geminiKey) {
    try {
      const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${geminiKey}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: {
              temperature: 0.7,
              maxOutputTokens: 2000
            }
          })
        }
      );

      const result = await response.json();
      if (result.candidates && result.candidates[0]) {
        return result.candidates[0].content.parts[0].text;
      }
    } catch (error) {
      console.log('Gemini API error:', error);
    }
  }

  // Try DeepSeek fallback
  if (deepseekKey) {
    try {
      const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${deepseekKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'deepseek-chat',
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.7,
          max_tokens: 2000
        })
      });

      const result = await response.json();
      return result.choices[0].message.content;
    } catch (error) {
      console.log('DeepSeek API error:', error);
    }
  }

  // Final fallback template
  return `The global commodity markets continue to experience significant developments across multiple sectors. Supply chain dynamics remain a key focus for industry analysts as producers adapt to changing market conditions and implement strategic operational adjustments to maintain competitive positioning.

Market participants are closely monitoring production levels and infrastructure developments that could impact future supply availability. Price volatility reflects ongoing uncertainty about demand patterns and geopolitical factors affecting international trade flows, with particular attention to emerging market trends and regulatory changes.

Industry stakeholders are implementing strategic adjustments to navigate the evolving landscape, with particular attention to operational efficiency and cost management measures. These developments will likely continue to influence market sentiment and investment decisions in the coming quarters as the sector adapts to new realities.`;
}

async function generateTitle(content) {
  const prompt = `Generate a professional, technical headline (maximum 80 characters) for this commodity analysis:\n\n${content.substring(0, 500)}...`;
  try {
    const title = await callAI(prompt);
    return title.replace(/"/g, '').replace(/\n/g, ' ').substring(0, 80);
  } catch {
    return "Commodity Markets Navigate Evolving Supply Dynamics";
  }
}

async function generateSummary(content) {
  const prompt = `Create a concise 2-sentence executive summary:\n\n${content.substring(0, 800)}...`;
  try {
    const summary = await callAI(prompt);
    return summary.replace(/\n/g, ' ').substring(0, 300);
  } catch {
    return "Global commodity markets face ongoing supply chain challenges and price volatility. Industry participants implement strategic adjustments to manage operational efficiency.";
  }
}

function forceMultipleParagraphs(text) {
  if (!text || text.length < 100) return text;
  
  // Remove existing paragraph breaks
  text = text.replace(/\n\n/g, ' ').replace(/\n/g, ' ').trim();
  
  // Split into sentences
  const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
  
  if (sentences.length < 3) return text;
  
  // Group sentences into 3 paragraphs
  const sentencesPerPara = Math.ceil(sentences.length / 3);
  const para1 = sentences.slice(0, sentencesPerPara).join('. ') + '.';
  const para2 = sentences.slice(sentencesPerPara, sentencesPerPara * 2).join('. ') + '.';
  const para3 = sentences.slice(sentencesPerPara * 2).join('. ') + '.';
  
  return `${para1}\n\n${para2}\n\n${para3}`;
}