import time

#Class UserInput manage user's name, email and date that the user's key is administered
class UserInput:
    def __init__(self):
        self.name = "Default"
        self.email = "default@gmail.com"
        self.date = time.strftime('%Y-%m-%d %H:%M:%S')


    def setName(self):
        self.name = input("Enter name of user: ")
        while self.name == "" or len(self.name) > 20:
            self.name = input("Incorrect input, try again: ")
    
    def setEmail(self):
        self.email = input("Enter email of user: ")
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def getDate(self):
        return self.date