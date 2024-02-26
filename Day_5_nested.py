from pprint import pprint

classes = {
    "Class A": [{
        "name": "Alice",
        "grades": [82, 90, 88]
    }, {
        "name": "Bob",
        "grades": [78, 81, 86]
    }, {
        "name": "Charlie",
        "grades": [85, 85, 87]
    }],
    "Class B": [{
        "name": "Dave",
        "grades": [92, 93, 88]
    }, {
        "name": "Eve",
        "grades": [76, 88, 91]
    }, {
        "name": "Frank",
        "grades": [88, 90, 92]
    }]
}

def find_avg(nums):
  return sum(nums)/len(nums)
# Find average of each class
# Task 1 - 5mins
#output = {"Class A": 82.53, "Class B": 85.5}

# Get the average of all the students' grades combined
output = {}
for class_name, students in classes.items():
  total_grades = []
  for student in students:
    # total_grades.extend(student["grades"])
    total_grades += student["grades"]
  output[class_name] = {find_avg(total_grades)}
pprint(output)

# Task 2
# output = {
#     "Class A": {
#         "Alice": 90.5,
#         "Bob": 84.5,
#         "Charlie": 90
#     },
#     "Class B": {
#         "Dave": 92.5,
#         "Eve": 86.5,
#         "Frank": 95
#     }
# }
# Get average of each student: Each student should have own average, under their class
print()
# I want a dictionary with classes, within each class I get the average of each student
student_average = {}
for class_name, students in classes.items():
    student_average[class_name] = {}
    for student in students:
        student_average[class_name][student["name"]] = find_avg(student["grades"])
pprint(student_average)

print()

# Task 3: Task 1 + List comprehension
classes_avg = {}
for class_name, students in classes.items():
  total_grades = [find_avg(student['grades']) for student in students]
  classes_avg[class_name] = find_avg(total_grades)
pprint(classes_avg)


# With a dictionary comprehension
classes_avg1 = {class_name: find_avg([find_avg(student['grades']) for student in students]) for class_name, students in classes.items() }
pprint(classes_avg1)

# Task 2: with comprehension
# students_avg_dict = {}
# for cls_name, students in classes.items():
#   students_dict = {}
#   for student in students:
#     students_dict[student['name']] = find_avg(student['grades'])
#   students_avg_dict[cls_name] = students_dict
# pprint(students_avg_dict)
print()
# Nested comprehension of the above 
students_avg_dict = {cls_name: {student['name']: find_avg(student['grades']) for student in students} for cls_name, students in classes.items()}
pprint(students_avg_dict)