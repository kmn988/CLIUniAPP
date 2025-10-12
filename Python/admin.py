import hashlib

class Admin:

    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD_HASH = hashlib.sha256("Admin123".encode()).hexdigest()
    
    def __init__(self, username="admin"):
        self.username = username
    
    @classmethod
    def authenticate(cls, username, password):

        if username != cls.DEFAULT_USERNAME:
            return False, "Invalid admin username"
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if password_hash != cls.DEFAULT_PASSWORD_HASH:
            return False, "Invalid admin password"
        
        return True, cls(username)
    
    def __str__(self):
        return f"Admin: {self.username}"