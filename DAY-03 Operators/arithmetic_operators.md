Arithmetic Operators in Python
==============================

Arithmetic operators are used with numeric values to perform common mathematical operations. Here is a comprehensive guide to the arithmetic operators available in Python.

1. Addition (+)
----------------
Adds two values together.
- Example:
  a = 10
  b = 5
  result = a + b  # result is 15
  print("Addition:", result)

2. Subtraction (-)
-------------------
Subtracts the right-hand value from the left-hand value.
- Example:
  a = 10
  b = 5
  result = a - b  # result is 5
  print("Subtraction:", result)

3. Multiplication (*)
----------------------
Multiplies two values.
- Example:
  a = 10
  b = 5
  result = a * b  # result is 50
  print("Multiplication:", result)

4. Division (/)
----------------
Divides the left-hand value by the right-hand value. In Python, this operator always returns a float (decimal value).
- Example:
  a = 10
  b = 5
  result = a / b  # result is 2.0
  print("Division:", result)

5. Modulus (%)
---------------
Returns the remainder when the left-hand value is divided by the right-hand value.
- Example:
  a = 10
  b = 3
  result = a % b  # result is 1 (since 10 = 3 * 3 + 1)
  print("Modulus:", result)

6. Exponentiation (**)
-----------------------
Raises the left-hand value to the power of the right-hand value (a raised to the power b).
- Example:
  a = 2
  b = 3
  result = a ** b  # result is 8 (2 * 2 * 2)
  print("Exponentiation:", result)

7. Floor Division (//)
-----------------------
Divides the left-hand value by the right-hand value and rounds down (floors) the result to the nearest whole number.
- Example:
  a = 10
  b = 3
  result = a // b  # result is 3
  print("Floor Division:", result)
  
  # Example with negative numbers:
  c = -10
  d = 3
  result_neg = c // d  # result is -4 (rounds down to the next smaller integer)
  print("Floor Division (negative):", result_neg)

Operator Precedence (Order of Operations)
==========================================
When multiple operators are used in a single expression, Python evaluates them in a specific order:
1. Parentheses ()
2. Exponentiation (**)
3. Multiplication, Division, Floor Division, and Modulus (*, /, //, %) - evaluated left to right
4. Addition and Subtraction (+, -) - evaluated left to right

Example:
expression = 5 + 3 * 2 ** 2
# 1. Exponentiation: 2 ** 2 = 4
# 2. Multiplication: 3 * 4 = 12
# 3. Addition: 5 + 12 = 17
print("Result of expression:", expression) # Output: 17
