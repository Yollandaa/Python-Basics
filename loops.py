# i = 0

# while i < 3:
#   print(i)
#   i = i + 1

# i  i < 3  print(i)
# 0  True   0
# 1  True   1
# 2  True   2
# 3  False  3

#😍
#😍😍
#😍😍😍
#😍😍😍😍

num = int(input("How many rows would you like? "))
i = 0
while i < num:
  print("😍" * (i+1))
  i = i+1
  
print()

#Same thing using for loop
#Range does not include the last number: rangle(1,3) -> 1 2

for curr in range(1,num+1):
  print("😍" * (curr))

#Task:
player_stats = [10, 30, 60]
stats_copy = player_stats[:]
for i in range(len(stats_copy)):
  #stats_copy[i] = stats_copy[i]*2
  stats_copy[i] *= 2
print(player_stats, stats_copy)

#Double all my stat for each stat present in player_stats
powered_up_stats = [stat * 2 for stat in player_stats]
print(powered_up_stats)

print()


avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

for ave in avengers:
  print(f"{ave} has {len(ave)} characters")

#To create the list of num characters
numing = [len(ave) for ave in avengers]
print(numing)

#acreate list Names of those with more than 10 characters
more_than_ten = [ave.upper() for ave in avengers if len(ave) > 10]
print(more_than_ten)
