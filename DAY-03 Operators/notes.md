# DAY-03 Operators

Operators are used to perform operations on variables and values.

## 1. Arithmetic Operators
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/` (Always returns a float)
- Floor Division: `//` (Returns integer, discards remainder)
- Modulus: `%` (Returns remainder)
- Exponentiation: `**` (Power)

**Input:**
```python
a = 10
b = 3
print(a / b)  # Normal division
print(a // b) # Floor division
print(a % b)  # Modulus
print(a ** b) # Power
```
**Output:**
```text
3.3333333333333335
3
1
1000
```

## 2. Assignment Operators
Used to assign values to variables.
- `=` (Assign)
- `+=` (Add AND Assign)
- `-=` (Subtract AND Assign)
- `*=` (Multiply AND Assign)
- `/=` (Divide AND Assign)

**Input:**
```python
x = 5
x += 3 # Equivalent to x = x + 3
print(x)
```
**Output:**
```text
8
```

## 3. Comparison (Relational) Operators
Used to compare two values. They return `True` or `False`.
- `==` (Equal)
- `!=` (Not equal)
- `>` (Greater than)
- `<` (Less than)
- `>=` (Greater than or equal to)
- `<=` (Less than or equal to)

## 4. Logical Operators
Used to combine conditional statements.
- `and`: Returns True if both statements are true
- `or`: Returns True if one of the statements is true
- `not`: Reverse the result, returns False if the result is true

**Input:**
```python
x = 5
print(x > 3 and x < 10)
print(not(x > 3 and x < 10))
```
**Output:**
```text
True
False
```

## 5. Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
- `is`
- `is not`

**Input:**
```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True because z is the same object as x
print(x is y) # False because x and y are different objects in memory, despite having same values
print(x == y) # True because the values are equal
```
**Output:**
```text
True
False
True
```

## 6. Membership Operators
Membership operators are used to test if a sequence is presented in an object.
- `in`
- `not in`

**Input:**
```python
fruits = ["apple", "banana"]
print("banana" in fruits)
print("pineapple" not in fruits)
```
**Output:**
```text
True
True
```

## 7. Bitwise Operators
Used to compare (binary) numbers.
- `&` (AND)
- `|` (OR)
- `^` (XOR)
- `~` (NOT)
- `<<` (Zero fill left shift)
- `>>` (Signed right shift)

**Input:**
```python
# 6 = 0110 in binary
# 3 = 0011 in binary
print(6 & 3) # AND: 0010 (2)
print(6 | 3) # OR:  0111 (7)
```
**Output:**
```text
2
7
```
