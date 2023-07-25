from subprocess import check_output

class Server:
    ip_address = (
        check_output(["hostname", "-I"]).strip().decode().split()[1]
    )  # Uses output of terminal to get ip address
    port = 8000  # default port number if one is not specified

    def __init__(self, ip_address: str, port: int):
        """A class for the server attributes
        @ip_address: The IP address of the server
        @port: The port number of the server
        """
        self.ip_address = ip_address
        self.port = port