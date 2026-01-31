from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry,fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(self):
                print(f"Ticket is: {self.trainNo} is running on time")


    def getFare(self,fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(5000, 1500000)}")


t = Train(12356)
t.book("Dholakpur", "Furfuri Nagar")
t.getStatus()
t.getFare("Dholakpur", "Furfuri Nagar")