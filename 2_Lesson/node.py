class Node:
    def __init__(self, subject) -> None:
        self.subject = subject

        self.nextYes = None
        self.nextNo = None

    def __str__(self) -> str:
        return f"--------------------------\n" +\
               f"{self.subject}\n\n" +\
               f"yes -> {self.nextYes}\n" +\
               f"no -> {self.nextNo}\n" +\
               f"--------------------------\n"
