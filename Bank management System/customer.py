# customer.py

class Customer:
    _customer_counter = 0

    def __init__(self, name, phone, address):
        Customer._customer_counter += 1
        self.__customer_id = Customer._customer_counter
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__accounts = []
        self.__loans = []

    # -------- Getters --------
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    # -------- Account Handling --------
    def add_account(self, account):
        self.__accounts.append(account)

    def get_accounts(self):
        return self.__accounts

    # -------- Loan Handling --------
    def add_loan(self, loan):
        self.__loans.append(loan)

    def get_loans(self):
        return self.__loans

    # -------- Display --------
    def show_details(self):
        print("\nCustomer ID:", self.__customer_id)
        print("Name:", self.__name)
        print("Accounts:", [acc.get_account_no() for acc in self.__accounts])
        print("Loans:", [loan.get_loan_id() for loan in self.__loans])
