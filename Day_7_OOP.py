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
        self.name = "ferrari"
        self.engine = "v4"
        self.wheels = 4
        self.doors = 2

    def horn(self):
        return "Vroom Vroom"


ferrari = Car("Ferrari", "v8", 4, 2)
toyota = Car("Toyota", "v4", 4, 4)
bmw = Car("bmw", "v6", 4, 4)


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
        return f"Your balance is: R{self.balance:,}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Failure. Insufficient balance"
        self.balance -= amount
        return f"Success. {self.display_balance()}"

    def deposit(self, amount):
        self.balance += amount
        return f"Successfully deposited. {self.display_balance()}"


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
print(dhara.withdraw(30_000))


# Class variables: Share the value between the class objects/instances
# Encapsulation: Putting all your variables/classes and methods into one container | giving access -> private, public, protected
# put double underscore in the variable to make it private, do not allow it be be changed outside of the class Bank
class Bank:
    interest_rate = 0.02
    total_no_accounts = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance  # private variable
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
        return f"Your balance is: R{self.__balance:,}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Failure. Insufficient balance"
        self.__balance -= amount
        return f"Success. {self.display_balance()}"

    def deposit(self, amount):
        self.__balance += amount
        return f"Successfully deposited. {self.display_balance()}"

    def apply_interest(self):
        interest = Bank.interest_rate * self.__balance
        self.__balance += interest


gemma = Bank("123", "Gemma Porrill", 15_000)
dhara = Bank("124", "Dhara Kara", 50_001)
caleb = Bank("125", "Caleb Potts", 100_000)
alex = Bank("126", "Alex Lazarus", 100)

# After 1 year
# gemma.apply_interest()
# dhara.apply_interest()
# caleb.apply_interest()

# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())

# Updates for everyone
Bank.update_interest_rate(0.10)

# Apply interest
gemma.apply_interest()
dhara.apply_interest()
caleb.apply_interest()
alex.apply_interest()

print(gemma.display_balance())
print(dhara.display_balance())
print(caleb.display_balance())

# Task
print(Bank.get_total_no_accounts())  # 4

print("--------------------------------")


# Task
class Circle:
    pi = 3.14159  # Class variable: All instances share the same value

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return f"The area is: {Circle.pi * self.radius ** 2}"

    @classmethod
    def from_diameter(cls, diameter):
        # return Circle(diameter/2)
        return cls(diameter / 2)

    @staticmethod
    def perimeter(r):
        return f"The circumference is: {2*Circle.pi*r}"


circle1 = Circle(2)
print(circle1.calculate_area())

circle_from_diameter = Circle.from_diameter(10)
print(circle_from_diameter.calculate_area())

print(Circle.perimeter(10))

print("--------------------------------")


# Inheritance: Animal(base class)
# But Animal cannot have anythng in Dog
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    # Animal becomes the base of the dog class
    # Whather is inside animal class, dog can use it
    # Dog overrides the speak method

    def __init__(self, name, speed):
        super().__init__(name)  # We calling the Animal class to initialize the dog name
        self.speed = speed

    def speak(self):
        return "Woof!"

    def run(self):
        return "🙈 wags tail!!"

    def speed_bonus(self):
        return f"Running at {self.speed*2}km/hr."


toby = Animal("toby")
maxy = Dog("maxy", 20)
print(toby.speak())
print(maxy.speak())
print(maxy.speed_bonus())
