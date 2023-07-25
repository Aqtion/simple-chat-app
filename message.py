from datetime import datetime, date
from client import Client


class Color:
    DARKCYAN = "\033[36m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"



class Color:
    DARKCYAN = "\033[36m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


class Message:
<<<<<<< HEAD
    
    def __init__(self, sender: Client, msg: str):
        """A class for each message sent/received
        @sender: The Client object sending the message
        @msg: The raw data being transferred over the TCP connection
        """

        self.sendDate = date.today()  # date.today() returns in the format yr/mon/day, sets the date of the message
        self.sendTime = datetime.now().strftime("%H:%M:%S") # sets the time of the message
=======
    """Represents a message and contains the metadata for each message
    metadata:
        Date message was sent in the format yr/month/day
        Time message was sent
        User that sent message
        Message that was sent"""

    def __init__(self, sender: client, msg: str):
        """Constructor for Message class
        Sets date and time to current date and time
        Sets sender and message to inputted sender and message"""

        self.sendDate = date.today()  # date.today() returns in the format yr/mon/day
        self.sendTime = datetime.now().strftime("%H:%M:%S")
>>>>>>> dea7f9f90904ee8d216868edc670cc553b4badbb
        self.sender = sender
        self.msg = msg

    def create_message(self):
<<<<<<< HEAD
        date = Color.DARKCYAN + self.sendTime + Color.END
        user = Color.RED + self.sender.username + Color.END
        data = Color.BOLD + self.msg + Color.END
        return (date + " | <" + user + "> " + data).encode()
=======
        date = Color.DARKCYAN + self.sendTime + Color.BOLD + Color.END
        user = Color.RED + self.sender.username + Color.BOLD + Color.END
        data = Color.BOLD + self.msg + Color.END
        print(user)
        return (date + " | <" + user + "> " + data).encode()

    if __name__ == "__main__":
        pass
>>>>>>> dea7f9f90904ee8d216868edc670cc553b4badbb
