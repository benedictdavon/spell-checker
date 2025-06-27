# Spell Checker Web App #
#
A full-stack spell checker built from scratch using React (TypeScript) for the frontend and FastAPI (Python) for the backend. The application detects misspelled words in user input and provides suggested corrections using a custom dictionary. #
#
## Features ##
- Spell checking based on a real English dictionary dataset #
- FastAPI backend API for processing text #
- React + TypeScript frontend for user interaction #
- Real-time suggestions for misspelled words #
#
## Project Structure ##
```
spell-checker-app/
├── backend/               # FastAPI backend
│   ├── main.py            # API logic
│   ├── trie.py            # Word trie implementation (optional)
│   └── data/
│       └── english_words.txt  # Word list used for validation
└── frontend/
    └── spell-checker-frontend/ # React app created with Vite
```
#
## Getting Started ##
#
### Backend Setup (Conda) ##
```
cd backend
conda create -n spellchecker-backend python=3.11
conda activate spellchecker-backend
pip install fastapi uvicorn python-multipart
python -m uvicorn main:app --reload
```
#
### Frontend Setup (Vite + React) ##
```
cd frontend
npm create vite@latest spell-checker-frontend -- --template react-ts
cd spell-checker-frontend
npm install
npm run dev
```
#
## API Endpoint ##
**POST** `/spellcheck` #
- **Request Body**: `{ "text": "your input text here" }` #
- **Response**: `{ "misspelled": [{ "word": "quik", "suggestions": ["quick"] }] }` #
#
## Dictionary Source ##
Dictionary used: [https://raw.githubusercontent.com/dwyl/english-words/master/words.txt](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt) #
#
## License ##
This project is open-source and available under the MIT License. #
