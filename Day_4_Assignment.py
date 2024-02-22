
# Each room in the hotel is represented by a dictionary with keys for room_number, bed_type 
rooms = [
  {"room_number": 1, "bed_type": "Single", "smoking": False, "availability": True},
  {"room_number": 2, "bed_type": "Double", "smoking": True, "availability": False},
  {"room_number": 5, "bed_type": "Double", "smoking": False, "availability": True},
  {"room_number": 8, "bed_type": "Single", "smoking": False, "availability": True},
  {"room_number": 9, "bed_type": "Single", "smoking": True, "availability": False}]

# Task 1: Write a function add_room(rooms, room_number, bed_type="Double", smoking=False) that adds a new room to the hotel's inventory.
def add_room(rooms, room_number, bed_type="Double", smoking=False):
  new_room = {"room_number": room_number, "bed_type": bed_type, "smoking": smoking, "availability": True}
  rooms.append(new_room)
  return rooms

print(add_room(rooms, 10, "Queen", True))
# print()
print(add_room(rooms, 4, "Queen"))
# print()
print(add_room(rooms, 7))
# print()

# Task 2: Write a function book_room(rooms, preferred_bed_type="Double", smoking_preference=False) that books the first available room that matches the customer's preferences. If a room is booked, update its availability to False.
def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  for room in rooms:
    if (room["availability"]) and (smoking_preference == room["smoking"]) and (room["bed_type"] == preferred_bed_type):
      room["availability"] = False
      return f"Room {room['room_number']} has been booked successfully."
  return "Sorry, there are no rooms that match your preferences."

print(book_room(rooms, "Single", True))
print()
print(book_room(rooms, "Double", False))
print()
print(book_room(rooms))
print()

# Task 3: Write a function list_available_rooms(rooms) that prints all rooms currently available.
def list_available_rooms(rooms):
  return [room for room in rooms if room["availability"]]

print(list_available_rooms(rooms))
      

