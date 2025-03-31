from fastapi import FastAPI
from pydantic import BaseModel


from logger import logger

# Initialize the FastAPI app
app = FastAPI()

# Define a model for input data
class SumRequest(BaseModel):
    num1: float
    num2: float

@app.get("/")
def read_root():
    logger.info("Checkup api done")
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/sum")
def calculate_sum(request: SumRequest):
    result = request.num1 + request.num2
    return {"num1": request.num1, "num2": request.num2, "sum": result}


print("Hello World..!")

# To run this API, save it as a Python file (e.g., `main.py`), then run:
# uvicorn main:app --reload
