"""
    File is for testing API functionality.

"""

#!/usr/bin/env python

"""
This script was created to test the REST API.

This script also allows text to be translated with
functionality that aut detects the language being
pushed through the

"""

import requests
import pathlib
import re
import sys

# Path of current directory script is located in
script_dir = pathlib.Path(__file__).parent.absolute()



def send( url ):

    print( f"\n\nTarget Url + Endpoint:\n{url}\n\n" )

    r = requests.post( url )
    json_data = r.json()
    resp_text = r.text

    return json_data


def send_get( url ):

    print( f"\n\nTarget Url + Endpoint:\n{url}\n\n" )

    r = requests.get( url )
    json_data = r.json()
    resp_text = r.text

    return json_data




 
def api_test_values():
    """
        Test for showing existing items in DB
    """
    ip = sys.argv[1]
    port = sys.argv[2]

    url = f"http://{ip}:{port}/item"
    
    resp = send_get( f"http://{ip}:{port}/item" )
    
    for value in resp['data']:
        print(value)

    # print( f"\n\nRESPONSE FROM API:\n{resp}\n\n" )
    



def test_get_item():
    """
        test for getting proper value
    """
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/item/get"
    
    choice = "id"
    id = "0317-2021-00-5205-578-135"

    url = f"{url}/{choice}/{id}"

    resp = send( url )

    print( f"\n\GET item RESPONSE FROM API:\n{resp}\n\n" )



def test_delete():
    
    """
        Test for deleting value
    """
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/item/delete"
    
    choice = "id"
    id = "0317-2021-00-5205-517-058"

    url = f"{url}/{choice}/{id}"

    resp = send( url )

    print( f"\n\nDELETE RESPONSE FROM API:\n{resp}\n\n" )


def test_update():
    
    """
        Test For Update
    """
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/item/update"
    
    choice = "id"
    id = "0317-2021-00-5205-948-924"
    updated_data = {"name": "Updated", "description": "This is testing the update functionality, and it worked"}

    url = f"{url}/{choice}/{id}/{updated_data}"
    print( f"\n\nTarget Url + Endpoint:\n{url}\n\n" )
    
    r = requests.post( url )
    resp = r.json()

    print( f"\n\nUPDATE RESPONSE FROM API:\n{resp}\n\n" )



    
def insert_test_values():
    """
        Test for insert test values into database.
    """
    ip = sys.argv[1]
    port = sys.argv[2]

    resp = send_get( f"http://{ip}:{port}/insert-test-data" )
    
    print( f"\n\nRESPONSE FROM API:\n{resp}\n\n" )
    



def api_test_all_values():
    """
        test for showing all values
    """
    ip = sys.argv[1]
    port = sys.argv[2]

    url = f"http://{ip}:{port}/item"
    
    # resp = send_get( f"http://{ip}:{port}/db_exists" )
    # resp = send_get( f"http://{ip}:{port}/test" )
    # resp = send_get( f"http://{ip}:{port}/insert-test-data" )
    # resp = send_get( f"http://{ip}:{port}/db_exists" )
    resp = send_get( f"http://{ip}:{port}/item" )
    
    # resp = send( url )

    print( f"\n\nGET ALL VALUES\nRESPONSE FROM API:\n{resp}\n\n" )
    




def main():

    print( "Starting test" )
    # insert_test_values()
    # api_test_all_values()
    api_test_values()

    # test_get_item()
    # test_delete()
    # test_update()
    
    # for i in show_all():
    #     print(i)
    
    

if __name__ == "__main__":
	main()