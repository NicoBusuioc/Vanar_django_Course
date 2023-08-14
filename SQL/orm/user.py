import psycopg2
from .model import Model

## using static and dynamic functions
class User(Model):

    def __init__(self, id, username, email, password) -> None:
        super().__init__(id)
        self.username   = username
        self.email      = email
        self.password   = password

    def __str__(self) -> str:
        return f"id: {self.id} username: {self.username} email: {self.email} aaand pw: {self.password}"
    
    # CRUD
    def create(id, username, email, password):
        user = User(id, username, email, password)
        user.save()

    def all():
        users = []
        _, cursor = User.connect()
        cursor.execute("SELECT * FROM users;")
        users_data = cursor.fetchall()
        for item in users_data:
            user = User(item[0], item[1], item[2], item[3])
            users.append(user)
        return users
    
    def get(id):
        _, cursor = User.connect()
        cursor.execute(f"SELECT * FROM users WHERE id = {id};")
        user_data = cursor.fetchone()
        user = User(user_data[0], user_data[1], user_data[2], user_data[3])
        return user

    def update(self):
        conn, cursor = User.connect()
        cursor.execute(f"UPDATE users SET username='{self.username}', email='{self.email}', password='{self.password}'\
                       WHERE id={self.id};")
        conn.commit()

    def save(self):
        conn, cursor = User.connect()
        cursor.execute(f"INSERT INTO users VALUES({self.id}, '{self.username}', '{self.email}', '{self.password}');")
        conn.commit()
    
    def delete(self):
        User.deleteById(self.id)

    def deleteById(id):
        conn, cursor = User.connect()
        cursor.execute(f"DELETE FROM users WHERE id = {id};")
        conn.commit()

    # BEHAVIOUR
    def resetPassword(self, newPassword):
        self.password = newPassword
        self.update()

    def signin(username, password):
        _, cursor = User.connect()
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';")
        user_data = cursor.fetchone()
        if user_data:
            user = User(user_data[0], user_data[1], user_data[2], user_data[3])
        else:
            raise ValueError("ERROR: Failed login attempt!")
        return user