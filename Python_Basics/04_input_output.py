```python
# Input and Output in Python


# 1. Output using print()

print("Hello, World!")
print("I am learning Python.")


# 2. Printing variables

name = "Aarti"
age = 29

print(name)
print(age)


# 3. Printing multiple values

first_name = "Aarti"
last_name = "Sharma"

print(first_name, last_name)


# 4. Using sep in print()

print("Aarti", "Sharma", sep="-")

print("2026", "10", "02", sep="-")


# 5. Using end in print()

print("Hello", end=" ")
print("World")


# 6. Taking input from the user

name = input("Enter your name: ")

print("Hello", name)


# 7. Taking different information from the user

name = input("Enter your name: ")
city = input("Enter your city: ")

print("My name is", name)
print("I live in", city)


# 8. Input is stored as a string

age = input("Enter your age: ")

print(age)
print(type(age))


# 9. Converting input into an integer

age = int(input("Enter your age: "))

print(age)
print(type(age))


# 10. Taking a decimal number as input

price = float(input("Enter the price: "))

print(price)
print(type(price))


# 11. Using input in a calculation

number = int(input("Enter a number: "))

print(number + 10)
print(number * 2)
```

### Important point

`input()` **always returns a string**.




