
from database import Database


from flask import Flask
from flask_restful import Api, Resource, reqparse

import string
import bcrypt
import secrets

app = Flask(__name__)
api = Api(app)


putArgs = reqparse.RequestParser()
putArgs.add_argument("name" ,type=str, help="Incorrect, name is required!", required=True)

d = Database()

@app.before_first_request
def before_first_request():
    d.connectToDatabase() 

class ExampleAPI(Resource):

    def get(self, userID, apikey):
        
        #Connecting to database
        dataReturned = d.queryDB(userID)
        
        #Preparing keys to be compared
        try:
            dbHashedKey = dataReturned[0][0]
        except:
            return {"Status": "Access denied", "Message": "Could not find ID in database", "Data": None}, 401
        dbHashedKey = dbHashedKey.encode('utf-8')
        apikey = apikey.encode('utf-8')
        
        #Return statement to be accessed
        if (bcrypt.checkpw(apikey, dbHashedKey)):
            return {"Status": "Access granted", "Message": "Authorized", "Data" : "Super secret data goes here"}
        else:
            return {"Status": "Access denied", "Message": "Unauthorized", "Data": None}, 401
        

api.add_resource(ExampleAPI, "/exampleAPI/<int:userID>/<string:apikey>")

if __name__ == "__main__":
    app.run(debug=True)