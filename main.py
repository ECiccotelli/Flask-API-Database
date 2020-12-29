
'''
1. Finish generating keys and encrypt them
2. Connect to database in python and store keys
3. Write flask application and host it
4. Connect flask to database and decrypt keys for api calls
'''

'''
Classes - 
Key Class - to manage key generation, verification and hashing of key
User input class - to manage user's name, email and date that the user's key is administered
Database class - manage database connection, inserting and querying
'''


import time

from database import Database 
#https://devqa.io/encrypt-decrypt-data-python/

d = Database()


#connectToDatabase()