# account.py
from abc import ABC, abstractmethod
import random

class Account(ABC):
    _used_account_numbers = set()   

    def __init__(self, customer):
        self.__account_no = self.__generate_account_no()
        self.__balance = 0
        self.customer = customer

    # -------- Random Account Number Generator --------
    def __generate_account_no(self):
        while True:
            acc_no = random.randint(1000000000, 9999999999)  # 10-digit number
            if acc_no not in Account._used_account_numbers:
                Account._used_account_numbers.add(acc_no)
                return acc_no

    # -------- Getters --------
    def get_account_no(self):
        return self.__account_no

    def get_balance(self):
        return self.__balance

    # -------- Deposit --------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    # -------- Protected deduct --------
    def _deduct_balance(self, amount):
        self.__balance -= amount

    # -------- Abstract Methods --------
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
