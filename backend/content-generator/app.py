import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'

@app.route('/generate-content', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get('prompt')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    content = response.choices[0].text.strip()
    
    return jsonify({'message': 'Content generated successfully!', 'content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
