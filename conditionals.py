# person1 = input("Please give your name? ")
# height1 = float(input("Please enter your height in cm "))
# person2 = input("Please give your name? ")
# height2 = float(input("Please enter your height in cm "))

# if (height1 > height2):
#   print(f"{person1} is taller than {person2}")
# elif (height1 == height2):
#   print(f"{person2} and {person1} are of same height")
# else:
#   print(f"{person2} is taller than {person1}")

#Ice cream One
#Task 1
shop_stock = "vanilla, lime, chocolate"
ice_cream = input("What ice cream would you like? ")
# if ice_cream in shop_stock:
#   print("Yes, we have it in stock")
# else:
#   print("No, we ran out of stock")

stock1 = "vanilla"
stock2 = "lime"
stock3 = "chocolate"

# #Task 2
# ice_cream = input("What ice cream would you like? ")
# if ice_cream == stock1:
#   print("Yes, we have it in stock")
# elif ice_cream == stock2:
#   print("Yes, we have it in stock")
# elif ice_cream == stock3:
#   print("Yes, we have it in stock")
# else:
#   print("No, we ran out of stock")

#Third way
# if ice_cream in (stock1, stock2, stock3):
#   print("Yes, we have it in stock")
# else:
#   print("No, we ran out of stock")

y = "Yes, we have it in stock" if (
    ice_cream in shop_stock) else "No, we ran out of stock"
print(y)
