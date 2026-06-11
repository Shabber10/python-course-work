# Day 4: Conditional Statements

Conditional statements allow your program to make decisions based on certain conditions.

## `if` Statement
Executes a block of code if the condition is True.
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

## `if...else` Statement
Executes an alternative block if the condition is False.
```python
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

## `if...elif...else` Statement
Used to check multiple conditions sequentially.
```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**Note**: Python uses indentation (whitespace) to define the scope of the code block. Consistent indentation is mandatory!
