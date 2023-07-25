from datetime import datetime, date
from client import Client


class Color:
    DARKCYAN = "\033[36m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


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

    def create_message(self):
        date = Color.DARKCYAN + self.sendTime + Color.END
        user = Color.RED + self.sender.username + Color.END
        data = Color.BOLD + self.msg + Color.END
        return (date + " | <" + user + "> " + data).encode()
