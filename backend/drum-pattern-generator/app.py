import openai
import pretty_midi
import boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'
s3_client = boto3.client('s3')
S3_BUCKET_NAME = 'your-s3-bucket-name'

def generate_midi_drum_pattern(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    drum_pattern = response.choices[0].text.strip()

    midi = pretty_midi.PrettyMIDI()
    drum = pretty_midi.Instrument(program=0, is_drum=True)

    # Parse drum pattern text into MIDI notes (this is a simplified example)
    for i, char in enumerate(drum_pattern):
        if char == 'X':
            note = pretty_midi.Note(velocity=100, pitch=35, start=i*0.5, end=(i+1)*0.5)
            drum.notes.append(note)

    midi.instruments.append(drum)
    return midi

@app.route('/generate-drum-pattern', methods=['POST'])
def generate_drum_pattern():
    data = request.json
    prompt = data.get('prompt')

    midi = generate_midi_drum_pattern(prompt)
    midi_filename = 'drum_pattern.mid'
    midi.write(midi_filename)

    # Upload to S3
    s3_client.upload_file(midi_filename, S3_BUCKET_NAME, midi_filename)
    midi_url = f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{midi_filename}'
    
    return jsonify({'message': 'Drum pattern generated successfully!', 'midi_url': midi_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
