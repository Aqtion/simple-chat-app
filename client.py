class Client:
    def __init__(self, username, ip_address, password, uuid):
        """A class for a client
        @username: The username of the client
        @ip_address: The IP address of the client
        @password: The password of the client
        @uuid: The unique user ID of the client
        """

        self.username = username
        self.ip_address = ip_address
        self.password = password
        self.uuid = uuid
