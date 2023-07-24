from datetime import datetime, date
import client

class Message:
    '''Represents a message and contains the metadata for each message
    metadata: 
        Date message was sent in the format yr/month/day
        Time message was sent
        User that sent message
        Message that was sent'''
    def __init__(self, sender: client, msg: str):
        self.sendDate = date.today()  #date.today() returns in the format yr/mon/day
        self.sendTime = datetime.now().strftime("%H:%M:%S")
        self.sender = sender
        self.msg = msg
    
    if __name__ == "__main__":
        pass
