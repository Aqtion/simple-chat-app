import message
import client


class Chatroom:
    def __init__(self, name: str, uuid: str, messages: list):
        self.name = name
        self.uuid = uuid
        self.messages = messages

        self.clients = []

    def set_name(self, name: str):
        self.name = name

    def add_client(self, client: client):
        self.clients.append(client)

    def delete_client(self, client: client):
        if client in self.clients:
            self.clients.removes(client)

    def send(self, message: message):
        usernames = [user.username for user in self.clients]

        if (message.chatroom_id == self.uuid) and (message.sender in usernames):
            self.messages.append(message)
