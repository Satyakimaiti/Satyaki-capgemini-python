# personal_loan.py
from loan import Loan

class PersonalLoan(Loan):
    INTEREST = 12

    def pay_emi(self, amount):
        print(f"EMI paid for Personal Loan: ₹{amount}")

    def show_loan_summary(self):
        emi = self.calculate_emi(PersonalLoan.INTEREST)
        total = self.total_payable_amount(PersonalLoan.INTEREST)

        print("\n--- Personal Loan Summary ---")
        print("Loan ID:", self.get_loan_id())
        print("EMI per month: ₹", emi)
        print("Total amount to be paid in", self.get_years(), "years: ₹", total)
