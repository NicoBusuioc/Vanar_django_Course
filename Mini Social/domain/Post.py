class Post:

    def __init__(self, id, title, body, author):
        self.id = id
        self.title = title
        self.body = body

        # HW2 - direct relation
        self.author = author
        self.comments = []

    def __str__(self):
        return f"Post({self.id})\n{self.title}\n{self.body}\n{self.author}\n"

    def removeComment(self, comment):
        for item in self.comments:
            if item is comment:
                self.comments.remove(item)
                print(
                    f"Comment with id: {comment.id} successfully deleted from the post list!")
                break

            # last element?
            if item is self.posts[-1]:
                raise KeyError(
                    f"The comment with comment_id: {comment.id} was not found under the post with post_id: {self.id}")
