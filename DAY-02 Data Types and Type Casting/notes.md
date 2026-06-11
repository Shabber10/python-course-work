# Day 2: Data Types and Type Casting

## Basic Data Types
Python has several built-in data types:
1. **Integer (`int`)**: Whole numbers (e.g., `10`, `-5`, `0`)
2. **Float (`float`)**: Decimal numbers (e.g., `3.14`, `-0.001`)
3. **String (`str`)**: Text enclosed in quotes (e.g., `"Hello"`, `'Python'`)
4. **Boolean (`bool`)**: Represents `True` or `False`.

```python
x = 10        # int
y = 3.14      # float
name = "Bob"  # str
is_active = True # bool

# To check the type of a variable
print(type(x)) # Output: <class 'int'>
```

## Type Casting (Type Conversion)
Converting a variable from one data type to another.

```python
# String to Integer
num_str = "100"
num_int = int(num_str)
print(type(num_int))

# Integer to Float
val = 5
val_float = float(val) # Becomes 5.0

# Float to Integer
pi = 3.14
pi_int = int(pi) # Becomes 3 (decimals are truncated)
```
