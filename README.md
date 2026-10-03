# Basic FastAPI Web API

A simple beginner-level web API developed using Python, FastAPI, and Uvicorn.

## Features

- Root `GET /` endpoint with a JSON welcome message
- Dynamic `GET /greet/{name}` endpoint using a path parameter
- Automatic interactive API documentation using Swagger UI
- Runs locally using Uvicorn

## Run

pip install fastapi uvicorn

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs
