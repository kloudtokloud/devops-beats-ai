import React, { useState } from 'react';
import * as Tone from 'tone';

function App() {
    const [input, setInput] = useState('');
    const [midiUrl, setMidiUrl] = useState('');

    const generateDrumPattern = async () => {
        const response = await fetch('http://localhost:5000/generate-drum-pattern', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: input }),
        });

        const data = await response.json();
        setMidiUrl(data.midi_url);
    };

    const playMidi = async (url) => {
        const response = await fetch(url);
        const arrayBuffer = await response.arrayBuffer();
        const midi = new Tone.Midi(arrayBuffer);
        
        const synth = new Tone.PolySynth(Tone.Synth).toDestination();
        midi.tracks.forEach(track => {
            track.notes.forEach(note => {
                synth.triggerAttackRelease(note.name, note.duration, note.time);
            });
        });
    };

    return (
        <div>
            <h1>AI Drum Pattern Generator</h1>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={generateDrumPattern}>Generate</button>
            {midiUrl && (
                <div>
                    <p>Drum pattern generated successfully! <a href={midiUrl} target="_blank" rel="noopener noreferrer">Download MIDI</a></p>
                    <button onClick={() => playMidi(midiUrl)}>Play</button>
                </div>
            )}
        </div>
    );
}

export default App;
