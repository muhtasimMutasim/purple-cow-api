
import sys
import os
# from fastapi import FastAPI, APIRouter, Request

from tinydb import TinyDB, Query, JSONStorage, Storage
from datetime import datetime



import os.path
from os import path


tdb = TinyDB('db.json')
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
    


# Function to show all items with associated data
def show_all():

    return tdb.all()


# Function to update the Items Name, Category or Description
def get_item_test():

    choice1 = "name"
    choice2 = "id"
    

    # 0316-2021-17-2007
    id = "0316-2021-17-2007"
    name = "Legal Assistance, LLC"

    get_item( choice1, name )
    get_item( choice2, id )



# Insert Data Test
def insert_test():

    #0316-2021-17-1016 & 0316-2021-17-2007
    item1 = [ "Legal Assistance, LLC", "Organization", "This law firm offered to take pro bono cases in balitmore."]
    #0316-2021-17-2905
    item2 = ["Bail Bonds", "Organization", "Bail bond help."]
    #0316-2021-17-2014
    item3 = [ "FreeFood.com", "Website", "Website for free food in balitmore."]
    #0316-2021-17-2021
    item4 = [ "mdot", "Organization", "Maryland department of transportation."]
    
    item = item2

    name = item[0]
    category = item[1]
    description = item[2]

    insert_new_item( name, category, description)


def main():

    print( "Starting test" )
    # insert_test()
    
    # for i in show_all():
    #     print(i)
    
    get_item_test()
    
    



if __name__ == "__main__":
    main()

