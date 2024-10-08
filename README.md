
# ATM Machine Simulation Project
- This project is a Python-based simulation of an Automated Teller Machine (ATM).
- It provides users with a simple command-line interface to perform basic banking operations, such as checking their balance, depositing and withdrawing cash, changing their PIN, and viewing transaction history.
- The project is designed to offer a realistic ATM experience through a menu-driven navigation system and user authentication via a secure PIN mechanism.

## Features
The ATM Machine Simulation includes the following functionalities:
1. User Authentication:
- Users are required to authenticate with a 4-digit PIN to access the ATM’s functionalities. The program allows up to 3 attempts to enter the correct PIN.
2. Balance Inquiry:
- Displays the current account balance to the user.
3. Cash Deposit:
- Allows the user to deposit a specified amount into their account. The deposited amount is then updated in the balance and recorded in the transaction history.
4. Cash Withdrawal:
- Enables the user to withdraw a specified amount from their account, provided that sufficient funds are available. The withdrawn amount is deducted from the balance and recorded in the transaction history.
5. PIN Change:
- Users can change their PIN after successfully authenticating with their current PIN.
6. Transaction History:
- Displays a history of all transactions (deposits and withdrawals) performed during the current session.
7. Exit:
- Allows the user to exit the ATM system.

## Project Structure
- The main components of the project include:

1. ATM Class:
a. Handles the ATM functionalities, including user authentication, displaying the menu, and managing transactions.

2. Methods:
- authenticate(): Verifies the user's PIN.
- display_menu(): Shows the list of available options.
- balance_inquiry(): Prints the current balance.
- cash_deposit(): Enables cash deposit and updates the balance.
- cash_withdrawal(): Handles cash withdrawal operations.
- pin_change(): Allows the user to change their PIN.
- transaction_history(): Displays the transaction history.
- run(): Main method that controls the flow of the ATM simulation.

## How to Run
1. Navigate to the project directory: cd Task 1
2. Run the atm.py file: python atm.py

## Tools and Technologies Used
1. Programming Language: Python 3.6 or higher
2. Python Libraries: No external libraries are used; the project uses standard Python built-in functionalities.
3. Syntax and Concepts:
- Classes and Objects
- Methods and Function Calls
- Control Flow (if-else conditions)
- Loops (for and while)
- Exception Handling
- Input/Output operations
- List operations for transaction tracking
4. Development Environment (IDE): VS Code (Visual Studio Code): Used for writing and testing the Python code.

## Author
**Rohan Laxman Waghmare**
