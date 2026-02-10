
from account import Account

class SavingsAccount(Account):
    INTEREST_RATE = 0.04   
    WITHDRAW_LIMIT = 3     

    def __init__(self, customer):
        super().__init__(customer)
        self.__withdraw_count = 0

    def withdraw(self, amount):
        if self.__withdraw_count >= SavingsAccount.WITHDRAW_LIMIT:
            print("Withdrawal limit reached for today.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.get_balance():
            print("Insufficient balance.")
            return

        self._deduct_balance(amount)
        self.__withdraw_count += 1
        print(f"₹{amount} withdrawn successfully from Savings Account.")

    def calculate_interest(self):
        interest = self.get_balance() * SavingsAccount.INTEREST_RATE
        print(f"Interest for Savings Account: ₹{interest}")
        return interest
