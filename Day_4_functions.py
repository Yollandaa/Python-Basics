a = 8
b = 10

print("The sum is: ", a + b)


# Declaration/Definition part
# def sum(a, b):  #(a,b) Parameters/arguments
#   return a + b


# Default values
def driving_test(name, age, car="Toyota tezz"):
  if age >= 18:
    return "You are eligible for driving"
  else:
    "Try again after few years"


print(driving_test("Caleb", 20, "GR Corrola"))
print(driving_test(age=21, name="Dhara"))  #Keyword arguments

print()


# def sum(a, b):
#   return a + b


#Lambda functions
# Lambda functions are anonymous functions: nameless function
# add = lambda a, b: a + b

# print(add(6,7))

arr = [10, 30, 60]
double_values = lambda x: x * 2
print(list(map(double_values, arr)))
print()


# greeting is a high order function and map also: Accepts a function as an argument
def say_hello():
  return "Hello "


def greeting(hello_message, name):
  print(hello_message() + name)


greeting(say_hello, 'Caleb')
print()


# output should be [20, 60, 120]
# The fn we receiving is: lambda x: x * 2
def map_own(fn, arr):
  result = []
  for item in arr:
    result.append(fn(item))
  return result


print(map_own(lambda x: x * 2, [10, 30, 60]))

print()


# List comprehension
def map_own1(fn, arr):
  return [fn(item) for item in arr]


print(map_own1(lambda x: x * 2, [10, 30, 60]))


def sayHello1():

  def msg():
    return "Hello, 🎊"

  return msg


print(sayHello1()())

# Another way to do it
one_part = sayHello1()
print(one_part())

# Currying, Partials
mul = lambda x: lambda y: x * y

# Output 3 6 -> 18
print(mul(3)(6))

mul_5 = mul(5)
mul_10 = mul(10)

print(mul_5, type(mul_5))
# rewrite mul as a function
def mulx(x):

  def muly(y):
    return x * y
  return muly

print(mulx(3)(6))

# filters
result2 = filter(lambda x: x > 10, [10, 50, 60, 100, 6, 8, 30])
print(list(result2))

# Pythonic way: Using list comprehension
print([x for x in [10, 50, 60, 100, 6, 8, 30] if x > 10])

# Sequence - List
# 1. len
# 2. sum
# 3. sorted 
# 
print(sum([10, 80, 30, 60]))
print(all([True, False, True])) # Behaves like and
print(any([True, False, True])) # Behaves like or

print(all([10, 0, 30, -1])) # 0 is False


# What are considered false
# 1. 0
# 2. None
# 3. None, False, 0, 0.0, [], (), {}
# 4. ""
