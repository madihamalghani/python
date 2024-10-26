from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fr_om,to):
        print(f'Ticket is booked in train no {self.trainNo} from {fr_om} to {to}')
    def getStatus(self):
        print(f'Train no: {self.trainNo} is running on time')
    def getFare(self,fr_om,to):
        print(f'Ticket fare in train no: {self.trainNo} from {fr_om} to {to} is {randint(222,800)}')
t=Train(129)
t.book("Multan","Lahore")
t.getStatus()
t.getFare("Multan","Lahore")