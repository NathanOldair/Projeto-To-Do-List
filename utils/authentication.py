from models.user import User

class Authentication:
    users = []

    @classmethod
    def register(cls, username, password):
        user = cls.find_user(username)
        if user is None:
            new_user = User(username, password)
            cls.users.append(new_user)
            return new_user
        else:
            raise Exception("Username already exists.")

    @classmethod
    def login(cls, username, password):
        user = cls.find_user(username)
        if user and user.password == password:
            return user
        else:
            raise Exception("Invalid username or password.")

    @classmethod
    def find_user(cls, username):
        for user in cls.users:
            if user.username == username:
                return user
        return None