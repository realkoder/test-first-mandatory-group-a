# Test - 1. Mandatory - Personal Test Data Generator

## Tech-stack

- **Frontend** - _Arturo's Fake Data Generator Frontend_
    - _HTML_
    - _JS_
    - _CSS_
- **Backend**
    - _Python_ Server
        - _Poetry_ as package manager
        - _FastAPI_ as web framework
        - _Pytest_ as test tool

---

<br>

## Dev Exp

### Run with _docker-compose_

Ensure to be positioned at `./`

```bash
docker.compose -f docker-compose.dev.yml up
```

Now you have _Python server_ running on `PORT: 8000` and
frontend on `PORT: 3000` served with _Python’s built-in HTTP server_.

---

### Run locally

To run locally Python server ensure to have installed _poetry_

Ensure to be positioned at `./server`

```
poetry shell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

### Testing with Pytest

```bash
poetry run pytest -v
```

---

<br>

## Configuring the project

Python with Poetry as project management tool and FastAPI as web framework

```bash
poetry init --name fastapi-backend -n
poetry add fastapi uvicorn
```

Adding _Pytest_ to Python server:

```bash
poetry add --dev pytest pytest-asyncio httpx
```

Added this to `pyproject.toml` to define python root path and path for test files

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```