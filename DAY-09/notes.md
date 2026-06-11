# Day 9: Lists Part 1

Lists are used to store multiple items in a single variable. They are created using square brackets `[]`.

## Characteristics of Lists
- **Ordered**: They maintain the order of insertion.
- **Mutable**: You can change, add, and remove items after creation.
- **Allow Duplicates**: Can contain items with the same value.
- **Heterogeneous**: Can contain different data types (e.g., ints, strings, other lists).

```python
my_list = [10, "Hello", 3.14, True]
```

## Accessing List Items
Indexing and slicing work exactly like strings.
```python
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[1])    # 'banana'
print(fruits[-1])   # 'orange'
print(fruits[1:3])  # ['banana', 'cherry']
```

## Basic List Methods (Adding/Removing)

```python
# append() - Add an item to the end
fruits.append("grape")

# insert() - Add an item at a specific index
fruits.insert(1, "mango")

# remove() - Removes the first matching value
fruits.remove("banana")

# pop() - Removes the item at the specified index (or the last item if index is not specified)
last_fruit = fruits.pop()
first_fruit = fruits.pop(0)

# clear() - Empties the list
fruits.clear()
```
