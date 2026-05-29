
# 1. Even or Odd from 1 to 5

for i in range(1, 6):
    if i % 2 == 0:
        print("Number", i, "is even.")
    else:
        print("Number", i, "is odd.")

# 2. Sum of all elements in list

lst = [10, 20, 30, 40]
total = 0

for i in lst:
    total += i
    print("Added", i, "Running total is", total)

print("Total Sum:", total)

# 3. Personalized message

student_names = ["Ram", "Hari", "Sita"]

print("--- Email Greetings Generated ---")

for name in student_names:
    print(f"Hi {name}, your course approval is ready!")

# 4. Chapter page counts

pages = [45, 30, 50, 40]

print("--- Book Chapter Summary ---")

for i in range(len(pages)):
    print(f"Chapter {i+1} has {pages[i]} pages.")

# 5. Product of list elements

lst = [4, 5, 3, 2]
product = 1

for i in lst:
    product *= i

print("Product =", product)

# 6. Multiplication table of 11

num = 11

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 7. Reverse a list

lst = [3, 2, 1, 4, 5]

for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=" ")

# 8. Common elements in two lists

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

for i in list1:
    if i in list2:
        print(i)

# 9. Print 1 and 4 only

lst = [1,2,3,4]

for i in lst:
    if i == 1 or i == 4:
        print(i)

# 10. Remove vowels from a string

text = "programming"
vowels = "aeiou"
result = ""

for ch in text:
    if ch not in vowels:
        result += ch

print(result)

# 11. Count vowels and consonants

text = "Loops are Fun"

vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

# 12. Separate odd and even numbers

lst = [1,2,3,4,5]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)

# 13. Check prime number

num = 7
prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False
        break

if prime:
    print("Prime Number")
else:
    print("Not Prime")

# 14. Separate data types

lst = [1,2,3,4,"a","b"]

numbers = []
strings = []

for i in lst:
    if type(i) == int:
        numbers.append(i)
    else:
        strings.append(i)

print(numbers)
print(strings)

# 15. Count digits and letters

text = "Python123"

letters = 0
digits = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)

# 16. Username and password check

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# 17. Odd or Even

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 18. Factorial of a number

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# 19. Multiplication tables from 1 to 8

for n in range(1, 9):
    print("Table of", n)

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

    print()

# 20. Print 1 and 2 only

lst = [1,2,3,4]

for i in lst:
    if i == 1 or i == 2:
        print(i)

# 21. Sum of odd numbers

total = 0

for i in range(1, 101):
    if i % 2 != 0:
        total += i

print(total)

# 22. Sum of even numbers

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print(total)

# 23. Count spaces in a string

text = "Hello World Python"
count = 0

for ch in text:
    if ch == " ":
        count += 1

print("Spaces:", count)

# 24. Cube of list numbers

lst = [1,2,3,4]
new_list = []

for i in lst:
    new_list.append(i ** 3)

print(new_list)

# 25. Reverse a string

a = "programming"

for i in range(len(a)-1, -1, -1):
    print(a[i], end="")

# 26. Print 0 to 7 only using break

for i in range(50):
    if i > 7:
        break
    print(i)

# 27. Print every letter in string

text = "Python"

for ch in text:
    print(ch)

# 28. Print Hello with names

a = ["ram", "shyam", 1, 2]

for i in a:
    if type(i) == str:
        print("Hello!", i)

# 29. Add Dr. prefix

a = ["ram", "shyam"]
new_list = []

for i in a:
    new_list.append("Dr." + i)

print(new_list)

# 30. Square of each number

lst = [1,2,3,4,5]
new_list = []

for i in lst:
    new_list.append(i ** 2)

print(new_list)

# 31. Append positive numbers

lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
new_list = []

for i in lst1:
    if i > 0:
        new_list.append(i)

print(new_list)

# 32. Print 0 to 6 except 3 and 6

lst = [0,1,2,3,4,5,6]

for i in lst:
    if i == 3 or i == 6:
        continue
    print(i)

# 33. Append datatype of each element

lst1 = [1, "a", 2.5, True]
lst2 = []

for i in lst1:
    lst2.append(type(i))

print(lst2)

# 34. for loop with else

for i in range(5):
    print(i)
else:
    print("Done")

# 35. Print series 105 98 ... 7

for i in range(105, 6, -7):
    print(i, end=" ")

# 36. Remove bad characters

bad_chars = [';', ':', '!', '*']
string = "py;th*o:n ! ;py * t*h:o ! n"
result = ""

for ch in string:
    if ch not in bad_chars and ch != " ":
        result += ch

print(result)

# 37. Count even and odd numbers

numbers = [1,2,3,4,5,6,7,8]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
# 38. Sum of multiples of 3 or 5

total = 0

for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)

# 39. Sum of even and odd separately
even_sum = 0
odd_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

# 40. Count how many times a number appears

list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10

count = 0
for i in list1:
    if i == target:
        count += 1

print("Count:", count)