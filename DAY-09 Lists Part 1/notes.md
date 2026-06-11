# DAY-09 Lists Part 1

Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data.

## 1. List Characteristics
- **Ordered:** The items have a defined order, and that order will not change.
- **Changeable (Mutable):** We can change, add, and remove items after it has been created.
- **Allow Duplicates:** Since lists are indexed, lists can have items with the same value.
- **Heterogeneous:** A list can contain different data types.

**Input:**
```python
mylist = ["apple", "banana", "cherry", "apple", 1, True]
print(mylist)
```
**Output:**
```text
['apple', 'banana', 'cherry', 'apple', 1, True]
```

## 2. List Length and Constructor
**Input:**
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(len(thislist))
print(type(thislist))
```
**Output:**
```text
3
<class 'list'>
```

## 3. Accessing and Slicing Items
List items are indexed and you can access them by referring to the index number.
**Input:**
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])      # Positive Indexing
print(thislist[-1])     # Negative Indexing
print(thislist[2:5])    # Range of Indexes
print(thislist[:4])     # From Start to Index 4 (not included)
```
**Output:**
```text
banana
mango
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
```

## 4. Changing Item Values
**Input:**
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)
```
**Output:**
```text
['apple', 'blackcurrant', 'cherry']
['apple', 'watermelon']
```

## 5. Adding Items (`append`, `insert`, `extend`)
**Input:**
```python
thislist = ["apple", "banana"]
thislist.append("cherry")      # Adds to end
print(thislist)

thislist.insert(1, "orange")   # Inserts at index 1
print(thislist)

tropical = ["mango", "pineapple"]
thislist.extend(tropical)      # Appends elements from another list
print(thislist)
```
**Output:**
```text
['apple', 'banana', 'cherry']
['apple', 'orange', 'banana', 'cherry']
['apple', 'orange', 'banana', 'cherry', 'mango', 'pineapple']
```

## 6. Removing Items (`remove`, `pop`, `del`, `clear`)
**Input:**
```python
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")  # Removes first occurrence
print(thislist)

popped = thislist.pop(1)   # Removes at index (or last if not specified)
print(popped)

del thislist[0]            # Also removes at specified index
print(thislist)

thislist.clear()           # Empties the list
print(thislist)
```
**Output:**
```text
['apple', 'cherry', 'banana']
cherry
['banana']
[]
```
