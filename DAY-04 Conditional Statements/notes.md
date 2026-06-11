# DAY-04 Conditional Statements

Conditional statements are used to perform different actions based on different conditions.

## 1. `if` Statement
Executes a block of code if the condition is True.

**Input:**
```python
age = 20
if age >= 18:
    print("You are eligible to vote.")
```
**Output:**
```text
You are eligible to vote.
```

## 2. `elif` Statement
The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

**Input:**
```python
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
```
**Output:**
```text
a and b are equal
```

## 3. `else` Statement
The `else` keyword catches anything which isn't caught by the preceding conditions.

**Input:**
```python
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
**Output:**
```text
Odd number
```

## 4. Short Hand `if`
If you have only one statement to execute, you can put it on the same line as the if statement.

**Input:**
```python
if 5 > 2: print("Five is greater than two!")
```
**Output:**
```text
Five is greater than two!
```

## 5. Short Hand `if...else` (Ternary Operator)
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.

**Input:**
```python
a = 2
b = 330
print("A") if a > b else print("B")
```
**Output:**
```text
B
```

## 6. Nested `if` Statements
You can have `if` statements inside `if` statements, this is called nested `if` statements.

**Input:**
```python
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```
**Output:**
```text
Above ten,
and also above 20!
```

## 7. The `pass` Statement
`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

**Input:**
```python
a = 33
b = 200
if b > a:
    pass # Code to be added later
print("Program continues without error.")
```
**Output:**
```text
Program continues without error.
```
