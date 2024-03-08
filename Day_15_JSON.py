import json
from pprint import pprint

data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Sales"},
    ]
}

print(type(data))
print(data["employees"][0]["age"])

data_json = json.dumps(data, indent=4)

print(data_json, type(data_json))

# JSON -> JavaScript Oject Notation -> A string representation
# This returns an error
# print(data_json["employees"][0]["age"])

# First-Class Function -> Function is being treated as a variable
sport = {"name": "Dhoni", "dbl": lambda x: x * 2}
print(sport["dbl"]([2, 3, 4]))

# This won't work "TypeError: Object of type function is not JSON serializable (conversion to string)" -> Can't convert dictionary to string bcz it contains a function
# print(json.dumps(sport))

# This converts the json back to dictionary
back_to_dict = json.loads(data_json)
pprint(back_to_dict)

print()
print()


bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""
# Task 1
# All active users the balance should increase by 10% - Final output should be in json format

bank_data_dict = json.loads(bank_data)
# pprint(bank_data_dict)

# for bank_data in bank_data_dict:
#     if bank_data["isActive"]:
#         bank_data["balance"] += bank_data["balance"] * 0.1

# # print as json
# print(json.dumps(bank_data_dict, indent=4))

# Task 2: List comprehension way

# This only returns the modified onees
# bank_dict = [
#     {**bank_data, "balance": bank_data["balance"] * 1.1}
#     for bank_data in bank_data_dict
#     if bank_data["isActive"]
# ]


# bank_dict = [
#     (bank_data if not bank_data["isActive"] else {**bank_data, "balance": bank_data["balance"] * 1.1}) for bank_data in bank_data_dict
# ]

bank_dict1 = [
    (
        {**bank_data, "balance": bank_data["balance"] * 1.1}
        if bank_data["isActive"]
        else bank_data
    )
    for bank_data in bank_data_dict
]
print(json.dumps(bank_dict1, indent=4))

# Write a file
# If any error happens with will silently exit/error out
with open("bank_accounts.json", "w") as file:
    json.dump(bank_dict1, file, indent=4)

# Read a file
with open("bank_accounts.json", "r") as file:
    data = json.load(file)
    print(data)
