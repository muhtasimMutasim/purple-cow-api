
"""

    This is the main file that is being sent requests.
        
"""

'''
1. Web application API that is served on port 3000 
2. The API includes one endpoint `/item` that allows a client to retrieve the current items, set the items, and delete the items 
3. The “Item” object should have two properties: id and name 

4. Items should be persisted in memory while the application is running 
5. Includes a Dockerfile that will run and serve the web application 

6. Runs locally with a single startup command 

7. Includes a solution.md that provides relevant documentation including system requirements and how to build/run the solution 

'''



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
    
    # Coment if you dont care if the API is up and running
    existence = "FAST API is up and running"
    
    # Uncomment to see if db exists in the db folder
    # existence = path.exists("../db/dbfile.json")
    
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



#  File Based database
# tdb = TinyDB('../../db/db.json')

# In memory database
tdb = TinyDB(storage=MemoryStorage)
query = Query()


# Function to Insert a new item
def insert_new_item( name, category, description):
    '''
        Inserted data will have different categories
        1) Website
        2) Person Of Interest
        3) Organization
        4) Location
    '''
    # Unique ID being 
    uid = datetime.now().strftime('%m%d-%Y-%H-%M%S')

    # Creates Dictionary with relevant data
    item = { "id": uid, "name": name, "category": category, "description": description }
    
    # Inserts item into file
    tdb.insert( item )


# Function to Get the Item by ID or name
def get_item( choice, identifier ):
    '''
        Function is to get an item that exists by choice ( id or name ) and identifier 
    '''
    # Unique ID being 
    
    if choice == "id":
        
        return tdb.search( query.id == identifier )
    
    elif choice == "name":
        
        return tdb.search( query.name == identifier )
    
# Update Existing Item with updated data in dictionary format
def update_item( choice, identifier, updated_data ):
    
    target = get_item( choice, identifier )
            
    if len(target) == 0:
        print( f"Item {identifier} Does not exist\n" )
        return False
    
    uid = target[0]['id']
    print( f"\nTarget item Unique ID: {uid} that will be updated with \n{updated_data}\n" )
    
    item = tdb.get(query.id == uid )
    db_id = item.doc_id
    
    print( f"Target item database ID: {db_id} that will be updated\n\n" )
    
    tdb.update( updated_data, doc_ids=[ db_id ] )  
    


# Delete Existing Item
def delete_item( choice, identifier ):
    
    target = get_item( choice, identifier )
            
    if len(target) == 0:
        print( f"Item {identifier} Does not exist\n" )
        return False
    
    uid = target[0]['id']
    print( f"Target item {uid} that will be deleted\n" )
    
    item = tdb.get(query.id == uid )
    db_id = item.doc_id
    
    print( f"Target item db ID {db_id} that will be deleted\n" )
    
    tdb.remove( doc_ids=[ db_id ] )
    


# Function to show all items with associated data
def show_all():

    return tdb.all()




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



