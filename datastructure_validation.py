# 1. 
students = { "Ram": "ram@gmail.com","Sita": "sita@gmail.com","Laxman": "laxman@gmail.com"}
name = input("Enter student name: ")
if name in students:
    print("Email:", students[name])
else:
    print("Contact not found")


 #2 
shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}
remaining = shopping_list - bought
if remaining:
    print("Unbought items:", remaining)
else:
    print("Shopping complete")

#3
class_list = ["ram", "sita", "laxman"]
new_student = input("Enter new student name: ")
if new_student not in class_list:
    class_list.append(new_student)
    print("Student added successfully")
else:
    print("Student already present")
print("Updated class list:", class_list)


#4
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
count_blue = votes.count("Blue")
print("Blue count:", count_blue)
if count_blue >= 3:
    print("Blue wins")
else:
    print("Blue did not win")


#5
grades = {"Ram": 92,"Sita": 88}
student = input("Enter student name: ")
if student in grades:
    print("Grade:", grades[student])
else:
    print("Grade is not available")


#6
applicant = { "name": "Priya", "skills": ["Java", "SQL"], "experience_years": 1}
required_skills = {"Python", "Java"}
# Check conditions
has_skill = any(skill in required_skills for skill in applicant["skills"])
has_experience = applicant["experience_years"] >= 2
if has_skill and has_experience:
    print("Priya qualifies")
else:
    print("Priya does not qualify")


#7
banned_items = {"scissors", "knife", "lighter"}
# User input
weight = float(input("Enter baggage weight: "))
item = input("Enter item name: ").lower()
# Check conditions
if weight <= 7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")


#8
sample_dict = {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},
                  'emp3': {'name': 'Shyam', 'salary': 500}}
# Change salary
sample_dict['emp3']['salary'] = 8500
print (sample_dict)


#9
# Sets of items
ram = {"pen", "book", "bag"}
laxman = {"copy", "bag", "pencil"}

# Check common items
if ram.isdisjoint(laxman):
    print("They picked completely different items")
else:
    print("They have some common items")


#10
# Data Initialization
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {40, 50, 60}
my_dict = {'a': 10, 'b': 20, 'c': 30}
val = 20
# Step 1: Universal Validity Check
if val in my_list and val in my_tuple:

    # Step 2 & 3: Zone & Revocation Check
    if 'b' in my_dict and val not in my_set:
        print("Path A")
        
    else:
        print("Path B")

else:
    print("Path C")


#16
menu = {"Pizza": 15,"Burger": 10,"Salad": 8}

order = "Pizza"

if order in menu:
    print("Price =", menu[order])
else:
    print("Item not found")


#17
student_data = {"name": "Sam", "score": 85}
if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)


#18
database = {"admin": "1234","user": "abcd"}
# Define two variables
user_input = "admin"
user_pass = "1234"

# Check login
if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed") 

#19
emails = ["ram123@gmail.com", "hari77@gmail.com"]
blacklisted_emails = {"hari77@gmail.com"}
current_email = "hari77@test.com"
# Check conditions
if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")


#20
inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'

if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")
else:
    print("invalid zone")
    

#21
valid_courses = {"python", "robotics", "java"}
hs_grades = [9, 10, 11, 12]

# Take input
name = input("Enter student name: ")
course = input("Enter course: ")
grade = int(input("Enter grade: "))

# Store in dictionary
student_records = {"name": name,"course": course,"grade": grade}
# Check course
if course not in valid_courses:
    print(name, "selected an invalid course.")

else:
    # Check grade range
    if grade < 9:
        print("grade too low")

    elif grade > 12:
        print("grade too high")

    else:
        # Robotics rule
        if course == "robotics" and grade == 9:
            print(name, "is not eligible for", course, "grade too low")

        else:
            print(name, "is approved for", course)     