
"""

    This is the main file that is being sent requests.
        
"""



import sys
import os
from fastapi import FastAPI, APIRouter, Request
from tinydb import TinyDB, Query, JSONStorage, Storage

import os.path
from os import path

app = FastAPI()
# router = APIRouter()

# @router.get("/test")
@app.get("/test")
def test():
    
    existence = path.exists("../db/dbfile.json")
    return {"Test": existence }


# @router.get("/test")
@app.get("/db_exists")
def db_test():
    """
        This checks if the tiny db file exists
    """
    existence = path.exists("../db/dbfile.json")
    if existence != True:
        open('../db/dbfile.json', 'w+')
        
    return {"DB Existence Test": existence }


tdb = TinyDB("../db/dbfile.json")

'''
1. Web application API that is served on port 3000 

2. The API includes one endpoint `/item` that allows a client to retrieve the current items, set the items, and delete the items 

3. The “Item” object should have two properties: id and name 

4. Items should be persisted in memory while the application is running 5. Includes a Dockerfile that will run and serve the web application 

6. Runs locally with a single startup command 

7. Includes a solution.md that provides relevant documentation including system requirements and how to build/run the solution 

'''

def insert_data(db_id, name, category, description):
    '''
        Inserted data will have different categories
        1) Website
        2) Person Of Interest
        3) Organization
        4) Location
    '''
    
    tdb.insert()




# @router.get("/items")
# @app.post("/vader/{data}")
@app.post("/item/insert/{name}/{category}/{description}")
def insert( request: Request, name: str, category: str, description: str ):
    """
    Route to insert an item. route needs a name, category, and description 
    """
    
    client_host = request.client.host
    
    print( f"\n\nGetting request from: {client_host}\n\n" )
    
    message = "This will contain links with information FAST API FROM DOCKER"
        
    # return { "data": vader_result }
    return { "data": message }




# @router.get("/items")
# @app.post("/vader/{data}")
@app.get("/item/show/{choice}")
def query(request: Request):
    """
    Route to items
    """
    # print(f"\n\nRESPONSE: {data}\n\n")
    # return {"client_host": client_host, "response": a}
    client_host = request.client.host
    
    print( f"\n\nGetting request from: {client_host}\n\n" )
    
    message = "This will contain links with information FAST API FROM DOCKER"
        
    # return { "data": vader_result }
    return { "data": message }



