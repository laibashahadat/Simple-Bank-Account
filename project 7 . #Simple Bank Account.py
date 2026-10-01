#------------------------------------------
# Simple To-Do List Manager
#------------------------------------------
balance = 0
#------------------------------------------
# deposit() Function
#------------------------------------------
def deposit():
    amount = int(input("Enter amount to deposit: "))
    global balance
    balance += amount
    print("Amount deposited successfully")
#------------------------------------------
# withdraw() Function
#------------------------------------------
def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully")
    else:
        print("Insufficient funds")
#------------------------------------------
# check_balance() Function
#------------------------------------------
def check_balance():
    print("Current balance:", balance)
#------------------------------------------
# main() Function
#------------------------------------------
while True:
    print("Simple Bank Account")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
