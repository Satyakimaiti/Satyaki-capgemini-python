# home_loan.py
from loan import Loan

class HomeLoan(Loan):
    INTEREST = 7.5

    def pay_emi(self, amount):
        print(f"EMI paid for Home Loan: ₹{amount}")

    def show_loan_summary(self):
        emi = self.calculate_emi(HomeLoan.INTEREST)
        total = self.total_payable_amount(HomeLoan.INTEREST)

        print("\n--- Home Loan Summary ---")
        print("Loan ID:", self.get_loan_id())
        print("EMI per month: ₹", emi)
        print("Total amount to be paid in", self.get_years(), "years: ₹", total)
