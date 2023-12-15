import subprocess
import os

def show_main():
    subprocess.run([os.sys.executable, 'main.py'])

bank_balance = 0.0  # Initialize the bank balance

def show_bank_balance():
    global bank_balance
    print(f"Bank balance: {bank_balance:.2f}")

def deposit_money(amount):
    global bank_balance
    bank_balance += amount

def main():
    while True:
        user_input = input("Type 'show balance' to check your bank balance or 'exit' to quit: ")

        if user_input.lower() == 'show balance':
            show_bank_balance()
        elif user_input.lower() == 'exit':
            break
        else:
            print("Invalid command. Please type 'show balance' or 'exit'.")

if __name__ == "__main__":
    main()