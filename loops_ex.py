numbers = [8, 5, 7, 4, 6, 2]
# ["Even", "Odd", "Odd", "Even", "Even", "Even"] in list comprehension
#odds = [num for num in numbers if num % 2 != 0]
# print(odds)

# I want to print "Even" if a number is divisible by 2 else "Odd" if it isn't
odd_even = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(odd_even)

for index, val in enumerate(numbers):
  print(index, val)