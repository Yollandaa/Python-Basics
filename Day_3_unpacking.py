movies = ["Remeber the Titans", "Juno", "Lucy"]
caleb, gemma, yolanda = movies
t1, t2, _, *t3 = (20, 30, 10, 40, 50) #Toomany values to unpack
print(t1, t2, type(t3))

# From origin (0,0) how far is the point
coordinates = [(5,4), (1,1), (6,10), (9,10)]
distances = []
for x,y in coordinates:
  distance = (x**2 + y**2)**0.5
  distances.append(distance)  
print(distances)

#Task 2
#Use unpacking and list comprehension for calculating the distance
c1, c2, c3, c4 = coordinates #Unpacked
dist1 = (c1[0]**2 + c1[1]**2)**0.5
dist2 = (c2[0]**2 + c2[1]**2)**0.5 
dist3 = (c3[0]**2 + c3[1]**2)**0.5
dist4 = (c4[0]**2 + c4[1]**2)**0.5
print(dist1, dist2, dist3, dist4)


#List comprehension
dist1 = [((x**2 + y**2)**0.5) for x,y in coordinates]
print(dist1)



