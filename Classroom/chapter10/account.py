from decimal import Decimal as d

class Account:
    """Manage account-related data"""
    def __init__(self, n, b):
        self.name = n
        self.balance = d(b)  

    def get_name(self):
        return self.name

    def deposit(self, amount):
        amount = d(amount)
        if amount <= d('0.00'):
            raise ValueError("Invalid deposit amount.")
        else:
            self.balance += amount  
            print(f"The amount in the account after deposit is: {self.balance}")

    def withdraw(self, amount):
        amount = d(amount)
        if amount <= d('0.00'):
            raise ValueError("Invalid withdrawal amount.")
        else:
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            else:
                self.balance -= amount  
                print(f"The amount in the account after withdrawal is: {self.balance}")


# Input from user
bal = input("Enter the balance in the account: ")
na = input("Enter the name: ")

# Create Account instance
acc = Account(na, bal)

# Display account information
print(f"Account holder's name is: {acc.get_name()}")
print(f"Initial balance is: {acc.balance}")

# Deposit money
dep = d(input("Enter the deposit amount: "))
acc.deposit(dep)

# Withdraw money
wit = d(input("Enter the withdrawal amount: "))
acc.withdraw(wit)

# Final balance after transactions
print(f"Final balance is: {acc.balance}")
