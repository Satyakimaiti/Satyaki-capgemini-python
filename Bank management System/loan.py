# loan.py
from abc import ABC, abstractmethod
import math

class Loan(ABC):
    _loan_counter = 5000

    def __init__(self, customer, amount, years):
        Loan._loan_counter += 1
        self.__loan_id = Loan._loan_counter
        self.__amount = amount
        self.__years = years
        self.__customer = customer

    def get_loan_id(self):
        return self.__loan_id

    def get_amount(self):
        return self.__amount

    def get_years(self):
        return self.__years

    # -------- EMI Calculation --------
    def calculate_emi(self, annual_rate):
        P = self.__amount
        R = annual_rate / (12 * 100)
        N = self.__years * 12

        emi = (P * R * math.pow(1 + R, N)) / (math.pow(1 + R, N) - 1)
        return round(emi, 2)

    def total_payable_amount(self, annual_rate):
        emi = self.calculate_emi(annual_rate)
        total = emi * self.__years * 12
        return round(total, 2)

    @abstractmethod
    def pay_emi(self, amount):
        pass
