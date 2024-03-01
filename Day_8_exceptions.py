def math_divide(n1, n2):
    try:
        result = n1 / n2
        print(f"The answer is {result}")
    except:
        # When there is an error
        print(f"You cannot divide by zero! 💀")

    else:
        # When there is no error
        print(f"Division was successful. ✅")
    finally:
        # Always goes in here regardless of whether the was an error or not
        print(f"Operation done!! ✌️✌️")


from datetime import datetime


# Task 1: Positive results
def calculate_age():
    year = input("Please tell me the year of birth: ")
    age = int(datetime.now().year) - int(year)
    print(f"You are {age} years old")


# Task 2: Handle the value error
def calculate_age1():
    try:
        year = input("Please tell me the year of birth: ")
        age = int(datetime.now().year) - int(year)
        print(f"You are {age} years old")
    except ValueError:
        print(f"Please enter a valid year")
    else:
        print(f"Age calculator was successfully calculated")
    finally:
        print("Operation done!!")


# Task 3: Logical errors
# Getting negetive year, getting a year that is > than the current year, create a valueError for this
def calculate_age2():
    try:
        year = int(input("Please tell me the year of birth: "))
        if year <= 0:
            # raise -> stops furthur execution
            # Handling logical errors
            raise ValueError(f"Year cannot be negative")
        elif year > datetime.now().year:
            raise ValueError(f"You're are not flash to be from the future")
        else:
            age = int(datetime.now().year) - int(year)
            print(f"You are {age} years old")
    except ValueError as err:
        print(f"Invalid year: ", err)
    except Exception as err:
        print(f"This is catch all: ", err)


# Create your own Error Class
class NegetiveNumbersError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negetive numbers are not allowed"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} -> {self.message}"


def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegetiveNumbersError(x)
    # Match what type of error we got
    except NegetiveNumbersError as e:  # Assign error to e | Making an alias
        print(e)


if __name__ == "__main__":
    print(math_divide(20, 0))
    # calculate_age2()
    # only_positive_num()
