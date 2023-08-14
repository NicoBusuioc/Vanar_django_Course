import psycopg2
from .model import Model

## using static and dynamic functions
class Comment(Model):

    def __init__(self, id, body) -> None:
        super().__init__(id)
        self.body = body

    def __str__(self) -> str:
        return f"id: {self.id} title: {self.title} body: {self.body}"
    
    # CRUD
    def create(id, title, body):
        user = Comment(id, title, body)
        user.save()

    def all():
        comments = []
        _, cursor = Comment.connect()
        cursor.execute("SELECT * FROM comments;")
        comments_data = cursor.fetchall()
        for item in comments_data:
            comment = Comment(item[0], item[1], item[2], item[3])
            comments.append(comment)
        return comments
    
    def get(id):
        _, cursor = Comment.connect()
        cursor.execute(f"SELECT * FROM comments WHERE id = {id};")
        comment_data = cursor.fetchone()
        comment = Comment(comment_data[0], comment_data[1], comment_data[2], comment_data[3])
        return comment

    def update(self):
        conn, cursor = Comment.connect()
        cursor.execute(f"UPDATE comments SET body='{self.body}'\
                       WHERE id={self.id};")                                                       #TODO: add author_id and post_id
        conn.commit()

    def save(self):
        conn, cursor = Comment.connect()
        cursor.execute(f"INSERT INTO comments VALUES({self.id}, '{self.body}', '1', '1');") #TODO: author_id  and post_id is hardcoded
        conn.commit()
    
    def delete(self):
        Comment.deleteById(self.id)

    def deleteById(id):
        conn, cursor = Comment.connect()
        cursor.execute(f"DELETE FROM comments WHERE id = {id};")
        conn.commit()

    # BEHAVIOUR
