#1
num = int(input("Enter number: "))

if 1 <= num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is not between 1 and 100")

#2
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3
num = int(input("Enter month number (1-12): "))

months = {1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"}

if num in months:
    print(months[num])
else:
    print("Invalid month number")

#4
marks = int(input("Enter marks: "))

if marks < 25:
    print("F")
elif marks <= 45:
    print("E")
elif marks <= 50:
    print("D")
elif marks <= 60:
    print("C")
elif marks <= 80:
    print("B")
else:
    print("A")

#5
num = int(input("Enter number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

 #6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print("Answer:", a + b)
elif op == "-":
    print("Answer:", a - b)
elif op == "*":
    print("Answer:", a * b)
elif op == "/":
    print("Answer:", a / b)
else:
    print("Invalid operator")

 #7
salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))

if salary >= 50000 and credit >= 700:
    print("Eligible")
else:
    print("Not Eligible")

#8       
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(num)

#9
ch = input("Enter character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#10
marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    print("A")
elif 80 <= marks <= 89:
    print("B")
elif 70 <= marks <= 79:
    print("C")
else:
    print("Fail")

#11
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

#12
ch = input("Enter character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

 #13
color = input("Enter color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

#14
age = int(input("Enter age: "))
experience = int(input("Enter experience in years: "))

if age > 18 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")

#15
temp = int(input("Enter temperature: "))

if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

#16
item = input("Enter item (Pizza/Burger/Pasta): ").lower()

if item == "pizza":
    print("$10")
elif item == "burger":
    print("$7")
elif item == "pasta":
    print("$8")
else:
    print("Item not available")

#17
height = float(input("Enter height in feet: "))

if height >= 6:
    print("Selected")
else:
    print("Not Selected")

#18
age = int(input("Enter age: "))

if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")

#19
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")

#20

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month")           
                                   