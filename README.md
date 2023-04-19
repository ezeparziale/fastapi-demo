# :circus_tent: Demo Fast API

API con varios endpoints utilizando FastAPI.  
Sirve de template para nuevas apis.

## :runner: Run

```bash
uvicorn app.main:app --reload
```

## :star: CRUD

### :rocket: Create

#### Creación de un post

```python
@app.post("/api/v1/posts")
```

Body:

```python
{
    "title": "CCC",  # titulo de post
    "content": "ccc",  # contenidos del post
    "published": true  # esta publicado el post? True = Si | False = No
}
```

#### Creación de un usuario

```python
@app.post("/api/v1/users")
```

Body:

```python
{
    "email": "example_email@example.com",
    "password": "my_password"
}
```

#### Login de usuario

```python
@app.post("/api/v1/login")
```

Parametros:

``` python
username: "example_email@example.com"
password: "my_password"
```

#### Votación de post

```python
@app.post("/api/v1/vote")
```

Body:

```python
{
    "post_id": 1,  # id de post
    "dir": 0  # 1 = LIKE | 0 = UNLIKE
}
```

### :eyeglasses: Read

#### Lectura de un post

```python
@app.get("/api/v1/posts/{id}")  # id = post id
```

#### Lectura de todos los post

```python
@app.get("/api/v1/posts")
```

#### Lectura de un usuario

```python
@app.get("/api/v1/users/{id}")  # id = user id
```

### :coffee: Update

#### Actualización de un post

```python
@app.put("/api/v1/posts/{id}")  # id = post id
```

### :fire: Delete

#### Borrado de un post

```python
@app.delete("/api/v1/posts/{id}")  # id = post id
```

## :globe_with_meridians: HTTP Methods

```http
https://developer.mozilla.org/es/docs/Web/HTTP/Methods
```

## :compass: HTTP Status code

```http
https://developer.mozilla.org/es/docs/Web/HTTP/Status
```

## :memo: Docs

```http
http://127.0.0.1:8000/docs
```

```http
http://127.0.0.1:8000/redoc
```

## :books: SQLAlchemy

```http
https://docs.sqlalchemy.org/en/14/
```

## :zap: FastAPI

```http
https://fastapi.tiangolo.com
```

## :satellite: psycopg

```http
https://www.psycopg.org
```

## :key: JWT

```http
https://jwt.io
```

## :alembic: Alembic

```http
https://alembic.sqlalchemy.org/en/latest/
```

Para inicializar alembic:

```bash
alembic init alembic
```

Comandos más utilizados:

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

## :test_tube: PyTest

Instalación:

```bash
pip install pytest
```

Tutorial:

```http
https://fastapi.tiangolo.com/tutorial/testing/
```

Comandos más utilizados:

```bash
pytest
pytest -v -s  ## Best
pytest --disable-warnings
pytest --disable-warnings -v
pytest --disable-warnings -v -s
pytest --disable-warnings -v -s -x
```

## :robot: Heroku

Plataforma en la nube gratis sin tarjeta de credito para devs:

```http
http://heroku.com
```

Tutoriales:

```http
https://devcenter.heroku.com/articles/getting-started-with-python
```

```http
https://devcenter.heroku.com/articles/heroku-postgresql
```

Comandos más utilizados:

```bash
heroku login
heroku create fastapi-demo
git push heroku main
heroku logs -t
heroku addons:create heroku-postgresql:hobby-dev
heroku ps restart
heroku apps:info fastapi-demo
heroku run "alembic upgrade head"
heroku ps -a fastapi-demo
```

## :package: Github Actions

```http
https://github.com/features/actions
```

```http
https://docs.github.com/es/actions/using-containerized-services/creating-postgresql-service-containers
```

## :whale: Docker

```http
https://docs.docker.com/get-started/
```

```http
https://docs.docker.com/compose/
```

```http
https://hub.docker.com
```
