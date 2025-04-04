# this a parrent class of entity handling the change in bank balance
class Corporation:
    def __init__(self, name, bank_balance=1000):
        self.name = name
        self.bank_balance = bank_balance
    def get_name(self):
        # returns name
        return self.name

    def get_balance(self):
        # returns balance
        return self.bank_balance
    def decrease_balance(self, decrease):
        # decreases bank balance
        self.bank_balance = self.bank_balance - decrease
        print("new balance is", self.bank_balance)
    def increase_balance(self, increase):
        # increase bank balance
        self.bank_balance = self.bank_balance + increase
        print("new balance is", self.bank_balance)