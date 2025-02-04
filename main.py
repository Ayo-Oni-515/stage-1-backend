from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from math_properties import is_prime, is_perfect, properties, digit_sum, fun_fact

#FastAPI instace creation
app = FastAPI()

# CORS Management
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["GET"],  
    allow_headers=["*"]
)

@app.get('/api/classify-number')
async def index(number):
    try:
        number = int(number)
    except:
        #API 400 Response
        return JSONResponse({"number": "alphabet", "error": True}, status_code=400)

    #API 200 Response
    return JSONResponse({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties(number),
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact(number)
    }, status_code=200)
