from message import Message
from client import Client


class Chatroom:
    def __init__(self, name: str, uuid: str):
        """A class for a chatroom
        @name: The name of the chatroom
        @uuid: The unique ID of the chatroom
        @messages: A list of messages previously sent in the chatroom
        """

        self.name = name
        self.uuid = uuid
        self.messages = []

        self.clients = []

    def add_client(self, client: Client):
        """Adds client to the chatroom

        :param client: A Client object to be added to the list of clients
        :return: None
        """

        self.clients.append(client)

    def delete_client(self, client: Client):
        """Removes client to the chatroom

        :param client: A Client object to be removed from the list of clients
        :return: None
        """

        if client in self.clients:
            self.clients.remove(client)

    def send(self, message: Message):
        """Sends a message to the chatroom

        :param message: A Message object to be added to the messages list
        :return: None
        """

        usernames = [user.username for user in self.clients]

        if (message.chatroom_id == self.uuid) and (message.sender in usernames):
            self.messages.append(message)
