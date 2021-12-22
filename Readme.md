# Demo Fast API

## Run

```bash
uvicorn app.main:app --reload
```

## CRUD

### Create

```python
@app.post("/posts")
```

### Read

```python
@app.get("/posts/{id}")
```

```python
@app.get("/posts")
```

### Update

```python
@app.put("/posts/{id}")
```

### Delete

```python
@app.delete("/posts/{id}")
```

## HTTP Methods

```http
https://developer.mozilla.org/es/docs/Web/HTTP/Methods
```

## HTTP Status code

```http
https://developer.mozilla.org/es/docs/Web/HTTP/Status
```

## Docs

```http
http://127.0.0.1:8000/docs
```

```http
http://127.0.0.1:8000/redoc
```

## SQLAlchemy

```http
https://docs.sqlalchemy.org/en/14/
```

## FastAPI

```http
https://fastapi.tiangolo.com
```

## psycopg

```http
https://www.psycopg.org
```

## JWT

```http
https://jwt.io
```

## Alembic

```http
https://alembic.sqlalchemy.org/en/latest/
```

```bash
alembic init alembic
```

```bash
alembic revision -m "add column to table xxx"
alembic current
alembic heads
alembic upgrade REVISION_ID
alembic downgrade REVISION_ID
alembic downgrade -1
alembic history
alembic upgrade head
```

## PyTest

```bash
pip install pytest
```

```http
https://fastapi.tiangolo.com/tutorial/testing/
```

Comandos más utilizados:

```bash
pytest
pytest -v -s
pytest --disable-warnings
pytest --disable-warnings -v
pytest --disable-warnings -v -s
pytest --disable-warnings -v -s -x
```
