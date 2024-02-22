# String, List, Tuple, Dictionary, Sets
# Sets are like lists since they are mutable.

# {}
tech_gadgets = {'smartphone', 'laptop', 'Smartwatch', 'Tablet', 'Tablet'}
tech_gadgets_list = ['smartphone', 'laptop', 'Smartwatch', 'Tablet', 'Tablet']
print(tech_gadgets)
print(tech_gadgets_list)

print()

tech_gadgets.add("E-reader")  # Order is not guaranteed
print(tech_gadgets)

print()
more_gadgets = {'Drone', 'Selfiestick'}
tech_gadgets.update(more_gadgets)
print(tech_gadgets)

tech_gadgets.discard('pile')
empty_set = set()
#tech_gadgets.remove('pile') #Avoid using remove since it gives an error if the item is not present
print(tech_gadgets.discard('pile'))

outdoor_activities = {"Hiking", "Cycling", "Swimming"}
indoor_activities = {"Gaming", "Reading", "Cycling"}

print(indoor_activities.intersection(outdoor_activities))  #Cycling
print(indoor_activities.union(outdoor_activities))

print(outdoor_activities.difference(indoor_activities))  #
print(indoor_activities.difference(outdoor_activities))  # {Gaming, cycling}
print(indoor_activities.symmetric_difference(outdoor_activities))

print()

colours = ["red", "blue", 'red', "green", "pink", "blue"]
#output: ["red", "blue", "green", "pink"]
# Easy way
print(list(set(colours)))

# Long way
unique_colours = set()
for colour in colours:
  unique_colours.add(colour)
print(unique_colours)

print()

outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# Task 1
# Which are outdoor_gadgets ? 
# {'Smartwatch',  'Drone'}
outdoor_gadgets = set()
for key, value in activity_gadgets.items():
  if value in outdoor_activities:
    outdoor_gadgets.add(key)
print(outdoor_gadgets)

#List comprehension way
outdoor_gadgets1 = {key for key, value in activity_gadgets.items() if value in outdoor_activities}
print(outdoor_gadgets1)

# Task 2
# # Which are indoor_gadgets ?
indoor_gadgets = set()
for key, value in activity_gadgets.items():
  if value in indoor_activities:
    indoor_gadgets.add(key)
print(indoor_gadgets)

# List comprehension way
indoor_gadgets1 = {key for key, value in activity_gadgets.items() if value in indoor_activities}
print(indoor_gadgets1)


print()

# Task 3 - DRY | Concept of today: Today's concept is functions
def get_gadgets(gadgets, activities):
  return  {key for key, value in gadgets.items() if value in activities}

print("Outdoor gadgets: ", get_gadgets(activity_gadgets, outdoor_activities))
print("Indoor gadgets: ", get_gadgets(activity_gadgets, indoor_activities))

print()

d


