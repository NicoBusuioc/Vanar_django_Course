from datetime import datetime
from typing import Any


class Message:

    # repository
    all = []

    # entity/instance
    def __init__(self, body, author, target):
        self.__body = body
        self.author = author
        self.target = target
        self.created = datetime.now()
        self.viewed = None  # automate

    def __str__(self):
        created_time = self.created.strftime("%m-%d-%Y, %H:%M:%S")
        if self.viewed is not None:
            viewed_time = self.viewed.strftime("%m-%d-%Y, %H:%M:%S")
        else:
            viewed_time = 'not seen'
        return f"\n\t\tcreated: <{created_time}>  \n\t\tviewed:  <{viewed_time}>\n\t\"{self.__body}\"\n"

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, attr):
        if attr == 'body':
            if self.viewed is None:
                self.viewed = datetime.now()
            return self.__body

    # domain
    # static method that sends a message
    def send(body, author, target):
        # 1. create a new message object
        message = Message(body)
        # 2. remember the message in the storage
        Message.all.append(message)

        return body
