#Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.


"proceding with que9"

from random import randint

class Train:
    def __init__(HARRY, trainNo):
        HARRY.trainNo = trainNo
        
    def book(HARRY, fro , to):
        print(f"the ticket is booked in train no: {HARRY.trainNo} from {fro} to {to}")
    def getstatus(HARRY, fro , to):
        print(f"the train  {HARRY.trainNo} is running successfully from {fro} to {to} on time.")
    def getfare(HARRY, fro , to):
        print(f"ticket fare in train no. : {HARRY.trainNo} from {fro} to {to} is {randint(222,5555)}")
        
t = Train(12399)        
t.book("rampur", "delhi")
t.getstatus("rampur", "delhi")
t.getfare("rampur","delhi")
    
    
"""
ANSWER --->>>>           YES WE CAN , WITH NO CHANGE
 """   