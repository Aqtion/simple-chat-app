from datetime import datetime, date
import client


class Color:
    DARKCYAN = "\033[36m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


class Message:
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
        self.sender = sender
        self.msg = msg

    def create_message(self):
        date = Color.DARKCYAN + self.sendTime + Color.BOLD + Color.END
        user = Color.RED + self.sender.username + Color.BOLD + Color.END
        data = Color.BOLD + self.msg + Color.END
        return (date + " | <" + user + "> " + data).encode()

    if __name__ == "__main__":
        pass
