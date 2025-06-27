from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.trie import WordTrie
from backend.utils import get_suggestions

import re

app = FastAPI()

word_trie = WordTrie()
word_trie.load_words("backend/data/english_words.txt")

with open("backend/data/20k_common_words.txt") as f:
    word_list = [line.strip().lower() for line in f if line.strip()]


# Allow React frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/spellcheck")
async def spellcheck(request: Request):
    data = await request.json()
    text = data.get("text", "")
    
    # Extract words (ignore punctuation, case-insensitive)
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    misspelled = []
    for word in words:
        if not word_trie.search(word):
            suggestions = get_suggestions(word, word_list)
            misspelled.append({"word": word, "suggestions": suggestions})

    return {"misspelled": misspelled}


