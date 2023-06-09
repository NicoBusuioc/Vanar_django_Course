from .Post import Post
from .Comment import Comment


class User:

    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

        # relationship with posts
        self.posts = []
        self.comments = []

    def __str__(self):
        return f"USER({self.id})\n{self.username}\n{self.email}\n"

    # BEHAVIOR
    def addPost(self, post_id, post_title, post_body):
        post = Post(post_id, post_body, post_title, self)
        self.posts.append(post)
        return post

    # HW 3
    def addComment(self, comm_id, comm_body, post):
        comment = Comment(comm_id, comm_body, self, post)
        self.comments.append(comment)
        return comment
