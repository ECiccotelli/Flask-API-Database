import string
import bcrypt
import secrets
class Key:

    def __init__(self):
        self.key = None
        self.hashedKey = None
    
    def generateKey(self):
        alphabet = string.ascii_letters + string.digits
        while True:
            key = ''.join(secrets.choice(alphabet) for i in range(32))
            if (any(c.islower() for c in key)
                    and any(c.isupper() for c in key)
                    and sum(c.isdigit() for c in key) >= 3):
                break
        self.key = key

    def hashKey(self, key):
        k = key
        encoded = k.encode("utf-8")
        hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
        self.hashedKey = hashed