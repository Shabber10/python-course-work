# DAY-02 Data Types and Type Casting

Variables can store data of different types, and different types can do different things.

## 1. Built-in Data Types Overview
- **Numeric Types:** `int`, `float`, `complex`
- **Sequence Types:** `str`, `list`, `tuple`
- **Mapping Type:** `dict`
- **Set Types:** `set`, `frozenset`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`, `memoryview`
- **None Type:** `NoneType`

## 2. Getting the Data Type (`type()`)
You can get the data type of any object by using the `type()` function.

**Input:**
```python
x = 10        # int
y = 3.14      # float
z = 1j        # complex
name = "Bob"  # str
is_active = True # bool

print(type(x))
print(type(z))
print(type(is_active))
```
**Output:**
```text
<class 'int'>
<class 'complex'>
<class 'bool'>
```

## 3. Implicit Type Conversion
Python automatically converts one data type to another data type when evaluating an expression (usually promoting the smaller type to the larger one to prevent data loss).

**Input:**
```python
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo # int + float results in a float
print("Value:", num_new)
print("Type:", type(num_new))
```
**Output:**
```text
Value: 124.23
Type: <class 'float'>
```

## 4. Explicit Type Casting
Converting a variable from one data type to another manually using constructor functions.

### `int()`
Constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number).
**Input:**
```python
x = int(1)     # x will be 1
y = int(2.8)   # y will be 2
z = int("3")   # z will be 3
print(x, y, z)
```
**Output:**
```text
1 2 3
```

### `float()`
Constructs a float number from an integer literal, a float literal or a string literal.
**Input:**
```python
x = float(1)     # x will be 1.0
y = float("3.5") # y will be 3.5
print(x, y)
```
**Output:**
```text
1.0 3.5
```

### `str()`
Constructs a string from a wide variety of data types, including strings, integer literals and float literals.
**Input:**
```python
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)
```
**Output:**
```text
s1 2 3.0
```

### `bool()`
Evaluates any value, and gives you `True` or `False`. Almost any value is evaluated to `True` if it has some sort of content. (Empty strings, `0`, `None`, empty lists `[]` are `False`).
**Input:**
```python
print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool(""))
```
**Output:**
```text
True
True
False
False
```
