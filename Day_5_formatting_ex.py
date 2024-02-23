recipe = {
  "name": "Spaghetti Carbonara",
  "servings": 4,
  "ingredients": ["200g spaghetti", "100g pancetta", "2 eggs", "1/2 cup grated Parmesan", "1 clove garlic"]
}

# Out should be as below.
# Task 1
# ======= Spaghetti Carbonara =======
# - 200g spaghetti
# - 100g pancetta
# - 2 eggs
# - 1/2 cup grated Parmesan
# - 1 clove garlic
# Serves: 4 people

print(f"{recipe['name']:=^33}")
for ingredient in recipe["ingredients"]:
  print(f"- {ingredient}")
print(f"Serves: {recipe['servings']} people")


print()
# Task 2:
from datetime import datetime

guests = ["Alice", "Bob", "Charlie"]
party_date = datetime(2024, 3, 14)
# Output should be as below.
# *       Alice       *
# You are invited to the party on March 14, 2024!
# *        Bob        *
# You are invited to the party on March 14, 2024!
# *      Charlie      *
# You are invited to the party on March 14, 2024!

for guest in guests:
  print(f"*{guest:^19}*")
  print(f"You are invited to the party on {party_date:%B %d, %Y}!")

about_me = """
Hi, My name is Caleb
I am from CPT"""
print(about_me)