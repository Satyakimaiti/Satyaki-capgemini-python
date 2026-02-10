
from account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000   

    def __init__(self, customer):
        super().__init__(customer)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
            return

        available_limit = self.get_balance() + CurrentAccount.OVERDRAFT_LIMIT

        if amount > available_limit:
            print("Overdraft limit exceeded.")
            return

        self._deduct_balance(amount)
        print(f"₹{amount} withdrawn successfully from Current Account.")

    def calculate_interest(self):
        print("No interest for Current Account.")
        return 0
