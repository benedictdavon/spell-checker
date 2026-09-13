from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_spellcheck_returns_unknown_word_and_suggestions() -> None:
    response = client.post("/spellcheck", json={"text": "This is a quik test."})
    assert response.status_code == 200
    body = response.json()
    assert body["misspelled"][0]["word"] == "quik"
    assert len(body["misspelled"][0]["suggestions"]) <= 3


def test_spellcheck_rejects_unknown_fields() -> None:
    response = client.post("/spellcheck", json={"text": "ok", "debug": True})
    assert response.status_code == 422


def test_spellcheck_rejects_oversized_text() -> None:
    response = client.post("/spellcheck", json={"text": "x" * 10001})
    assert response.status_code == 422


def test_spellcheck_is_case_and_punctuation_tolerant() -> None:
    response = client.post("/spellcheck", json={"text": "Hello, WORLD!"})
    assert response.status_code == 200
    assert response.json()["misspelled"] == []
