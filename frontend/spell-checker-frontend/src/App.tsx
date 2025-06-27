import { useState } from 'react';
import './App.css';

interface SpellcheckResponse {
  misspelled: { word: string; suggestions: string[] }[];
}

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState<SpellcheckResponse | null>(null);

  const handleCheck = async () => {
    const res = await fetch('http://127.0.0.1:8000/spellcheck', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h2>📝 Spell Checker</h2>
      <textarea
        style={{ width: '100%', height: '120px', fontSize: '1rem' }}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type something here..."
      />
      <button
        onClick={handleCheck}
        style={{
          marginTop: '1rem',
          padding: '0.5rem 1rem',
          fontSize: '1rem',
          cursor: 'pointer',
        }}
      >
        Check Spelling
      </button>

      {result && (
        <div style={{ marginTop: '2rem' }}>
          <h3>🔍 Misspelled Words:</h3>
          {result.misspelled.length === 0 ? (
            <p>No spelling errors found ✅</p>
          ) : (
            <ul>
              {result.misspelled.map((item, i) => (
                <li key={i}>
                  <strong>{item.word}</strong> → Suggestions: {item.suggestions.join(', ') || 'None'}
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
