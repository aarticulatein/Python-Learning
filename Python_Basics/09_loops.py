```python
# Loops in Python

# A loop is used to execute a block of code repeatedly.


# 1. for loop

for i in range(5):
    print(i)


# range(5) produces numbers from 0 to 4.


# 2. for loop with a list

names = ["Aarti", "Rahul", "Priya"]

for name in names:
    print(name)


# 3. for loop with a string

word = "Python"

for letter in word:
    print(letter)


# 4. range() with a starting and ending value

for number in range(1, 6):
    print(number)


# 5. range() with a step

for number in range(2, 11, 2):
    print(number)


# 6. while loop

number = 1

while number <= 5:
    print(number)
    number += 1


# 7. Using a condition inside a loop

numbers = [10, 15, 20, 25, 30]

for number in numbers:

    if number > 20:
        print(number)


# 8. break statement

# break stops the loop completely.

for number in range(1, 10):

    if number == 5:
        break

    print(number)


# 9. continue statement
# continue skips the current iteration and moves to the next iteration.

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# 10. else with a loop

for number in range(1, 4):
    print(number)
else:
    print("Loop completed.")


# 11. Nested loops

for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)


# 12. Calculating a total using a loop

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total = total + number

print("Total:", total)


# 13. Finding even numbers

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:

    if number % 2 == 0:
        print(number)


# 14. Finding the largest number

numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest:", largest)
```
