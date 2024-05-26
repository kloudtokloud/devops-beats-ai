from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze-data', methods=['POST'])
def analyze_data():
    data = request.json
    # Data analysis logic goes here
    
    result = {"analysis": "Sample analysis result"}
    
    return jsonify({'message': 'Data analyzed successfully!', 'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
