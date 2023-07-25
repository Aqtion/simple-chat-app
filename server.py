from subprocess import check_output

<<<<<<< HEAD
=======
'''
The Server class holds the attributes of the Server object: ip_address and port
'''

>>>>>>> dea7f9f90904ee8d216868edc670cc553b4badbb
class Server:

    ip_address = check_output(['hostname',  '-I']).strip().decode().split()[1] # Uses output of terminal to get ip address
    port = 8001 # default port number if one is not specified

    
    def __init__(self, ip_address: str, port: int):
        """A class for the server attributes
        @ip_address: The IP address of the server
        @port: The port number of the server
        """
<<<<<<< HEAD
        self.ip_address = ip_address
        self.port = port
=======
        self.ip_address = ip_address
>>>>>>> dea7f9f90904ee8d216868edc670cc553b4badbb
