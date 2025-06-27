from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from trie import WordTrie
import re

app = FastAPI()

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
    return {"misspelled": [], "suggestions": {}}

