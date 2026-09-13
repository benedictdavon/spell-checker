import { useState } from 'react'
import type { FormEvent } from 'react'
import './App.css'

interface MisspelledWord { word: string; suggestions: string[] }
interface SpellcheckResponse { misspelled: MisspelledWord[] }

function App() {
  const [text, setText] = useState('')
  const [result, setResult] = useState<SpellcheckResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleCheck(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setError('')
    setResult(null)
    setLoading(true)
    try {
      const response = await fetch('/spellcheck', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      })
      if (!response.ok) throw new Error(`Request failed (${response.status})`)
      setResult((await response.json()) as SpellcheckResponse)
    } catch (requestError) {
      setError(requestError instanceof Error ? requestError.message : 'Unable to check spelling.')
    } finally { setLoading(false) }
  }

  return (
    <main className="app-shell">
      <section className="card" aria-labelledby="title">
        <p className="eyebrow">Small full-stack prototype</p>
        <h1 id="title">Spell checker</h1>
        <p className="intro">Check English text against a local dictionary and inspect edit-distance suggestions.</p>
        <form onSubmit={handleCheck}>
          <label htmlFor="text">Text to check</label>
          <textarea id="text" value={text} onChange={(event) => setText(event.target.value)} maxLength={10000} placeholder="Type a sentence here..." />
          <div className="form-footer">
            <span>{text.length}/10,000 characters</span>
            <button type="submit" disabled={loading || text.trim().length === 0}>{loading ? 'Checking…' : 'Check spelling'}</button>
          </div>
        </form>
        {error && <p className="error" role="alert">{error}</p>}
        {result && <section className="results" aria-live="polite">
          <h2>Results</h2>
          {result.misspelled.length === 0 ? <p>No spelling errors found.</p> : <ul>{result.misspelled.map((item, index) => <li key={`${item.word}-${index}`}><strong>{item.word}</strong><span>{item.suggestions.join(', ') || 'No suggestions'}</span></li>)}</ul>}
        </section>}
      </section>
    </main>
  )
}

export default App
