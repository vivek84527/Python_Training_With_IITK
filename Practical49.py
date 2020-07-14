# Object Oriented Programming
# -------------------------------

class Account:
    "Details for all Account"
    accCount = 0  # Class variables

    def __init__(self, n, b):  # Constructor
        self.name = n
        self.balance = b
        Account.accCount = Account.accCount + 1
        print("Constructor is working.", b)

    def displayCount(self):
        print("Total Account %d" %
              Account.accCount)

    def displayAccount(self):
        print("Name : ", self.name,
              ", Balance: ", self.balance)


# Creating Instance Objects
ptr1 = Account("Pappu", 2000)
ptr2 = Account("Munni", 5000)
