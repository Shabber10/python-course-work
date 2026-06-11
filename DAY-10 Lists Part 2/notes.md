# DAY-10 Lists Part 2

## 1. Looping Through Lists
You can loop through the list items by using a `for` loop, by index using `range()`, or a `while` loop.

**Input:**
```python
thislist = ["apple", "banana", "cherry"]

# Loop through items
for x in thislist:
    print(x)

# Loop through index numbers
for i in range(len(thislist)):
    print(i, thislist[i])
```
**Output:**
```text
apple
banana
cherry
0 apple
1 banana
2 cherry
```

## 2. List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
**Syntax:** `newlist = [expression for item in iterable if condition == True]`

**Input:**
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

squares = [x**2 for x in range(5)]
print(squares)
```
**Output:**
```text
['apple', 'banana', 'mango']
[0, 1, 4, 9, 16]
```

## 3. Sorting Lists (`sort`, `reverse`)
List objects have a `sort()` method that will sort the list alphanumerically, ascending, by default.

**Input:**
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [100, 50, 65, 82, 23]
numlist.sort(reverse=True) # Descending sort
print(numlist)

thislist.reverse()         # Reverses the current order
print(thislist)
```
**Output:**
```text
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
[100, 82, 65, 50, 23]
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```

## 4. Copying Lists
You cannot copy a list simply by typing `list2 = list1`, because `list2` will only be a reference to `list1`. You must use `copy()` or `list()`.

**Input:**
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```
**Output:**
```text
['apple', 'banana', 'cherry']
```

## 5. Joining Lists
There are several ways to join, or concatenate, two or more lists.
**Input:**
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)
```
**Output:**
```text
['a', 'b', 'c', 1, 2, 3]
['a', 'b', 'c', 1, 2, 3]
```

## 6. List Aggregation Functions
Built-in functions to get totals or find min/max.
**Input:**
```python
nums = [10, 20, 30]
print(sum(nums))
print(max(nums))
print(min(nums))
```
**Output:**
```text
60
30
10
```
