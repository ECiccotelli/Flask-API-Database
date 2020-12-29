import json

import mysql.connector
class Database:

    def __init__(self):
        self.readCreds()
        print("Init")
    
    #Inserts data into database
    def insertData(self, mycursor, conn, apikey, name, dateIssued, email):
        sql = "INSERT INTO apikeystable VALUES (%s, %s, %s, %s)"
        args = apikey, name, dateIssued, email
        mycursor.execute(sql, args)
        #mycursor.execute(statement)
        conn.commit()
    
    
    def readCreds(self):
        with open('dbcreds.json') as f:
            data = json.load(f)
        
        self.username = data['user']
        self.password = data['pass']
        self.host = data['host']
        self.databaseName = data['database']
        self.port = data['port']
        print(self.databaseName)

        
    def connectToDatabase(self):
        conn = mysql.connector.connect(user=self.username, password=self.password,
                                host=self.host,
                                database=self.databaseName, port=self.port)
        mycursor = conn.cursor(buffered=True)

        if conn.is_connected():
            print("Successfully connected to database")
        else:
            print("Error connecting to database")
        
        mycursor.execute("use apikeys")
        mycursor.execute("Select * from apikeystable;")
        data = mycursor.fetchall()
        print("Data before!")
        print(data)

        insertData(mycursor, conn, hashKey(), getName(), getDate(), getEmail())

        mycursor.execute("Select * from apikeystable;")
        data = mycursor.fetchall()
        print("Data after!")
        print(data)