# DAY-01 Introduction to Python

Python is a high-level, interpreted programming language created by Guido van Rossum. It is known for its readability, simplicity, and broad range of applications (web development, data science, automation, etc.).

## 1. Python Syntax & Strict Indentation
Unlike other languages that use curly brackets `{}` or keywords to define blocks of code, Python uses **indentation** (whitespace at the beginning of a line).
- You must be consistent with the number of spaces (usually 4).
- Missing or inconsistent indentation will result in an `IndentationError`.

**Input:**
```python
if 5 > 2:
    print("Five is greater than two!") # Indented correctly
```
**Output:**
```text
Five is greater than two!
```

## 2. Comments
Comments are used to explain code and are ignored by the Python interpreter.
- **Single-line Comments:** Start with a hash symbol `#`.
- **Multi-line Comments:** Python doesn't have explicit multi-line comment syntax, but you can use triple quotes `"""` or `'''` (often called docstrings) which are ignored if not assigned to a variable.

**Input:**
```python
# This is a single-line comment
print("Hello")

"""
This is a multi-line comment.
It can span multiple lines.
"""
print("World")
```
**Output:**
```text
Hello
World
```

## 3. Variables & Memory References
Variables are containers for storing data values. You don't need to declare their type explicitly.
Python uses dynamic typing. Variables refer to objects in memory. You can get the memory address using the `id()` function.

**Input:**
```python
x = 10
y = "Alice"
print("x:", x)
print("Memory Address of x:", id(x))
```
**Output:**
```text
x: 10
Memory Address of x: 140723849312936
```

## 4. Variable Naming Conventions
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables).
- **Camel Case:** `myVariableName = "John"`
- **Pascal Case:** `MyVariableName = "John"`
- **Snake Case:** `my_variable_name = "John"`

## 5. Output Function (`print()`)
The `print()` function outputs text to the console. It has optional parameters like `sep` (separator) and `end` (end character).

**Input:**
```python
print("Apple", "Banana", "Cherry", sep=" | ", end=" ***")
print("New Line!")
```
**Output:**
```text
Apple | Banana | Cherry ***New Line!
```

## 6. Input Function (`input()`)
The `input()` function pauses program execution to allow the user to type something. By default, it reads the input as a **string**.

**Input:**
```python
name = input("Enter your name: ")
print("Welcome,", name)
```
**Output:**
```text
Enter your name: Shabber
Welcome, Shabber
```
