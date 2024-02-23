from datetime import datetime
salary = 420_000_00
print(salary)

#Float
print(f"Dhars's salary R{salary:,}")
print(f"Dhars's salary R{salary:.2f}")
print(f"Dhars's salary R{round(salary)}")

# Text
name = "Lilitha"
print(f"{name:>20}")
print(f"{name:<20}")
print(f"{name:^20}")

print(f"{name:*>20}")
print(f"{name:#<20}")
print(f"{name:$^20}")

caleb = 0.925
print(f"The test results are not {caleb:.2%} ")

# Date time
now = datetime.now()
print(now)
print(f"The current day is {now:%Y-%M-%D}")
print(f"The current day is {now:%d/%m/%Y}")
print(f"The current day is {now:%H:%M:%S}")
#print(f"The current day is {now:%%DD")