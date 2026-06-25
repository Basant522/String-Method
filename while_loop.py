#1
numbers = []

num = int(input("Enter number: "))

while num not in numbers:
    numbers.append(num)
    num = int(input("Enter number: "))

print("Duplicate found:", num)

#2

n = int(input("Enter a positive number: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)



n = int(input("Enter a number: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum =", total)

#4
numbers = [10, 5, 10, 7, 10, 3]

count = 0
i = 0

while i < len(numbers):
    if numbers[i] == 10:
        count += 1
    i += 1

print("Count =", count)

#5
text = input("Enter a sentence: ")

vowels = 0
consonants = 0
i = 0

while i < len(text):
    ch = text[i]

    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    i += 1

print("Vowels =", vowels)
print("Consonants =", consonants)

#6
num = abs(int(input("Enter number: ")))

count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)

#7
n = int(input("Enter number: "))

while n != 1:
    print(n, end=" ")
    
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(1)

#8
ch = ord('A')

while ch <= ord('Z'):
    print(chr(ch), end=" ")
    ch += 1

#9
start = int(input("Enter start: "))
end = int(input("Enter end: "))

while start <= end:
    print(start)
    start += 1

#10
n = 49

while n >= 1:
    print(n)
    n -= 2

#11
i = 7

while i <= 100:
    print(i)
    i += 7

#12
total = 0

num = int(input("Enter number: "))

while num != 0:
    total += num
    num = int(input("Enter number: "))

print("Total =", total)

#13
age = int(input("Enter age: "))

while age < 0 or age > 120:
    print("invalid age")
    age = int(input("Enter age again: "))

print("Valid age =", age)

#14
total = 0
count = 0

score = int(input("Enter score (-1 to stop): "))

while score != -1:
    total += score
    count += 1
    score = int(input("Enter score (-1 to stop): "))

if count > 0:
    print("Average =", total / count)
else:
    print("No scores entered")

#15
password = "secret123"
attempts = 0

while attempts < 3:
    user_pass = input("Enter password: ")

    if user_pass == password:
        print("access granted")
        break

    attempts += 1

if attempts == 3:
    print("access denied")

#16
num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed =", reverse)


#17
n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#18
text = input("Enter string: ")

i = 0
result = ""

while i < len(text):
    if text[i].lower() not in "aeiou":
        result += text[i]
    i += 1

print(result)

#19
text = input("Enter string: ")
sub = input("Enter substring: ")

count = 0
i = 0

while i <= len(text) - len(sub):
    if text[i:i+len(sub)] == sub:
        count += 1
    i += 1

print("Occurrences =", count)

#20
numbers = [12, 25, 7, 30, 18, 40, 55, 9]

i = 0

while i < len(numbers):
    if numbers[i] % 5 == 0:
        print(numbers[i])
    i += 1


#21

text = input("Enter a string: ")

i = 0
result = ""

while i < len(text):
    ch = text[i]

    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

    i += 1

print(result)

#22
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f"({i},{j})", end=' ')
        j += 1
    i += 1
#When i = 1, j runs: 1, 2 → 2 times
#When i = 2, j runs: 1, 2 → 2 times
#Answer: For every one increment of i, the inner loop j runs 2 times.


#23

i=1
j=1
while i<=3:
    while j <=2:
        print('*',end='')
        j+= 1
    i+= 1
    
#Mistake: j is initialized only once outside the outer loop.
#First iteration: j = 1, 2 → prints **
#Then j = 3
#Next outer loop iterations: condition j <= 2 is False
#So no more stars are printed.
#Answer: j should be reset inside the outer loop.

#CORRECT CODE:
i=1
while i <= 3:
    j = 1
    while j <= 2:
        print('*', end='')
        j += 1
    i += 1

#24
found = False
x = 1

while not found:
    if x * x > 20:
        found = True
    else:
        x += 1

print(x)
#Answer:
#1² = 1
#2² = 4
#3² = 9
#4² = 16
#5² = 25 > 20

print(x)

#25
total = 0
user_input = 0

while user_input != -1:
    total += user_input
    user_input = int(input())

print(total)
#Answer:
#4 added
#7 added
#-1 is entered and loop stops
#10 is never entered
#Total:
#0 + 4 + 7 = 11

#26
x = 10

while x < 5:
    x += 1
    print('loop')

print(x)
#Since 10 < 5 is False, the loop never runs.
#Answer:
#"loop" prints 0 times
#Final value of x = 10

#27
x = 3

while x:
    print(x, end=' ')
    x -= 1

#After printing 1, x becomes 0.
#In Python, 0 = False.
#Answer: x evaluates to False when x = 0.

#28
a, b = 0, 1

while a < 10:
    print(a, end=' ')
    a, b = b, a + b

#Answer: This is the Fibonacci Sequence.

#29
def count_case(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("No. of upper case characters :", upper)
    print("No. of lower case characters :", lower)

count_case("The quick Brow Fox")

#30
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    a = int(input("First number: "))
    b = int(input("Second number: "))

    if choice == 1:
        print("Result =", a + b)
    elif choice == 2:
        print("Result =", a - b)
    elif choice == 3:
        print("Result =", a * b)


#31
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]
i = 1

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1

print("Largest =", largest)

#32
start = int(input("Enter start: "))
end = int(input("Enter end: "))

while start <= end:
    if start > 1:
        i = 2
        prime = True

        while i < start:
            if start % i == 0:
                prime = False
                break
            i += 1

        if prime:
            print(start)

    start += 1

#33
numbers = [12, 40, 21, 31, 10, 7, 5]

i = 0

while i < len(numbers):
    if numbers[i] < 20:
        print(numbers[i])
    i += 1

#34
numbers = [45, 60, 12, 75, 30, 55, 8, 90]

i = 0

while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0
    i += 1

print(numbers)

#35
numbers = [15, 25, 30, 45, 60, 12, 90, 7]

count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 15 == 0:
        count += 1
    i += 1

print("Count =", count)


#36
numbers = [10, 15, 25, 30, 45]

i = 0
sorted_list = True

while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break
    i += 1

if sorted_list:
    print("Sorted")
else:
    print("Not Sorted")

#37
ch = ord('a')

while ch <= ord('z'):
    print(chr(ch), end=" ")
    ch += 1

#38
pages = [45, 30, 50, 40]

i = 0
chapter = 1

while i < len(pages):
    print("Chapter", chapter, "has", pages[i], "pages")
    chapter += 1
    i += 1

#39
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

i = 0

while i < len(list1):
    if list1[i] in list2:
        print(list1[i])
    i += 1

#40
numbers = [2, 4, 6, 7, 8]

i = 0

while i < len(numbers):
    j = 1

    while j <= 10:
        print(numbers[i], "x", j, "=", numbers[i] * j)
        j += 1

    print()
    i += 1

#41
numbers = [1, 2, 3, 4, 2]

i = 0
duplicate = False

while i < len(numbers):
    j = i + 1

    while j < len(numbers):
        if numbers[i] == numbers[j]:
            duplicate = True
            break
        j += 1

    if duplicate:
        break

    i += 1

if duplicate:
    print("Has Duplicates")
else:
    print("No Duplicates")



