books = [
  {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
  {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
  {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
  {"title": "Sapiens", "rating": 4.9, "genre": "History"},
  {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]


# Task 1: Books that are highly rated, rating of 4.7 or higher
# Expected output: ['A Brief History of Time', 'Clean Code', 'Sapiens']
highly_rated = []
for book in books:
  if book["rating"] >= 4.7:
    highly_rated.append(book["title"])    
print(highly_rated)

# Task 2: List comprehension
high_rate = [book["title"] for book in books if book["rating"] >= 4.7]
print(high_rate)

# Task 3: Ascending order
#high_rate.sort() #Can use sorted() as it returns a new sorted array
print(sorted(high_rate))

print()
# Input:
# What is the product name?
# What is the quantity?
# What is the price?

inventory = [

  {"name": "Apple", "quantity": 30, "price": 0.50},

  {"name": "Banana", "quantity": 20, "price": 0.20},

  {"name": "Orange", "quantity": 10, "price": 0.60}

]

# Task 1: Allows duplicate products
# product_name = input("What is the product name? ")
# quantity = int(input("What is the quantity? "))
# price = float(input("What is the price? "))

#ew_product = {"name": "Orange", "quantity": 10, "price": 0.60}
# new_product = {"name": product_name, "quantity": quantity, "price": price}
# inventory.append(new_product)
# print(inventory)


# Task 2: If they enter a product name that already exists, update the quantity (old quantity + new quantity) and price (use the new one)

# new_product = {"name": product_name, "quantity": quantity, "price": price}

# Check if product exists in the list
# Only add if it doesn't exist
# if (new_product["name"] in [product["name"] for product in inventory]):
#   #Only Update the price and quantity when 
#   for product in inventory:
#     if product["name"] == new_product["name"]:
#       product["quantity"] += new_product["quantity"]
#       product["price"] = new_product["price"]  
# else:
#   inventory.append(new_product)
# print(inventory)

# We can avoid thhe first if statement and start on the for loop but add a break after adding/updating the product

print()

# Easier way:
# item_found = False
# for item in inventory:
#   if (item["name"] == product_name):
#     item["quantity"] += new_product["quantity"]
#     item["price"] = new_product["price"] 
#     item_found = True
#     break

# if item_found == False:
#   inventory.append(new_product)
# print(inventory)


guests = [
  {"name": "Alice", "age": 25, "code": "VIP123"},
  {"name": "Bob", "age": 17, "code": "VIP123"},
  {"name": "Charlie", "age": 30, "code": "VIP123"},
  {"name": "Dave", "age": 22, "code": "GUEST"},
  {"name": "Eve", "age": 29, "code": "VIP123"}
]

blacklist = ["Dave", "Eve"]


# Output
# People who are 21 or above and VIP123
# Blacklist are not allowed

# ["Alice", "Charlie"]
allowed = []
for guest in guests:
  if (guest["age"] >= 21 and guest["code"] == "VIP123") and guest["name"] not in blacklist:
    allowed.append(guest["name"])
print(allowed)

#Another approach
guest_list = [guest['name'] for guest in guests if guest["age"] >= 21 and guest["code"] == "VIP123" and guest["name"] not in blacklist]
print(guest_list)

# Update experience by 1
employees = [
  {"name": "Alex", "experience": 2},
  {"name": "Gemma"},
  {"name": "Rashay", "experience": 4},
  {"name": "Thato"}
]

# Task 1: +1 to experience
# for employee in employees:
#   if "experience" in employee:
#     employee["experience"] += 1
#   else:
#     employee["experience"] = 1

# Task 2 & 3: Using .get() and adding status
# Senior 5 or more, Mid-Level 3 to 5, Junior < 3
for employee in employees:
  employee["experience"] = employee.get('experience', 0) + 1
  if (employee["experience"] >= 5):
    employee["status"] = "Senior"
  elif (employee["experience"] >= 3):
    employee["status"] = "Mid-Level"
  else:
    employee["status"] = "Junior"
print(employees)

#Copy dictionaries:
movie = {
  "name": "Mr Bones",
  "year": 2001
}
print()
# Unpacking operator * -> List | ** - Dictionaries
movie_copy1 = movie.copy()
movie_copy11 = {**movie}

movie_copy2 = {**movie, "rating": 10}
print()
print(movie_copy2)
print(movie)

# The right most value replaces the left most value if the key already exists.
movie_copy3 =  {**movie, "rating": 10, "year": 2002} #This one replaced 2001 with 2002
print()
print(movie_copy3)
print(movie)

movie_copy4 =  {"rating": 10, "year": 2002, **movie} #This one remained 2001
print()
print(movie_copy4)
print(movie)


detail = {
  "actor": "leon schuster",
  "director": "Dzithendo"
}

movie_detail = {**movie, **detail}
print()
print(movie_detail)
print(movie)

print()
#Unpacking lists
price = [1000, 1200, 400]
price_copy = [*price]
price_copy1 = [50, 40, *price, 60]
print(price_copy)
print(price_copy1)

t1 = [80, 90]
t2 = [50, 60]
t3 = [*t1, *t2]
print(t3)
