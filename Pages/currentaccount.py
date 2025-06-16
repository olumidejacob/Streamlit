import streamlit as st

with st.form("current_account_form"):
    amount = st.number_input("Enter amount", min_value=1000)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

# 1. Initialize variables
balance = 1000.00  # Starting balance, using a float for decimal money
transaction_history = [] # An empty list to store what happened

# 2. Welcome message
print("---------------------------------------")
print("   Welcome to Your Simple Bank App!    ")
print("---------------------------------------")
print(f"Your starting balance is: N{balance:.2f}") # .2f formats to 2 decimal places

# 3. Main loop for interactions
while True: # This loop will keep running until you choose to exit
    print("\n--- Main Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    # Get user's choice
    choice = input("Enter your choice (1-5): ")

    # 4. Handle user's choice
    if choice == '1':
        # Check Balance
        print(f"\nYour current balance is: N{balance:.2f}")

    elif choice == '2':
        # Deposit Money
        try: # Try to do this, if it fails (like entering text), go to 'except'
            amount_to_deposit = float(input("Enter amount to deposit: N"))
            if amount_to_deposit <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                balance = balance + amount_to_deposit # Add to balance
                # Record the transaction
                transaction_history.append(f"Deposited N{amount_to_deposit:.2f} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. New balance: N{balance:.2f}")
                print(f"N{amount_to_deposit:.2f} deposited successfully.")
                print(f"New balance: N{balance:.2f}")
        except ValueError: # If the user didn't enter a valid number
            print("Invalid input. Please enter a number for the amount.")

    elif choice == '3':
        # Withdraw Money
        try:
            amount_to_withdraw = float(input("Enter amount to withdraw: N"))
            if amount_to_withdraw <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount_to_withdraw > balance: # Check if there's enough money
                print("Insufficient funds. You don't have enough money.")
            else:
                balance = balance - amount_to_withdraw # Subtract from balance
                # Record the transaction
                transaction_history.append(f"Withdrew N{amount_to_withdraw:.2f} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. New balance: N{balance:.2f}")
                print(f"N{amount_to_withdraw:.2f} withdrawn successfully.")
                print(f"New balance: N{balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    elif choice == '4':
        # View Transaction History
        print("\n--- Transaction History ---")
        if len(transaction_history) == 0: # Check if the list is empty
            print("No transactions yet.")
        else:
            for transaction in transaction_history: # Go through each item in the list
                print(transaction)

    elif choice == '5':
        # Exit
        print("\nThank you for using the Simple Bank App. Goodbye!")
        break # This breaks out of the 'while True' loop, ending the program

    else:
        # Invalid choice
        print("Invalid choice. Please enter a number between 1 and 5.")

# Optional: Import datetime for transaction timestamps
from datetime import datetime