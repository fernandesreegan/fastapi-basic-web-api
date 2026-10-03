from fastapi import FastAPI

app = FastAPI(
    title="My First FastAPI App",
    description="A simple beginner FastAPI application",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI application"
    }


@app.get("/greet/{name}")
def greet_user(name: str):
    return {
        "message": f"Hello, {name}!",
        "name": name
    }