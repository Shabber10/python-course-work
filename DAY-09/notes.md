# Day 9: Lists Part 1 (Basics and Built-in Functions)

Lists are used to store multiple items in a single variable. They are **ordered**, **mutable** (changeable), and allow duplicate values.

Here is a well-organized list of basic built-in list functions.

---

## 1. Adding Items to a List

### `append()`
Adds a single element to the end of the list.
**Input:**
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
```
**Output:**
```text
['apple', 'banana', 'cherry']
```

### `insert()`
Inserts an element at a specified index.
**Input:**
```python
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)
```
**Output:**
```text
['apple', 'orange', 'banana']
```

### `extend()`
Adds the elements of another list (or any iterable) to the end of the current list.
**Input:**
```python
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)
```
**Output:**
```text
[1, 2, 3, 4]
```

---

## 2. Removing Items from a List

### `remove()`
Removes the first occurrence of a specified value.
**Input:**
```python
colors = ["red", "green", "blue", "green"]
colors.remove("green")
print(colors)
```
**Output:**
```text
['red', 'blue', 'green']
```

### `pop()`
Removes the element at the specified index and returns it. If no index is specified, it removes and returns the last item.
**Input:**
```python
numbers = [10, 20, 30, 40]
last_item = numbers.pop()
print("Popped:", last_item)
print("List:", numbers)
```
**Output:**
```text
Popped: 40
List: [10, 20, 30]
```

### `clear()`
Removes all elements from the list, leaving it empty.
**Input:**
```python
items = ["pencil", "pen", "eraser"]
items.clear()
print(items)
```
**Output:**
```text
[]
```
