
class TransferService:

    @staticmethod
    def transfer(from_account, to_account, amount):
        if amount <= 0:
            print("Invalid transfer amount.")
            return

        initial_balance = from_account.get_balance()
        from_account.withdraw(amount)

        if from_account.get_balance() == initial_balance:
            print("Transfer failed during withdrawal.")
            return

        to_account.deposit(amount)
        print(f"₹{amount} transferred successfully!")
