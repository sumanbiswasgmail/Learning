# Learning

A simple FastAPI app that greets a user by name.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000.

- `GET /` — greets the currently logged-in OS user
- `GET /greet/{name}` — greets the given name

## Test

```bash
pytest -v
```
