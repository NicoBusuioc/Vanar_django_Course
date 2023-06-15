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
        post.comments.append(comment)
        return comment

    # HW 7
    def removePost(self, post):
        for item in self.posts:
            if item is post:
                self.posts.remove(item)
                print(f"Post with id: {post.id} successfully deleted!")
                break

            # last element?
            if item is self.posts[-1]:
                raise KeyError(
                    f"User {self.username} has no post with post_id: {post.id}")

    def removeComment(self, comment):
        for item in self.comments:
            if item is comment:
                self.comments.remove(item)
                print(
                    f"Comment with id: {comment.id} successfully deleted from user list")
                # remove comment from the post list
                item.post.removeComment(item)
                break

            # last element?
            if item is self.posts[-1]:
                raise KeyError(
                    f"User {self.username} has no comment with comment_id: {comment.id}")
