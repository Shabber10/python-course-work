# Day 10: Lists Part 2 (Advanced Built-in Functions)

Continuing from Day 9, here are more advanced built-in functions for manipulating lists.

---

## 1. Sorting and Reversing

### `sort()`
Sorts the list in ascending order by default. This modifies the original list.
**Input:**
```python
numbers = [4, 1, 9, 3]
numbers.sort()
print(numbers)
```
**Output:**
```text
[1, 3, 4, 9]
```

**Input (Descending Order):**
```python
numbers = [4, 1, 9, 3]
numbers.sort(reverse=True)
print(numbers)
```
**Output:**
```text
[9, 4, 3, 1]
```

### `reverse()`
Reverses the order of the elements in the list.
**Input:**
```python
letters = ['A', 'B', 'C']
letters.reverse()
print(letters)
```
**Output:**
```text
['C', 'B', 'A']
```

---

## 2. Searching and Counting

### `count()`
Returns the number of times a specified value appears in the list.
**Input:**
```python
votes = ["yes", "no", "yes", "yes", "no"]
print(votes.count("yes"))
```
**Output:**
```text
3
```

### `index()`
Returns the index of the first occurrence of a specified value.
**Input:**
```python
animals = ["cat", "dog", "rabbit"]
print(animals.index("dog"))
```
**Output:**
```text
1
```

---

## 3. Copying Lists

### `copy()`
Returns a shallow copy of the list.
**Input:**
```python
original = [1, 2, 3]
duplicate = original.copy()

# Changing the duplicate doesn't affect the original
duplicate.append(4)

print("Original:", original)
print("Duplicate:", duplicate)
```
**Output:**
```text
Original: [1, 2, 3]
Duplicate: [1, 2, 3, 4]
```
