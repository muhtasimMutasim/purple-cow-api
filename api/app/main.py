
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



import json
import os.path
from os import path
import sys
import os

from fastapi import FastAPI, APIRouter, Request
from tinydb import TinyDB, Query, JSONStorage, Storage
from tinydb.storages import MemoryStorage
from datetime import datetime
import random


app = FastAPI()
# router = APIRouter()



###############################################################
# Testing endpoints
###############################################################

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
    existence = path.exists("../db/db.json")
    if existence != True:
        open('../db/db.json', 'w+')
        
    return {"DB Existence Test": existence }


###############################################################



################################################################
# API logic
###############################################################
#  File Based database
# tdb = TinyDB('../../db/db.json')

# In memory database
tdb = TinyDB(storage=MemoryStorage)
query = Query()




def insert_new_item( name, category, description):
    '''
        Function to Insert a new item.
        Inserted data will have different categories
        1) Website
        2) Person Of Interest
        3) Organization
        4) Location
    '''
    # Unique ID being 
    uid = datetime.now().strftime('%m%d-%Y-%H-%M%S')
    uid = uid + "-" + '-'.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])

    # Creates Dictionary with relevant data
    item = { "id": uid, "name": name, "category": category, "description": description }
    
    # Inserts item into file
    tdb.insert( item )



def get_item( choice, identifier ):
    '''
        Function is to get an item that exists by choice ( id or name ) and identifier. 
    '''
    # Unique ID being 
    
    if choice == "id":
        
        return tdb.search( query.id == identifier )
    
    elif choice == "name":
        
        return tdb.search( query.name == identifier )
    


def update_item( choice, identifier, updated_data ):
    
    '''
         Update Existing Item with updated data in dictionary format.
    '''
    target = get_item( choice, identifier )
    
    # Checks if item requested exists  
    if len(target) == 0:
        print( f"Item {identifier} Does not exist\n" )
        return False
    
    
    updated_data = updated_data.replace("'", '"', 30)
    # Uses timestamp id to get doc_id. 
    uid = target[0]['id']
    print( f"\nTarget item Unique ID: {uid} that will be updated with " )
    print(updated_data)
    print("\n\n")
    
    updated_data = json.loads(updated_data)
    # d_t = type( updated_data )
    # print( f"\nUpdated data type \n{ d_t }\n" )
    
    # Uses Database Index to update item
    item = tdb.get(query.id == uid )
    db_id = item.doc_id
    
    print( f"Target item database ID: {db_id} that will be updated\n\n" )
    
    # Item Updated
    tdb.update( updated_data, doc_ids=[db_id] )
    
    print( "Item Successfully Updated" )
    
    # Returns Updated Item
    # return get_item( "id", uid )  
    return True  
    



def delete_item( choice, identifier ):
    
    '''
            Function for deleting Existing Item
    '''
    target = get_item( choice, identifier )
    
    # Checks if item requested exists  
    if len(target) == 0:
        print( f"Item {identifier} Does not exist\n" )
        return False
    
    # Uses timestamp id to get doc_id. 
    uid = target[0]['id']
    print( f"Target item {uid} that will be deleted\n" )
    
    # Uses Database Index to delete item
    item = tdb.get(query.id == uid )
    db_id = item.doc_id
    
    print( f"Target item db ID {db_id} that will be deleted\n" )
    
    tdb.remove( doc_ids=[ db_id ] )
    return True
    


def show_all():
    """
        Shows All existing entries, If any exist
    """
    return tdb.all()


###############################################################
##   All of the API endpoints
############################################################### 



@app.post("/item/insert/{name}/{category}/{description}")
def insert( request: Request, name: str, category: str, description: str ):
    """
    Route to insert an item. route needs a name, category, and description 
    """
    
    client_host = request.client.host
    
    print( f"\n\nGetting request from: {client_host}\n\n" )
    
    insert_new_item( name, category, description)
    message = "Data Has Succesfully been stored"
        
    return { "data": message }




