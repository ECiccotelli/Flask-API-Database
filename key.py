import string
import bcrypt
import secrets
class Key:

    def __init__(self):
        self.key = None
        self.hashedKey = None
    
    #Generates a random key that is 32 digits long
    def generateKey(self):
        alphabet = string.ascii_letters + string.digits
        while True:
            key = ''.join(secrets.choice(alphabet) for i in range(32))
            if (any(c.islower() for c in key)
                    and any(c.isupper() for c in key)
                    and sum(c.isdigit() for c in key) >= 3):
                break
        self.key = key
        return key

    #Takes key and hashes it into a bytes format
    def hashKey(self, key):
        k = key
        encoded = k.encode("utf-8")
        hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
        self.hashedKey = hashed
        return hashed