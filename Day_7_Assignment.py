# Assignment - List of dictionaries: To print this: dhara.print_statement()
# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000
from datetime import datetime

class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Failure. Insufficient balance"
        self.balance -= amount
        self.add_transaction(len(self.transactions) + 1, datetime.now(), 'withdraw', amount)
        return f"Success. Your balance is: R{self.balance:,}"

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction(len(self.transactions) + 1, datetime.now(), 'deposit', amount)
        return f"Success. Your balance is: R{self.balance:,}"
    
    def add_transaction(self, id, date, type, amount):
        transaction = {
            'id': id,
            'date': date,
            'type': type,
            'amount': amount
        }
        self.transactions.append(transaction)
    
    def print_statement(self):
        print(f"id\tDate  \t  Type\t\tAmount")
        for transaction in self.transactions:
            print(f"{transaction['id']:<5} {transaction['date'].strftime('%d %b'):<10} {transaction['type']:<10} {transaction['amount']:>10}")
    
gemma = Bank("123", "Gemma Porrill", 15_000)
dhara = Bank("124", "Dhara Kara", 50_001)
caleb = Bank("125", "Caleb Potts", 100_000)

# Display balance
print(gemma.display_balance())

# For Caleb
print(caleb.withdraw(120000))
print(caleb.display_balance())

# Dhara
print(dhara.deposit(10_000))
print(dhara.withdraw(15_000))
dhara.print_statement()