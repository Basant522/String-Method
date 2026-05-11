# 1. Final Outputs

# a) i=3, j=5, k=7
(5,5,7)

# b) i=-2, j=-5, k=9
(9,-5,9)

# c) i=8, j=15, k=12
(12,15,12)

# d) i=13, j=15, k=13
(15,15,13)

# e) i=3, j=5, k=17
(5,5,7)

# f) i=25, j=15, k=17
(25,25,17)



# 2(a)
(3,5,3)

# 2(b)
(-2,-2,9)

# 2(c)
(15,15,12)

# 2(d)
(15,15,13)

# 2(e)
(3,5,3)

# 2(f)
(25,25,17)


# 3(a)
(5, 5, 7)

# 3(b)
(-5,-5, 9)

# 3(c)
(15,15,12)

# 3(d)
(13,15,13)

# 3(e)
(5,5,17)

# 3(f)
(25,15,25)

#4
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")

elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")

else:
    print("Invalid Credentials. Please try again.")


#5
total_purchase_amount = float(input("Enter total purchase amount: "))

if total_purchase_amount > 5000:
    membership = input("Do you have a membership card? (yes/no): ").lower()

    if membership == "yes":
        discount = total_purchase_amount * 0.30
        final_bill = total_purchase_amount - discount

        print("Discount:", discount)
        print("Final Bill:", final_bill)

    else:
        print("Final Bill (No Discount):", total_purchase_amount)

else:
    print("Final Bill (No Discount):", total_purchase_amount)



#6
rint("Welcome to the Magic Forest")

# Stage 1
direction = input("Go north or south? ").lower()

if direction == "north":

    # Stage 2
    choice = input("Cross the river or follow the path? ").lower()

    if choice == "cross the river":
        print("Cross the River. End.")

    elif choice == "follow the path":

        # Stage 3
        character = input("Choose Fairy, Ogre, or Elf: ").lower()

        if character == "elf":
            print("YOU WIN")

        elif character == "fairy":
            print("GAME OVER")

        elif character == "ogre":
            print("GAME OVER")

        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

else:
    print("GAME OVER")

#7 Traffic Light System

light = input("Enter traffic light color: ").lower()

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic light color")


# 8. Season Finder

num = int(input("Enter a number (1-4): "))

match num:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Unknown")


# 9. Bank Loan Approval System

age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

if 21 <= age <= 60 and income >= 30000 and credit_score >= 700:
    print("Loan Approved")
else:
    print("Loan Not Approved")

    if not (21 <= age <= 60):
        print("Age condition failed")

    if income < 30000:
        print("Income condition failed")

    if credit_score < 700:
        print("Credit score condition failed")

# 10. BMI Calculator Program

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi <= 25:
    status = "Normal weight"
elif bmi <= 30:
    status = "Overweight"
else:
    status = "Obese"

print("Weight:", weight)
print("Height:", height)
print("BMI:", round(bmi, 1), status)


# 11. Movie Ticket Booking System

age = int(input("Enter age: "))

if age < 12:
    price = 0

elif age <= 60:
    member = input("Do you have membership card? (yes/no): ")

    if member == "yes":
        price = 150
    else:
        price = 200

else:
    price = 100

print("Ticket price is Rs.", price)


# 12. Employee Bonus Program
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
else:
    bonus = 0

print("Net bonus amount =", bonus)


#13
radius = float(input("Enter the radius of circle: "))

area = 3.14 * radius * radius

print("The area of circle is =", area)


# 14. Wages according to age and gender

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

if age >= 18 and age < 30:
    if gender == 'M':
        wage = 700
    else:
        wage = 750

elif age >= 30 and age <= 40:
    if gender == 'M':
        wage = 800
    else:
        wage = 850

else:
    print("Invalid age")
    exit()

total = wage * days

print("Wage per day =", wage)
print("Total wage =", total)


# 15. Fizz Buzz Program

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print(num)


# 16. Electricity Bill Calculator
units = int(input("Enter electricity units: "))

if units < 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 8)

else:
    bill = (100 * 5) + (200 * 8) + ((units - 300) * 10)

print("Total Bill = Rs", bill)


# 17. Rock Paper Scissors Game

player1 = input("Player 1 enter rock/paper/scissors: ").lower()
player2 = input("Player 2 enter rock/paper/scissors: ").lower()

if player1 == player2:
    print("It's a tie!")

elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):

    print("Player 1 wins!")

else:
    print("Player 2 wins!")


#18
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

else:
    print("Not positive")


#19
total_amount = float(input("Enter total amount: "))
is_member = input("Are you a member (True/False): ")

if total_amount > 1000 and is_member == "True":
    final_amount = total_amount - (total_amount * 0.20)
    print("20% discount applied")
    print("Final amount =", final_amount)

elif total_amount > 1000 and is_member == "False":
    final_amount = total_amount - (total_amount * 0.10)
    print("10% discount applied")
    print("Final amount =", final_amount)

else:
    print("No discount")
    print("Final amount =", total_amount)


#20
earth_weight = float(input("Enter Earth weight: "))
planet = int(input("Enter planet number (1-7): "))

if planet == 1:
    gravity = 0.38
    name = "Mercury"

elif planet == 2:
    gravity = 0.91
    name = "Venus"

elif planet == 3:
    gravity = 0.38
    name = "Mars"

elif planet == 4:
    gravity = 2.53
    name = "Jupiter"

elif planet == 5:
    gravity = 1.07
    name = "Saturn"

elif planet == 6:
    gravity = 0.89
    name = "Uranus"

elif planet == 7:
    gravity = 1.14
    name = "Neptune"

else:
    print("Invalid planet number")
    exit()

destination_weight = earth_weight * gravity

print("Your weight on", name, "is", destination_weight)


#21
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

total = m1 + m2 + m3 + m4
percentage = total / 4

print("Total marks =", total)
print("Percentage =", percentage)

if percentage > 70:
    print("Grade: Distinction")

elif percentage > 60:
    print("Grade: First")

elif percentage > 40:
    print("Grade: Pass")

else:
    print("Grade: Fail")


#22 Simple ATM Program

is_valid = True
balance = 5000
correct_pin = 123

if is_valid == True:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:

        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance = balance - amount
                print("Withdrawal successful")
                print("Remaining balance =", balance)

            else:
                print("Insufficient balance")

        elif choice == 2:
            print("Current balance =", balance)

        elif choice == 3:
            print("Thank you for visiting")

        else:
            print("Invalid option")

    else:
        print("Wrong PIN")

else:
    print("Card is invalid")

#23 Elevator Logic Program

target_floor = int(input("Enter target floor (0-10): "))
weight = float(input("Enter total weight in kg: "))
door_status = input("Enter door status (open/closed): ").lower()

# Floor validation
if target_floor < 0 or target_floor > 10:
    print("INVALID FLOOR")

# Weight validation
elif weight > 500:
    print("OVERWEIGHT: LIFT CANNOT MOVE")

# Door validation
elif door_status == "open":
    print("WARNING: CLOSE THE DOOR")

 # All conditions satisfied
else:
    print("ACTIVATE ELEVATOR MOTION")

#24    
print("=== Facebook Sign Up Validation ===")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email: ")
re_email = input("Re-enter email: ")
password = input("Enter password: ")

if (first_name.isalpha() and first_name != "" and
    last_name.isalpha() and last_name != "" and
    "@" in email and "." in email and
    email == re_email and
    len(password) >= 6):

    print("Sign Up Successful")
else:
    print("Invalid Details")
