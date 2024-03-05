from pprint import pprint

print(f"\n Question 1")
# Question 1: Sort by descending order and add rank position to dictionary
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
rank = 1
for student in sorted_students:
    student["rank"] = rank
    rank += 1
pprint(sorted_students)

print(f"\n Question 2")
# Question 2: Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]

merged_employees = []
for employee in employees:
    for salary in salaries:
        if employee["id"] == salary["id"]:
            merged_employees.append({**employee, **salary})
            break
pprint(merged_employees)

print(f"\n Question 3")
# Question 3: Filter the list to include only products in the "Electronics" category with a price less than 500.
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Get electronics first
electronic_products = filter(
    lambda product: product["category"] == "Electronics", products
)
with_price = filter(lambda product: product["price"] <= 500, electronic_products)
pprint(list(with_price))


print(f"\n Question 4")
# Question 4: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# A dictionary with product names as keys and total quantities as values.
names_quantity = {}
for order in orders:
    for item in order["items"]:
        if item["product"] in names_quantity:
            names_quantity[item["product"]] += item["quantity"]
        else:
            names_quantity[item["product"]] = item["quantity"]
pprint(names_quantity)


print(f"\n Question 5")
# Question 5: Summarize the total amount spent per category.
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
totals = {}
for transaction in transactions:
    if transaction["category"] in totals:
        totals[transaction["category"]] += transaction["amount"]
    else:
        totals[transaction["category"]] = transaction["amount"]
pprint(totals)

print(f"\n Question 6")
# Quesstion 6: Group sales by salesperson and calculate the total sales amount for each.
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
sales_total = {}
for sale in sales:
    if sale["salesperson"] in sales_total:
        sales_total[sale["salesperson"]] += sale["amount"]
    else:
        sales_total[sale["salesperson"]] = sale["amount"]
pprint(sales_total)

print(f"\n Question 7")
# Question 7: Sort the spells list by power level in descending order using a lambda function.
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
sorted_spells = sorted(spells, key=lambda x: x[1], reverse=True)
pprint(sorted_spells)

print(f"\n Question 8")
# Question 8: Use `map` to append ": 3 grams" to each ingredient.
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Output: ['Wolfsbane: 3 grams', 'Eye of Newt: 3 grams', 'Dragon Scale: 3 grams']
new_ingredients = map(lambda ingredient: ingredient + ": 3 grams", ingredients)
pprint(list(new_ingredients))

print(f"\n Question 9")
# Question 9: Filter books with more than 120 pages and format their titles to uppercase.
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# filter_books = filter(lambda book: book["pages"] >= 120, books)
# map_books = map(lambda book: book["title"].upper(), filter_books)
results = map(
    lambda book: book["title"].upper(), filter(lambda book: book["pages"] >= 120, books)
)
pprint(list(results))

print(f"\n Question 10")


# Question 10: Implement a class with methods for casting spells, reducing health points, and determining the winner.
# Expected Output: After a duel between Harry and Draco, Harry wins with 10 health points left.
class WizardDuel:
    def __init__(self, name, health_points):
        self.name = name
        self.health_points = health_points

    def cast_spell(self, spell):
        print(f"{self.name} casts {spell}")

    def reduce_points(self, points):
        self.health_points -= points
        print(f"{self.name} has {self.health_points} health points left.")

    def determine_winner(self):
        if self.health_points <= 0:
            print(f"{self.name} has died!")
        else:
            print(f"{self.name} has won!")


harry = WizardDuel("Harry", 20)
Draco = WizardDuel("Draco", 20)
# Attacks

harry.cast_spell("Lumos")
Draco.reduce_points(15)
Draco.cast_spell("Obliviate")
harry.reduce_points(10)
harry.cast_spell("Lumos")
Draco.reduce_points(15)
harry.determine_winner()

print("\n Question 11")


