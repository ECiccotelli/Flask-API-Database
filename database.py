import json

import mysql.connector
class Database:

    def __init__(self):
        self.readCreds() #Reads information into file to connect to database

    #Reading database credentials from file
    def readCreds(self):
        with open('dbcreds.json') as f:
            data = json.load(f)
        
        self.username = data['user']
        self.password = data['pass']
        self.host = data['host']
        self.databaseName = data['database']
        self.port = data['port']

    
    #Connects to database
    def connectToDatabase(self):
        conn = mysql.connector.connect(user=self.username, password=self.password,
                                host=self.host,
                                database=self.databaseName, port=self.port)
        mycursor = conn.cursor(buffered=True)

        if conn.is_connected():
            print("Successfully connected to database")
        else:
            print("Error connecting to database")
        
        #Selects proper database and table
        mycursor.execute("use apikeys")
        self.conn = conn
        self.cursor = mycursor
        return conn, mycursor
    
    #Inserts data into database
    def insertData(self, mycursor, conn, apikey, name, dateIssued, email, ID):
        sql = "INSERT INTO apikeystable VALUES (%s, %s, %s, %s, %s)"
        args = apikey, name, dateIssued, email, ID
        mycursor.execute(sql, args)
        conn.commit()
    
    #Queries database to return information about a given ID
    def queryDB(self, ID):

        self.cursor.execute("Select * from apikeystable where ID = '" + str(ID) + "';")
        data = self.cursor.fetchall()
        return data
    
    def getConn(self):
        return self.conn
    
    def getCursor(self):
        return self.cursor