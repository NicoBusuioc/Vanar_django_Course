class Post:

    def __init__(self, id, title, body, author):
        self.id = id
        self.title = title
        self.body = body

        # HW2 - direct relation
        self.author = author

    def __str__(self):
        return f"Post({self.id})\n{self.title}\n{self.body}\n{self.author}\n"