@app.post("/item/update/{choice}/{identifier}/{updated_data}")
def update( request: Request, choice: str, identifier: str, updated_data: str ):
    """
    Route to update an item. 
    Route needs choice of identifier ( like id or name).
    Route needs Updated Data in JSON form.
    """
    
    client_host = request.client.host
    print( f"\n\nUpdate ENDPOINT\nGetting request from: {client_host}\n\n" )
    print( f"RESPONSE: {choice}\n{identifier}\n{updated_data}\n\n" )
    # print( f"Request JSON:\n{request.json()}\n\n" )
    
    # updated_data = json.loads(updated_data)
    
    message = update_item( choice, identifier, updated_data )
    
    print( f"\n\nMesage: {message}\n\n" )
    
    
    return { "data": message }





@app.post("/item/delete/{choice}/{identifier}")
def delete( request: Request, choice: str, identifier: str ):
    """
    Route to delete an item. 
    Route needs choice of identifier ( like id or name) and identifier.

    """
    
    client_host = request.client.host
    print( f"\n\Delete ENDPOINT\nGetting request from: {client_host}\n\n" )
    
    message = delete_item( choice, identifier )
    
    return { "data": message }




@app.post("/item/get/{choice}/{identifier}")
def get_item_( request: Request, choice: str, identifier: str ):
    """
    Route to delete an item. 
    Route needs choice of identifier ( like id or name) and identifier.

    """
    
    client_host = request.client.host
    print( f"\n\Get Item ENDPOINT\nGetting request from: {client_host}\n\n" )
    
    message = get_item( choice, identifier )
    print( f"\n\nIten Gotten:\n{message}\n\n" )
    
    return { "data": message }



@app.get("/item")
def all_items(request: Request):
    """
    Route to show existing items.
    """
    # print(f"\n\nRESPONSE: {data}\n\n")
    # return {"client_host": client_host, "response": a}
    client_host = request.client.host
    
    print( f"\n\nitem ENDPOINT for Show ALL\nGetting request from: {client_host}\n\n" )
    
    message = show_all()
    
    if len(message) == 0:
        
        return {"data": "Database is currently empyt. send request to /insert-test-data endpoint for test data"}
        
    # return { "data": vader_result }
    return { "data": show_all() }



@app.get("/insert-test-data")
def insert_test_data():
    
    """
        This End Point is to insert test data
    """

    print( "Inside Test Data Function" )
    
    #0316-2021-17-1016 & 0316-2021-17-2007
    item1 = [ "Legal Assistance, LLC", "Organization", "This law firm offered to take pro bono cases in balitmore."]
    #0316-2021-17-2905
    item2 = ["Bail Bonds", "Organization", "Bail bond help."]
    #0316-2021-17-2014
    item3 = [ "FreeFood.com", "Website", "Website for free food in balitmore."]
    #0316-2021-17-2021
    item4 = [ "mdot", "Organization", "Maryland department of transportation."]
    # item5 = [ "deleting", "Test", "This is to test deleting"]
    # item6 = [ "Updating", "Test", "This is to test Updating"]
    # item7 = [ "CHECK-Existence", "Test", "Check to see what db returns when a value does not exist"]
    tdb.insert( {'id': '0317-2021-00-5205-517-058', 'name': 'deleting', 'category': 'Test', 'description': 'This is to test deleting'} )
    tdb.insert( {'id': '0317-2021-00-5205-948-924', 'name': 'Updating', 'category': 'Test', 'description': 'This is to test Updating'})
    tdb.insert({'id': '0317-2021-00-5205-578-135', 'name': 'CHECK-Existence', 'category': 'Test', 'description': 'Check to see what db returns when a value does not exist'})
    test_data = [ item1, item2, item3, item4 ]
    # test_data = [ item1, item2, item3, item4, item5, item6 ]
    
    for data in test_data:
        
        item = data
    
        name = item[0]
        category = item[1]
        description = item[2]
        
        # uid = get_item( "name", name)[0]['id']
        exists = get_item( "name", name)
        
        if len(exists) == 0:
            print( f"Does not exist {name}, entering data\n" )
            insert_new_item( name, category, description)
            continue
                    
        print( f"\nEXISTS: {exists} \n" )

        # insert_new_item( name, category, description)
    
    return { "message": "Test Data Exists in Database" }

