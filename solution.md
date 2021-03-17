# purple-cow-api


# Purple Cow API

    The purpose of this project is to create a REST api using FastAPI that has the ability to 
    
    to create a database using a python library called tinyDB which provides an option to create an in memory database

    or a database based on a JSON file. This API can serve the needs of Baltimore by providing people with impactful resources

    such as Non-Profit organizations, Law firms taking pro-bono cases, or any other helpful resource
    
    
    -------------------------------------------------------------------------------------------

    This project was deployed on Google Cloud Platform. It incorporates technology such as:
            - docker-machine (if using OSx)
            - docker
            - docker-compose
            - python's FastAPI  https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjRzKDw27bvAhXRK80KHRh7Ci0QFjAAegQIBBAE&url=https%3A%2F%2Ffastapi.tiangolo.com%2F&usg=AOvVaw2QqRQY4CTrMVY9Db4rEONB
            - TinyDB  https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiKl4Hj27bvAhWNKs0KHT7lB0sQFjAAegQIBRAE&url=https%3A%2F%2Ftinydb.readthedocs.io%2F&usg=AOvVaw1YrfnS-U_1nwU7TcmaZK7g


# Run using docker-compose locally on computer.

        # Make sure you have Docker and docker-compose installed and docker-machine if you have OSX
        # Afterwards Just Run this command in the same directory as the solution.md File.
        run "docker-compose up --build"

        # After the command is ran, the proper python libraries will be installed
        # And a sever will be spun up.



# Run on Container on Mac

        # This command is for creating a new docker-machine if on OSX
        docker-machine create --driver virtualbox {insert machine name}
        Ex: docker-machine create --driver virtualbox test

        # Starts desired machine 
        docker-machine start  {insert machine name}  
        Ex: docker-machine start test  

        # Creates Docker container
        docker-compose up --build





# Endpoints

     /test
        - Simple test endpoint that checks to see that the API is alive.

     /db_exists
        - Test that checks if the DB exists, if you plan on using the File based DB.
     
     /insert-test-data
        - This endpoint preloads hardcoded test data to make sure the functionalities are working properly.
     
     /item
        - Returns a list of existing entries within the database.
     
     
     # The "test" directory includes a python file that has exxamples of these endpoints being used.s
     
     /item/update/
        - Endpoint allows you to update the existing entries within the database.
     
     /item/delete/
        - Endpoint allows you to delete existing entry.
     
     /item/get
        - Endpoint allows you to retireve a single item within the database.
     
     /item/insert
        - Endpoint allows you to insert a single item within the database.
    
     
   # test

        In the test directory there is a python script called "test.py" that has functions that and test cases to check if everything on the REST api is 
        working and returning properly.
        
        Some of the tests are commented out so they aren't overused. 


        usage example:

            cd tests
            python test.py {Ip address} {Port Number}
            python test.py 0.0.0.0 5050

         usage of custom_mesaage():

            python test.py {Ip address} {Port Number}
            python test.py 0.0.0.0 5050 
