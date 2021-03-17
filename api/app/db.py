import sys
import os
# from fastapi import FastAPI, APIRouter, Request

from tinydb import TinyDB, Query, JSONStorage, Storage
from tinydb.storages import MemoryStorage
from datetime import datetime



import os.path
from os import path

#  File Based database
# tdb = TinyDB('../../db/db.json')

# In memory database
tdb = TinyDB(storage=MemoryStorage)
query = Query()

'''
2. The API includes one endpoint `/item` that allows a client to retrieve the current items, set the items, and delete the items 
3. The “Item” object should have two properties: id and name 
4. Items should be persisted in memory while the application is running
5. Includes a Dockerfile that will run and serve the web application 
6. Runs locally with a single startup command 
7. Includes a solution.md that provides relevant documentation including system requirements and how to build/run the solution 
'''

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



# Function to update the Items Name, Category or Description
def get_item_test():

    choice1 = "name"
    choice2 = "id"
    
    # 0316-2021-17-2007
    id = '0316-2021-22-1010'
    name = "Legal Assistance, LLC"
    
    id = "0316-2021-22-1032"

    a = get_item( choice1, name )
    b = get_item( choice2, id )
    print( f"\n\n{a}\n{b}\n\n" )



# Insert Data Test
def insert_test_data():

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


def test_delete():
    
    c1 = "id"
    id = "0316-2021-22-1244"
    delete_item( c1, id )
      
    


def test_update():
    
    c1 = "id"
    id = "0317-2021-00-5205-948-924"
    updated_data = {'name': 'Updated', 'description': 'This is testing the update functionality, and it worked'}
    
    # update_item( choice, identifier, updated_data )
    update_item( c1, id, updated_data )




def main():

    print( "Starting test" )
    insert_test_data()
    # tdb.insert( {'id': '0316-2021-22-1244', 'name': 'deleting', 'category': 'Test', 'description': 'This is to test deleting'} )
    # tdb.insert( {'id': '0316-2021-22-1252', 'name': 'Updating', 'category': 'Test', 'description': 'This is to test Updating'} )
    # get_item_test()
    
    # test_delete()
    test_update()
    
    # for i in show_all():
    #     print(i)
    
    
    



if __name__ == "__main__":
    main()