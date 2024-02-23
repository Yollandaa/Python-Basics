msg = "Hi, all"
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())

msg1 = "    Dream is not something that you see in sleep, Dream is something that does not let you sleep.    "
print(msg1.strip())  # Removes extra spaces at start and end
# msg1 = "----Dream is not something that you see in sleep, Dream is something that does not let you sleep.---"

print(msg1.strip("-"))

print(msg1.startswith("Dream"))

num = "45445"
print(num.isdigit())

# print(msg1.find("something")) #Returns index of the first match.
# print(msg1.find("something", 20))

#After the key that is your secret codde
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

index = message.find("🔑")
output = message[index + 1:].upper()

#The find() method returns -1 if the value is not found.
if (index == -1):
  print("No secret key is present")
elif (output == code):
  print("You are a hacker 🎊")
else:
  print("Try again")

# Task 2: What if the key is not present
# Task 3: What is there is a secret key but they hide it more with some junk
message = "    🚨🔍📱🔑*****secret_code✌️((("
code = "SECRET_CODE✌️"

index = message.find("🔑")
output = message[index + 1:].strip("*")
output = output.strip("(").upper()

print(output)
if (index == -1):
  print("No secret key is present")
elif (output == code):
  print("You are a hacker 🎊")
else:
  print("Try again")
