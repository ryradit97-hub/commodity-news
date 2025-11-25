from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from Flask!",
        "status": "working"
    })

@app.route('/api')  
def api():
    return jsonify({
        "message": "Flask API Working",
        "status": "ok"
    })

if __name__ == '__main__':
    app.run()