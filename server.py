from subprocess import check_output

"""
The Server class holds the attributes of the Server object: ip_address and port
"""


class Server:
    ip_address = (
        check_output(["hostname", "-I"]).strip().decode().split()[1]
    )  # Uses output of terminal to get ip address
    port = 8000  # default port number if one is not specified

    def __init__(self, ip_address: str, port: int):
        """
        Constructor for Server object

        Take in ip_address as a string and the port as an int
        """
        self.ip_address = ip_address
        self.port = port
