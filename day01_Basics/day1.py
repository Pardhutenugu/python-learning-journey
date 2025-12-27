# This is my Day 1 Python Learning

# Variables

name = "Pardhu"  # string
age = 20         # integer
height = 5.8     # float
is_student = True  # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Input from user

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print("Hello", user_name, "you are", user_age, "years old.")

# Arithmetic operations

a = 10
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Exponent:", a ** b)

# Comparison and logical operators

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b and b < 5:", a > b and b < 5)
print("not(a < b):", not(a < b))

# Strings


greeting = "Hello " + name
repeat_text = "Hi! " * 3
print(greeting)
print(repeat_text)

print("First character:", name[0])
print("Last character:", name[-1])
print("Slice name[1:4]:", name[1:4])

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Capitalize:", name.capitalize())
print("Replace P->B:", name.replace("P", "B"))
print("Length of name:", len(name))

# Conditional statements

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Boolean logic
is_adult = True
has_permission = False
if is_adult and has_permission:
    print("Access granted")
else:
    print("Access denied")