# Question 11: Define a `PotionError` exception and use it in a potion-making function.
# Create a custom exception to handle errors in potion making, such as using the wrong ingredient.
class PotionError(Exception):
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.message = " is not a valid ingredient for the Love Potion."
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ingredient} {self.message}"


love_potion_ingredients = [
    "rose petals",
    "chicory root",
    "jasmine",
    "dill",
    "hibiscus",
    "orange peels",
]
try:
    # ingredients = input("Please enter your love Potion main ingredient \n")
    ingredients = "Eye of Newt"
    if ingredients not in love_potion_ingredients:
        raise PotionError(ingredients)
except PotionError as e:  # Assign error to e | Making an alias
    print(e)

print(f"\n Question 12")
# Question 12: Use a list comprehension to select books written by Bathilda Bagshot.
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
bathilda_books = [book for book in library if book["author"] == "Bathilda Bagshot"]
pprint(bathilda_books)

print(f"\n Question 13")
# Question 13: Aggregate points for each house and print the total.
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]

points_total = {}
for house_point in house_points:
    if house_point["house"] in points_total:
        points_total[house_point["house"]] += house_point["points"]
    else:
        points_total[house_point["house"]] = house_point["points"]

pprint(points_total)

print(f"\n Question 14")


# Question 14: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.
# Expected Output: Calling sound() on a Dragon instance prints 'Roar', on a Unicorn instance prints 'Neigh'.
class MagicalCreature:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"A sound!")


class Dragon(MagicalCreature):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"Roar!")


class Unicorn(MagicalCreature):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"Neigh!")


uni = Unicorn("Lily")
drag = Dragon("Steve")
uni.sound()
drag.sound()

print(f"\n Question 15")
# Question 15: Sort the artifacts first by age, then by power, using a lambda function.
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
sorted_artifacts = sorted(artifacts, key=lambda x: ((x["age"]), (x["power"])))
pprint(sorted_artifacts)

print("\n Question 16")
# Question 16: Use an f-string to create a profile string that includes the wizard's name, title, and house.
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
pprint(f"{wizard['name']}, the {wizard['title']} of {wizard['house']}")

print("\n Question 17")
# Question 17: Use `filter` and `map` to create a list of matches between adopters and creatures.
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Output: [('Harry', 'Fawkes'), ('Hermione', 'Dobby')]

filtered = list(filter(lambda x: any(y[1] == x[1] for y in creatures), adopters))
result = list(
    map(lambda x: (x[0], next(y[0] for y in creatures if y[1] == x[1])), filtered)
)
pprint(result)

print(f"\n Question 18")
# Question 18: For each pair of ingredients, print out the unique potion they produce.


def potion_produced(p1, p2):
    if (p1 == "Silver Dust" and p2 == "Moonstone") or (
        p1 == "Moonstone" and p2 == "Silver Dust"
    ):
        return "Visibility Potion"
    if (p1 == "Moonstone" and p2 == "Dragon Blood") or (
        p1 == "Dragon Blood" and p2 == "Moonstone"
    ):
        return "Some Potion"
    if (p1 == "Silver Dust" and p2 == "Dragon Blood") or (
        p1 == "Dragon Blood" and p2 == "Silver Dust"
    ):
        return "Another one"


ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Output:** `Combining Moonstone and Silver Dust produces a Visibility Potion.`, etc., for all unique pairs.
for i in range(0, len(ingredients)):
    for j in range(0, len(ingredients)):
        if i != j:
            potion = potion_produced(ingredients[i], ingredients[j])
            print(f"Combining {ingredients[i]} and {ingredients[j]} produces {potion}")

print("\n Question 19")
# Question 19: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
]
for item in data:
    if "tag4" not in item["tags"]:
        item["tags"].append("tag4")
pprint(data)

print("\n Question 20")
# Question 20: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False},
]
sorted_tasks = sorted(tasks, key=lambda x: (x["completed"], x["priority"]))
pprint(sorted_tasks)
