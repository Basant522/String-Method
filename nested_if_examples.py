#1
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))

if age >= 12:
    if height >= 140:
        print("You can ride the roller coaster")
    else:
        print("You are not tall enough")
else:
    print("You are too young")

#2
color = input("Enter color (red/yellow/green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

#3
 num = int(input("Enter number (1-4): "))

if num == 1:
    print("Spring")
elif num == 2:
    print("Summer")
elif num == 3:
    print("Autumn")
elif num == 4:
    print("Winter")
else:
    print("Unknown")

#4
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "pass123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")  

 #5
age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if 21 <= age <= 60:
    if income >= 30000:
        if credit >= 700:
            print("Loan Approved")
        else:
            print("Rejected: Low credit score")
    else:
        print("Rejected: Low income")
else:
    print("Rejected: Age not eligible")

 #6
age = int(input("Enter age: "))
member = input("Membership (yes/no): ").lower()

if age < 12:
    price = 0
elif 12 <= age <= 60:
    if member == "yes":
        price = 150
    else:
        price = 200
else:
    price = 100

print("Ticket price:", price)

#7
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
else:
    bonus = 0

print("Bonus:", bonus)

#8
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area:", area)

#9
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

wage = 0

if 18 <= age < 30:
    if gender == "M":
        wage = 700
    else:
        wage = 750
elif 30 <= age <= 40:
    if gender == "M":
        wage = 800
    else:
        wage = 850

total = wage * days
print("Total wages:", total)

#10
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)