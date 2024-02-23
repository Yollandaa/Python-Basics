marks = [98, 75, 40, 45, 80, 60]
# marks.pop()
# marks.pop()
# marks.pop()
# Remove last K elements: marks[:-K]
# Remove first K elements: marks[:K]
print(marks[:-3])
print(marks.remove(40))
print(marks.append(20))
print(marks)

sci = 85
marks.insert(2, sci)

print(marks)

price_list1 = [1000, 1500, 400]
price_list2 = [2000, 500]
new_list = price_list1 + price_list2
#price_list1 and price_list2 are not changed
print(new_list)

coppp = new_list.copy()
coppppp3 = new_list[:]
print(coppppp3.append(10))
print(new_list, coppppp3)


print(new_list)

subjects = ["math", "science", "english", "history"]
print(", ".join(subjects))
subjects.sort(reverse = True)
print(subjects)