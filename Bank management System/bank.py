
from customer import Customer
from savings_account import SavingsAccount
from current_account import CurrentAccount
from home_loan import HomeLoan
from personal_loan import PersonalLoan

class Bank:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
        self.__customers = []

    # -------- Customer --------
    def add_customer(self, name, phone, address):
        customer = Customer(name, phone, address)
        self.__customers.append(customer)
        print(f"Customer created. ID: {customer.get_customer_id()}")
        return customer

    def find_customer(self, cust_id):
        for c in self.__customers:
            if c.get_customer_id() == cust_id:
                return c
        return None

    # -------- Account --------
    def open_account(self, customer, acc_type):
        if acc_type.lower() == "savings":
            account = SavingsAccount(customer)
        elif acc_type.lower() == "current":
            account = CurrentAccount(customer)
        else:
            print("Invalid account type.")
            return None

        customer.add_account(account)
        print(f"{acc_type.capitalize()} Account created. A/C No: {account.get_account_no()}")
        return account

    def find_account(self, acc_no):
        for customer in self.__customers:
            for acc in customer.get_accounts():
                if acc.get_account_no() == acc_no:
                    return acc
        return None

    # -------- Transfer within same bank --------
    def transfer_between_customers(self, from_acc_no, to_acc_no, amount):
        from_account = self.find_account(from_acc_no)
        to_account = self.find_account(to_acc_no)

        if not from_account or not to_account:
            print("One of the accounts not found.")
            return

        initial_balance = from_account.get_balance()
        from_account.withdraw(amount)

        if from_account.get_balance() == initial_balance:
            print("Transfer failed during withdrawal.")
            return

        to_account.deposit(amount)
        print(f"₹{amount} transferred successfully within the bank.")

    # -------- Loan --------
    def apply_loan(self, customer, loan_type, amount, years):
        if loan_type.lower() == "home":
            loan = HomeLoan(customer, amount, years)
        elif loan_type.lower() == "personal":
            loan = PersonalLoan(customer, amount, years)
        else:
            print("Invalid loan type.")
            return None

        customer.add_loan(loan)
        print(f"{loan_type.capitalize()} Loan Approved. Loan ID: {loan.get_loan_id()}")
        return loan
    
        # -------- Show loan details --------
    def show_customer_loans(self, cust_id):
        customer = self.find_customer(cust_id)
        if not customer:
            print("Customer not found.")
            return

        loans = customer.get_loans()
        if not loans:
            print("No loans for this customer.")
            return

        for loan in loans:
            loan.show_loan_summary()


    # -------- Display --------
    def display_bank_details(self):
        print(f"\nBank: {self.name}, Branch: {self.branch}")
        for c in self.__customers:
            c.show_details()
