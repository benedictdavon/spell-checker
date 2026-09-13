from pathlib import Path
import re

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.trie import WordTrie
from backend.utils import get_suggestions

ROOT = Path(__file__).resolve().parent


class SpellcheckRequest(BaseModel):
    text: str = Field(max_length=10_000)

    model_config = {"extra": "forbid"}


def create_app() -> FastAPI:
    app = FastAPI(title="Spell Checker API", version="0.1.0")
    trie = WordTrie()
    trie.load_words(str(ROOT / "data" / "english_words.txt"))
    common_words = [
        line.strip().lower()
        for line in (ROOT / "data" / "20k_common_words.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
        allow_methods=["POST", "GET"],
        allow_headers=["Content-Type"],
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/spellcheck")
    def spellcheck(payload: SpellcheckRequest) -> dict[str, list[dict[str, object]]]:
        words = re.findall(r"\b[a-zA-Z]+\b", payload.text.lower())
        misspelled = []
        for word in words:
            if not trie.search(word):
                misspelled.append({"word": word, "suggestions": get_suggestions(word, common_words)})
        return {"misspelled": misspelled}

    return app


app = create_app()
