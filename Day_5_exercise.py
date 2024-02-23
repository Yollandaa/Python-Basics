# Exercise: Event Registration System
# Objective: Write a Python program that includes a function to register participants for an event. The registration function should handle participant details and their preferences with default values for some parameters.
# Initial Setup
# Participants need to provide their name and email. Additionally, they can specify their meal preference (vegetarian or non-vegetarian) and if they need accommodation. By default, the meal preference should be set to "non-vegetarian", and accommodation required should be False.
participants = [{"name": "Lilian" , "email": "tzirw@example.com", "meal_preference": "non-vegetarian", "accommodation_required": True},
                       {"name": "Caleb" , "email": "caleb@gmail.com", "meal_preference": "Hallal", "accommodation_required": False},
                       {"name": "Quinlan" , "email": "quinlan@gmail.com", "meal_preference": "vegetarian", "accommodation_required": False}]

# Task
# Registration Function: Write a function register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False) that registers a participant with their provided details and preferences.
# Display Registered Participants: After registration, display the participant's details, including their name, email, meal preference, and accommodation needs.
def register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False):
  participant = {"name": name, "email": email, "meal_preference": meal_preference, "accommodation": needs_accommodation}
  participants.append(participant)

register_participant(name="Uya", email="uya@gmail.com", meal_preference="vegetarian", needs_accommodation=True)
print(participants)
print()

register_participant("Dave", "dave@gmail.com")
print(participants)
print()
# Expected Functionality
# Registering a participant with all details specified.
# Registering a participant with only the name and email, using default values for the other parameters


classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}

# Task 1: Find average of each class
# Expected output: output = {"Class A": 82.53,"Class B": 85.5}
output = {}
for class_name, students in classes.items():
  for student in students:
    output[class_name] = sum(student["grades"]) / len(student["grades"])
print(output)

# Task 2: