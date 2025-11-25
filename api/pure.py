import json

def handler(event, context):
    """Pure Python handler for Vercel - no FastAPI"""
    
    # Get the path from the event
    path = event.get('rawPath', event.get('path', '/'))
    method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'GET'))
    
    # Simple routing
    if path == '/api' and method == 'GET':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({
                "message": "Pure Python API Working",
                "status": "ok",
                "path": path
            })
        }
    
    # Default response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps({
            "message": "Hello from Pure Python!",
            "status": "working",
            "path": path
        })
    }