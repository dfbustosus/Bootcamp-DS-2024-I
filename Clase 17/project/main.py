# python -m pip install fastapi uvicorn
from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

# Include route definitions from endpoints module
app.include_router(endpoints.router)
# uvicorn main:app --reload