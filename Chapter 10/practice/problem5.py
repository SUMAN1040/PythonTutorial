# Write a class Train which has methods to book a ticket, get status (no of seats) and get information of train running under Indian Railway

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
                print(f"Ticket is: {self.trainNo} is running on time")


    def getFare(self,fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(5000, 1500000)}")


t = Train(123456)
t.book("Dholakpur", "Furfuri Nagar")