#1
name = "rahUl Dahal"
formatted_name = name.title()
print (formatted_name)

#2
password = "pass@123"
print(password.lower())

#3
movie = "spider-man no way home "
print(movie.title())

#4
heading = "annual sports day"
print(heading.upper())

#5
text="hELLO wORLD"
print(text.swapcase())

#6
log = "System error detected, error code 404"
print(log.find("error"))   # returns first occurrence index

#7
email = "user@gmail.com"
print(email.endswith("@gmail.com"))

#8
msg = "Get free stuff, free gifts and free coupons now!"
print(msg.count("free"))

#9
url = "https://example.com"
print(url.startswith("https"))

#10
resume = "I have experience in Python and Java"
print("Python" in resume)

#11
msg = "Transaction FAILED due to low balance"
print(msg.index("FAILED"))

#12
file = "budget_report.pdf"
print(file.endswith(".pdf"))

#13
phone = "+977-9841123111"
print(phone.startswith("+977"))

#14
url = "https://www.moha.gov.np/"
print(url.endswith(".gov.np/") or ".gov.np" in url)

#15
feedback = "   Great service!   "
print(feedback.strip())

#16
msg = "I hate this, hate it completely"
print(msg.replace("hate", "**"))

#17
filename = "///myfile.txt"
print(filename.lstrip("/"))

#18
price = "Price: $120.33   "
cleaned = price.strip().replace("$", "")
print(cleaned)

#19
phone = "+977 984-123-4567"
digits = phone.replace("-", "")
print(digits)

#20
data = "Aarav,22,Kathmandu,Computer Science"
fields = data.split(",")
for field in fields:
    print(field)

#21
tags = "Python, Coding, Nepal, Tech"
tag_list = tags.split(", ")
result = " ".join("#" + tag for tag in tag_list)
print(result)

#22
names = "Ram, Shyam, Hari, Sita"
passengers = names.split(", ")
print(len(passengers))

#23
words = ["The", "flight", "departs", "at", "6AM"]
sentence = " ".join(words)
print(sentence)

#24
age = input("Enter age: ")
print(age.isdigit())

#25
username = input("Enter username: ")
print(username.isalnum())

#26
name = input("Enter name: ")
print(name.isalpha())

#27
pin = input("Enter PIN: ")
print(pin.isupper())

#28
text = input("Enter text: ")
print(text.isspace())


