# from flask import Flask

# app = Flask('app')

# @app.route('/')
# def hello_world():
#   return 'Hello, World!'

# app.run(host='0.0.0.0', port=8080)
temperature = float(input("Please enter a temperature in ferenheit "))
convert = (temperature - 32) * (5 / 9)
print(f"Temperature in celsius {convert} C")

birth_year = input("Enter the year you were born in ")
age = 2024 - int(birth_year)
print(f"You are {age} years old")

r = input("Enter radius ")
area = 3.1415 * float(r)**2
print(f"The area of the circle is {area}")

num = input("Enter a number ")
eq = int(num) // 10
spaces = 10 - eq
print(f'[{"=" * eq} {" " * spaces}] {num}%')
