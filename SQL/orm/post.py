import psycopg2
from .model import Model
from .user import User

## using static and dynamic functions
class Post(Model):

    def __init__(self, id, title, body, author) -> None:
        super().__init__(id)
        self.title = title
        self.body = body
        self.author = author

    def __str__(self) -> str:
        return f"id: {self.id} title: {self.title} body: {self.body} author: {self.author}"
    
    # CRUD
    def create(id, title, body):
        user = Post(id, title, body)
        user.save()

    def all():
        posts = []
        _, cursor = Post.connect()
        cursor.execute("SELECT * FROM posts;")
        posts_data = cursor.fetchall()
        for item in posts_data:
            author = User.get(item[3])
            post = Post(item[0], item[1], item[2], author)
            posts.append(post)
        return posts
    
    def get(id):
        _, cursor = Post.connect()
        cursor.execute(f"SELECT * FROM posts WHERE id = {id};")
        post_data = cursor.fetchone()
        author = User.get(post_data[3])
        post = Post(post_data[0], post_data[1], post_data[2], author)
        return post

    def update(self):
        conn, cursor = Post.connect()
        cursor.execute(f"UPDATE posts SET title='{self.title}', body='{self.body}'\
                       WHERE id={self.id};")                                                       #TODO: add author_id
        conn.commit()

    def save(self):
        conn, cursor = Post.connect()
        cursor.execute(f"INSERT INTO posts VALUES({self.id}, '{self.title}', '{self.body}', '{self.author}');") #TODO: author_id is hardcoded
        conn.commit()
    
    def delete(self):
        Post.deleteById(self.id)

    def deleteById(id):
        conn, cursor = Post.connect()
        cursor.execute(f"DELETE FROM posts WHERE id = {id};")
        conn.commit()

    # BEHAVIOUR
