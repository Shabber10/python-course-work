# Day 11: Tuples (Basics and Built-in Functions)

Tuples are used to store multiple items in a single variable. They are **ordered**, **allow duplicate values**, but are **immutable** (cannot be changed after creation).

Because tuples are immutable, they have fewer built-in methods compared to lists.

Here is a well-organized list of tuple built-in functions.

---

## 1. Searching and Counting

### `count()`
Returns the number of times a specified value occurs in the tuple.
**Input:**
```python
my_tuple = (1, 5, 7, 5, 9, 5)
print(my_tuple.count(5))
```
**Output:**
```text
3
```

### `index()`
Searches the tuple for a specified value and returns the index of its first occurrence.
**Input:**
```python
colors = ("red", "green", "blue", "yellow")
print(colors.index("blue"))
```
**Output:**
```text
2
```

---

## 2. Working with Tuples (Operations rather than Methods)

While tuples don't have many methods, you can perform several operations on them using built-in Python functions.

### Finding Length (`len()`)
Finds how many items are in the tuple.
**Input:**
```python
fruits = ("apple", "banana", "cherry")
print(len(fruits))
```
**Output:**
```text
3
```

### Concatenation (`+`)
You can join two tuples together to create a new one.
**Input:**
```python
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)
```
**Output:**
```text
(1, 2, 3, 4)
```

### Tuple Unpacking
Extracting values from a tuple into variables.
**Input:**
```python
coordinates = (10, 20, 30)
x, y, z = coordinates
print("X:", x)
print("Y:", y)
```
**Output:**
```text
X: 10
Y: 20
```
