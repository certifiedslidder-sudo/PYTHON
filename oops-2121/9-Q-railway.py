#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro , to):
        print(f"the ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def getstatus(self, fro , to):
        print(f"the train  {self.trainNo} is running successfully from {fro} to {to} on time.")
        
    def getfare(self, fro , to):
        print(f"ticket fare in train no. : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
        
t = Train(12399)        
t.book("rampur", "delhi")
t.getstatus("rampur", "delhi")
t.getfare("rampur","delhi")
    

    