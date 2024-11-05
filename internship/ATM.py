class ATM:
    def _init_(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self):
        """Prompt user to enter PIN and check if it matches the stored PIN."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def account_balance(self):
        """Display the current account balance."""
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Checked account balance.")

    def deposit(self, amount):
        """Add the deposit amount to balance and record the transaction."""
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.transaction_history.append(f"Deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw amount from balance if funds are sufficient and record the transaction."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def change_pin(self):
        """Allow user to change the PIN after verifying the current one."""
        current_pin = input("Enter your current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("PIN changed.")
            else:
                print("PIN confirmation does not match.")
        else:
            print("Incorrect current PIN.")

    def show_transaction_history(self):
        """Display a list of all previous transactions."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction}")
        else:
            print("No transactions found.")

    def main_menu(self):
        """Display the main menu for ATM operations and prompt user choice."""
        while True:
            print("\nATM Main Menu")
            print("1. Balance Inquiry")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                if self.check_pin():
                    self.account_balance()
            elif choice == '2':
                if self.check_pin():
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
            elif choice == '3':
                if self.check_pin():
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
            elif choice == '4':
                if self.check_pin():
                    self.change_pin()
            elif choice == '5':
                if self.check_pin():
                    self.show_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")


