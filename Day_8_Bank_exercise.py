class Bank:
    interest_rate = 0.02
    total_no_accounts = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self._balance = balance  # private variable
        Bank.total_no_accounts += 1

    @classmethod  # cls -> Class
    def update_interest_rate(cls, rate):
        Bank.interest_rate = rate

    # We prefer static methods when we are not updating any class variables
    # Can also be outside of the class | normal method
    # static methods -> no cls, self | normal function
    @staticmethod
    def get_total_no_accounts():
        return Bank.total_no_accounts

    def display_balance(self):
        return f"Your balance is: R{self._balance:,}"

    def withdraw(self, amount):
        if amount > self._balance:
            return "Failure. Insufficient balance"
        self._balance -= amount
        return f"Success. {self.display_balance()}"

    def deposit(self, amount):
        self._balance += amount
        return f"Successfully deposited. {self.display_balance()}"

    def apply_interest(self):

        interest = self.interest_rate * self._balance
        self._balance += interest


gemma = Bank("123", "Gemma Porrill", 15_000)
dhara = Bank("124", "Dhara Kara", 50_001)
caleb = Bank("125", "Caleb Potts", 100_000)
alex = Bank("126", "Alex Lazarus", 100)

# Updates for everyone
Bank.update_interest_rate(0.10)

# Apply interest
gemma.apply_interest()
dhara.apply_interest()
caleb.apply_interest()
alex.apply_interest()

# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())


class SavingsAccount(Bank):
    interest_rate = 0.05


class CheckingAccount(Bank):

    def __init__(self, acc_no, name, balance):
        super().__init__(acc_no, name, balance)

    def withdraw(self, amount):
        amount += 1
        return super().withdraw(amount)


# SavingsAccount -  interest_rate = 0.05

# Task 1
gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
gemma.apply_interest()
print(gemma.display_balance())  # 1_050


# Task 2
# CheckingAccount - withdraw  R1
alex = CheckingAccount(126, "Alex Lazarus", 100)
print(alex.withdraw(50))
#  49

print(alex)


class SavingsAccount(Bank):
    interest_rate = 0.05


# Magic methods __repr__, __str__
class CheckingAccount(Bank):
    """This is for withdrawing"""

    def withdraw(self, amount):
        amount += 1
        return super().withdraw(amount)

    def __str__(self):
        """Human readable output"""
        return (
            f"This account belongs to {self.name} and has a balance of {self._balance}"
        )

    def __repr__(self):
        """DX: String -> Class"""
        return f"CheckingAccount('{self.acc_no}', '{self.name}', '{self._balance}')"

    """Add the two balances to the account"""

    def __add__(self, other):
        return self._balance + other._balance


alex = CheckingAccount(126, "Alex Lazarus", 100)
caleb = CheckingAccount(125, "Caleb Potts", 100_000)

print(alex)
print(alex._balance)
print(repr(alex))
print(repr(caleb))
print(alex + caleb)
