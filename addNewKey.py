
from key import Key
from database import Database
from userIn import UserInput
from random import randint
#Script to use all the classes/functions and add a new API key to the database

print("Beginning process to add new key to the database")

'''User input'''
userIn = UserInput()
name = userIn.getName()
date = userIn.getDate()
email = userIn.getEmail()


'''Generating Key'''
k = Key()

unhashed = k.generateKey()
hashedKey = k.hashKey(unhashed) #Hashing key
print(len(hashedKey))

'''Database'''
#Reads values from file and initializes object
d = Database() 

#Connecting to database
conn, cursor = d.connectToDatabase() 


#Generating random ID with given n digits
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
  # randint is inclusive at both ends

ID = str(random_with_N_digits(6))


#Inserting data into database directly
d.insertData(cursor, conn, hashedKey, name, date, email, ID)


f = open(ID + ".txt", "w")
f.write("Hashed key: " + str(hashedKey))
f.close()
print("Stored key in file: " + str(ID) + ".txt")

#Need to save these for the user to use when calling the API
print("ID is: " + str(ID))
print("Unhashed API key is: " + str(unhashed))