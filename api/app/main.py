
"""

    This is the main file that is being sent requests.
        
"""



import sys
import os
from fastapi import FastAPI, APIRouter, Request


app = FastAPI()
# router = APIRouter()


# @router.get("/test")
@app.get("/test")
def test():
    return {"Test": "Test for Purple Cow API"}




# @router.get("/items")
# @app.post("/vader/{data}")
@app.get("/items")
def query(data: str, request: Request):
    """
    Route to items
    """
    # print(f"\n\nRESPONSE: {data}\n\n")
    # return {"client_host": client_host, "response": a}
    client_host = request.client.host
    
    print( f"\n\nGetting request from: {client_host}\n\n" )
    
    message = "This will contain links with information"
        
    # return { "data": vader_result }
    return { "data": message }



