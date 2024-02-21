person = {
  "name": "Siya Kolisi",
  "age": 32,
  "address": {
    "city": "Port Elizabeth",
    "country": "South Africa",
  },
  "stats": {
    "points": 50
  },
  "height": 186,
  "sport": "Ruby"
}

print(person)

person["age"] += 1
print(person)

#Methods 
print(person.keys(), type(person.keys()))
print(person.items())

print()

for key, value in person.items():
  print(key, value)

print(person.get('height')) #Returns none when height key wasn't added
print(person.get('height', 175))
#Get the city value
print(person.get('address').get('city'))
print(person['address']['city'])

# If stats doesn't exist, set default value of empty dictionary
print(person.get('stats', {}).get('points'))

# Dictionary comprehension
nums = {x:x for x in range(10)}
print(nums)