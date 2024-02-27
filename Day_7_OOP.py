# Object Oriented Programming 
# If I could model my problem as real life problem it could make my life easier

# Car
# 1. engine
# 2. wheels
# 3. doors

# Toyota Tazz:
# 1. engine - v4
# 2. wheels - 4
# 3. doors - 4

# Ferrari:
# 1. engine - v4
# 2. wheels - 4
# 3. doors - 2

# Car -> Blueprint | Class blueprint object
# __init__ -> first method to create the object (initializes)
class Car:
    def __init__(self, name, engine, wheels, doors):
        self.name = 'ferrari'
        self.engine = "v4"
        self.wheels = 4
        self.doors = 2
    def horn(self):
        return "Vroom Vroom"

ferrari = Car("Ferrari", "v8",4,2)
toyota = Car("Toyota", "v4",4,4)
bmw = Car("bmw", "v6", 4,4)


# Create a bank  Account
# 1. acc_no
# 2. name
# 3. balance

class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return(f"Your balance is: R{self.balance:,}")

    def withdraw(self, amount):
        if amount > self.balance:
            return("Failure. Insufficient balance")
        self.balance -= amount
        return(f"Success. Your balance is: R{self.balance:,}")
    
    def deposit(self, amount):
        self.balance += amount
        return(f"Success. Your balance is: R{self.balance:,}")

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


# Assignment - List of dictionaries: To print this: dhara.print_statement()
# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount  
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000  