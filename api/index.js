export default function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight OPTIONS request
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // Simple routing
  if (req.url === '/api' && req.method === 'GET') {
    res.status(200).json({
      message: "Node.js API Working",
      status: "ok",
      version: "1.0"
    });
    return;
  }

  if (req.url === '/api/news/paraphrase' && req.method === 'POST') {
    try {
      const articles = req.body?.articles || [];
      
      // Simple template response - no AI calls for now
      const response = {
        synthesized_article: "The global commodity markets continue to experience significant developments across multiple sectors. Supply chain dynamics remain a key focus for industry analysts as producers adapt to changing market conditions.\n\nMarket participants are closely monitoring production levels and infrastructure developments that could impact future supply availability. Price volatility reflects ongoing uncertainty about demand patterns and geopolitical factors.\n\nIndustry stakeholders are implementing strategic adjustments to navigate the evolving landscape, with particular attention to operational efficiency and cost management measures.",
        title: "Commodity Markets Navigate Supply Chain Challenges",
        summary: "Global commodity markets face ongoing supply chain disruptions and price volatility as industry participants implement strategic operational adjustments.",
        source_articles: articles
      };

      res.status(200).json(response);
      return;

    } catch (error) {
      res.status(500).json({ error: "Processing error" });
      return;
    }
  }

  // Default response
  res.status(200).json({
    message: "Hello from Node.js!",
    status: "working"
  });
}

