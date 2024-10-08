# Author: Rohan Laxman Waghmare
# Task: Create An ATM Machine Simulation

# Automated Teller Machine Simulation

class ATM:
    def __init__(self, initial_balance=0):
        
        # firstly ATM class is with a default balance, PIN, and empty transaction history
        
        self.balance = initial_balance
        self.pin = 1234  # this is a default PIN i generate to use
        self.transactions = []  # here will be store transaction history after the authentication done successfully (PIN)

    def authenticate(self):
        
        # this method covers the users authentication process like PIN before accessing to the ATM interface
        
        attempts = 3  # this allow user 3 attempts to enter the correct PIN
        while attempts > 0:
            entered_pin = int(input("Enter your PIN: "))
            if entered_pin == self.pin:
                print("Authentication Process Successful!\n")
                return True
            else:
                attempts -= 1 # this line decreases user attempts by 1, -= operator is use for subtracting 1 from the current value of attempts
                print(f"Incorrect PIN. Please enter correct PIN, you have {attempts} attempts left.")
        
        print("Authentication failed. Exiting program.") # this will print if 3 attempts failed
        return False

    def display_menu(self):
        
        # these interface will print on screen of ATM options menu to the user

        print("\nATM Menu Bar:")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        # from here below are the menu's programmed
        
        # this is the first option of menu "Balance Inquiry"
    def balance_inquiry(self):
        
        # this method display the current balance of the account of user
        
        print(f"Your current balance is: ₹{self.balance}")

        # this is the second option of menu "Cash Deposit"
    def cash_deposit(self):
        
        # this method allows the user to deposit money into the account and record the transaction.
        
        amount = float(input("Enter the amount to deposit: ₹"))
        self.balance += amount 
        self.transactions.append(f"Deposited: ${amount}")
        print(f"₹{amount} has been deposited to your account.")

        # this is the third option of menu "Cash Withdrawal"
    def cash_withdrawal(self):
        
        # this method allows the user to withdraw money from the account if there is a sufficient balance avalaible
        
        amount = float(input("Enter the amount to withdraw: ₹")) # entering the amount number to withdraw
        if amount > self.balance:
            print("Insufficient balance! Please do Balance Inquiry.")  # if user enter amount more than available balance, this error will print
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount}")  
            print(f"₹{amount} has been withdrawn from your account.")

        # this is the fourth option of menu "Change PIN"
    def pin_change(self):
        
        # allowing the user to change the PIN after verifying the original PIN
        
        current_pin = int(input("Enter your current PIN: "))
        if current_pin == self.pin:
            new_pin = int(input("Enter your new PIN: "))  # generating new PIN by user
            confirm_pin = int(input("Confirm your new PIN: ")) # confirming the generated new PIN by user
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully!")
            else:
                print("New PIN and confirmation do not match.") # this occur due to not matching the "Enter your new PIN: "
        else:
            print("Incorrect current PIN.")

        # this is the fifth option of menu "Transaction History"
    def transaction_history(self):
        
        print("Transaction History:") # this method display the transaction history of the bank account
        if not self.transactions:
            print("No transactions is done yet!")
        else:
            for transaction in self.transactions:
                print(transaction)


        # this is the main method to run the ATM simulation, in which user able to choose necessary option as they need
    def run(self): 
        
        if not self.authenticate():  # here write the correct PIN to access
            return
        
        while True:
            self.display_menu()
            choice = int(input("Select an option: "))
            
            if choice == 1:
                self.balance_inquiry()
            elif choice == 2:
                self.cash_deposit()
            elif choice == 3:
                self.cash_withdrawal()
            elif choice == 4:
                self.pin_change()
            elif choice == 5:
                self.transaction_history()
            elif choice == 6:      # this is the sixth option from menu to exit from login ATM bank account
                print("Thank you for visiting here. Have a nice day!")  
                break
            else:
                print("Invalid choice, please try again.") # in case, if you select option apart from given 6 options this error will print on screen


atm = ATM(initial_balance=999) # created initial balance of ₹999 in the bank account

atm.run() # it run the ATM program
