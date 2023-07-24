from message import Message
from client import Client


class Chatroom:
    def __init__(self, name: str, uuid: str, messages: list):
        """
        Arguments:
            name(str): name of the chatroom
            uuid(str): unique id of the chatroom
            messages(list): list of message"""

        self.name = name
        self.uuid = uuid
        self.messages = messages

        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def delete_client(self, client: Client):
        if client in self.clients:
            self.clients.removes(client)

    def send(self, message: Message):
        usernames = [user.username for user in self.clients]

        if (message.chatroom_id == self.uuid) and (message.sender in usernames):
            self.messages.append(message)
