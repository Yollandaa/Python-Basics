# Virtual environment
# To be compatible with all python versions
# Creates a copy of your current python
# python -m venv myenv
# ctrl + ~ -> Open / Close terminal

# myenv -> copy of python
# .\myenv\Scripts\Activate.ps1 -> activate -> python -> local copy of python
# deactivate -> python -> global python installed
# Create a gitignore file and insert "myenv" so that it ignores any changes in the myenv folder.

# Shortcuts
# Ctrl + shift + p -> command
# Ctrl + p -> find file


# Lexical scope: Used the grandfather, father, son example
def market():
    price = 100
    def get_price():
        print("The price is " + str(price))
    get_price()

market()

# Scope -> Lifetime of a variable
def cool():
    x = 10

cool()
# x not defined, not whithin the scope
#print("the value of x is:", x)

# Within lexical scope
code_word = "Hulk"
def space_ship():
    question = "Please provide code word"

    def code_word_check():
        password = "Hulk" 
        print(question)

        if code_word == password:
            print(f"Welcome, {password} the strongest avenger 💪")
        else:
            print("❌ Access denied to 🚀")
    code_word_check()

space_ship()

def add(x):
    def add1(y):
        return x + y
    return add1
print(add(10)(5))

# Default values: copy by reference -> updates original values
def fun(nums=[]):
    nums.append(10)
    print(nums)

fun()
fun()
fun()
fun()
# [10]
# [10, 10]
# [10, 10, 10]
# [10, 10, 10, 10]

# Create the same fun function but output should have only one element, no pass by reference but pass by values
def fun_1(nums=None):
    if nums is None:
        nums = []
    nums.append(10)
    print(nums)
fun_1()
fun_1()
fun_1()
fun_1()