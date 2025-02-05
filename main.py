from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union
from pydantic import BaseModel
import requests

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response Models
class NumberClassificationResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: List[str]
    digit_sum: int
    fun_fact: str

class ErrorResponse(BaseModel):
    number: str
    error: bool

# Utility Functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

def get_fun_fact(number: int) -> str:
    response = requests.get(f"http://numbersapi.com/{number}/math?json")
    if response.status_code == 200:
        return response.json().get("text", "No fun fact available.")
    return "No fun fact available."

# API Endpoint with Typed Response
@app.get("/api/classify-number", response_model=NumberClassificationResponse, responses={400: {"model": ErrorResponse}})
async def classify_number(number: Union[int, str] = Query(..., description="Provide an integer to classify.")):
    try:
        number = int(number)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(number=str(number), error=True).dict()
        )

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    response = NumberClassificationResponse(
        number=number,
        is_prime=is_prime(number),
        is_perfect=is_perfect(number),
        properties=properties,
        digit_sum=sum(int(d) for d in str(abs(number))),
        fun_fact=get_fun_fact(number)
    )
    return response
