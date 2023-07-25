from datetime import datetime, date
from client import Client

class Message:
    
    def __init__(self, sender: Client, msg: str):
        """A class for each message sent/received
        @sender: The Client object sending the message
        @msg: The raw data being transferred over the TCP connection
        """

        self.sendDate = date.today()  # date.today() returns in the format yr/mon/day, sets the date of the message
        self.sendTime = datetime.now().strftime("%H:%M:%S") # sets the time of the message
        self.sender = sender
        self.msg = msg
