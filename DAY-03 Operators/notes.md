# Day 3: Operators

Operators are special symbols that carry out arithmetic or logical computation.

## 1. Arithmetic Operators
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/` (Always returns a float)
- Floor Division: `//` (Returns integer, discards remainder)
- Modulus: `%` (Returns remainder)
- Exponentiation: `**` (Power)

```python
a = 10
b = 3
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000
```

## 2. Relational (Comparison) Operators
Return `True` or `False`.
- Equal to: `==`
- Not equal to: `!=`
- Greater than: `>`
- Less than: `<`
- Greater/Equal: `>=`
- Less/Equal: `<=`

## 3. Logical Operators
Used to combine conditional statements.
- `and`: True if both statements are true
- `or`: True if one of the statements is true
- `not`: Reverse the result

```python
x = 5
print(x > 3 and x < 10) # True
```

## 4. Assignment Operators
Used to assign values to variables (`=`, `+=`, `-=`, `*=`, `/=`).
```python
count = 0
count += 1 # Equivalent to count = count + 1
```
