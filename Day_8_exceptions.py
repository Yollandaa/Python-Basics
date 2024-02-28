try:
    result = 10 / 0
    print(f"The answer is {result}")
except ZeroDivisionError:
    # When there is an error
    print(f"You cannot divide by zero! 💀")
else:
    # When there is no error
    print(f"Division was successful. ✅")
finally:
    # Always goes in here regardless of whether the was an error or not
    print(f"Operation done!! ✌️✌️")
