# main.py
from bank import Bank

def main():
    bank = Bank("Python Bank", "Bhubaneswar")

    while True:
        print("\n====== BANK MENU ======")
        print("1. Add Customer")
        print("2. Open Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Transfer Between Customers")
        print("7. Show Bank Details")
        print("8. Apply Loan")
        print("9.Show Loan Summary")
        print("10. Exit")

        choice = input("Enter choice: ")

        # ---- Add Customer ----
        if choice == '1':
            bank.add_customer(input("Name: "), input("Phone: "), input("Address: "))

        # ---- Open Account ----
        elif choice == '2':
            cust_id = int(input("Customer ID: "))
            acc_type = input("Account type (savings/current): ")

            customer = bank.find_customer(cust_id)

            if customer:
                bank.open_account(customer, acc_type)
            else:
                print("Customer not found.")

        # ---- Deposit ----
        elif choice == '3':
            acc_no = int(input("Account No: "))
            amount = float(input("Amount: "))

            acc = bank.find_account(acc_no)
            if acc:
                acc.deposit(amount)
            else:
                print("Account not found.")

        # ---- Withdraw ----
        elif choice == '4':
            acc_no = int(input("Account No: "))
            amount = float(input("Amount: "))

            acc = bank.find_account(acc_no)
            if acc:
                acc.withdraw(amount)
            else:
                print("Account not found.")

        # ---- Balance ----
        elif choice == '5':
            acc_no = int(input("Account No: "))

            acc = bank.find_account(acc_no)
            if acc:
                print("Balance: ₹", acc.get_balance())
            else:
                print("Account not found.")

        # ---- Transfer ----
        elif choice == '6':
            from_acc = int(input("From Account No: "))
            to_acc = int(input("To Account No: "))
            amount = float(input("Amount: "))

            bank.transfer_between_customers(from_acc, to_acc, amount)

        # ---- Display ----
        elif choice == '7':
            bank.display_bank_details()

        # ---- Apply Loan ----
        elif choice == '8':
            cust_id = int(input("Customer ID: "))
            loan_type = input("Loan type (home/personal): ")
            amount = float(input("Loan amount: "))
            years = int(input("Years: "))

            customer = bank.find_customer(cust_id)

            if customer:
                bank.apply_loan(customer, loan_type, amount, years)
            else:
                print("Customer not found.")

        elif choice == '9':
            cust_id = int(input("Customer ID: "))
            bank.show_customer_loans(cust_id)

        elif choice == '10':
            print("Thank you!")
            break


        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
