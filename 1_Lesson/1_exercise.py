

class Title:
    def __init__(self, title):
        self.row_title = title

    def __str__(self):
        return f"-= {str(self.row_title).upper()} =-"


title = Title("Programming in Python 3")
print(title)
