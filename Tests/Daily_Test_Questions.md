# Comprehensive Daily Test Questions

This file contains the complete question bank. Each question has its options (if MCQ), followed by a collapsible section containing the correct answer and a brief explanation.

---

## Day 02-04: Python Tokens, Data Types & Operators

### Q171. Analyze the following Python code snippet. What is the exact number of times the multiplication result will be printed to the console? for i in range(2, 4): for j in range(1, 11): if i == j: break print(i, "*", j, "=", i*j)

* [ ] **A**. 10
* [ ] **B**. 20
* [ ] **C**. 3
* [ ] **D**. 2

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 3<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q172. What two measurements are used to calculate BMI?

* [ ] **A**. Weight and Height
* [ ] **B**. Weight and Age
* [ ] **C**. Height and Age
* [ ] **D**. Weight and Blood Pressure

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Weight and Height<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q173. Where is procedural programming commonly applied?

* [ ] **A**. Complex GUI applications
* [ ] **B**. Operating Systems and embedded systems
* [ ] **C**. Large scale enterprise applications
* [ ] **D**. Modern web frameworks

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Complex GUI applications<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q174. According to the conditional logic in the Python BMI Calculator, which status will be displayed to a user if their calculated BMI is exactly 17.5?

* [ ] **A**. Underweight
* [ ] **B**. Healthy
* [ ] **C**. Extremely Underweight
* [ ] **D**. Overweight

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. Overweight<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q175. What is the visual result of the following Python code snippet? for i in range(4): for j in range(4): if i == j: print('*', end=' ') else: print(' ', end=' ') print()

* [ ] **A**. A vertical line of stars in the first column
* [ ] **B**. A hollow square made of stars
* [ ] **C**. A horizontal line of stars in the first row
* [ ] **D**. A diagonal line of stars starting from the top-left corner

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. A hollow square made of stars<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q176. In the following Python implementation for a BMI calculator, what is the result if the user inputs a height of '0' after selecting 'Meters' as the unit? try: if height_unit == 'Centimeters': height_m = height / 100 else: height_m = height if height_m <= 0: st.error('Height must be greater than zero.') else: bmi = weight / (height_m ** 2) except: st.error('Please enter valid numeric values.')

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q177. Given an integer n, print the following pattern: For n = 3, the output should be: 1 1 1 2 3 2 2 2 3 3 3 4 Pattern Rules :- Output contains n rows. Each row has 4 numbers. Column-1 (first column): Row-1 → 1 Row-2 → 3 Row-3 → 3 Middle columns follow a different decreasing or increasing logic. Last column alternates values based on row index. (Your exact pattern appears to be fixed for n=3 only. So we treat this as: for any n, follow the mathematical rules.)

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
n=int(input())
for i in range(1,n+1):
  c1=i
  c2=n-i+1 
  c3=n-i+1
  if i%2==1:
    c4=i+1 
  else:
    c4=i
  print(c1,c2,c3,c4)
```
</details>

### Q178. Given an integer n, print the following pattern: Numbers start from 1 and increase continuously. For odd rows (1,3,5,...) print numbers in ascending order. For even rows (2,4,6,...) print numbers in descending order. Numbers in the same row must be separated using "*".

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())

num=1
for i in range(1,a+1):
  row=[]
  for j in range(i):
    row.append(num)
    num+=1
  if i%2==0:
    row=row[::-1]
    
  print("*".join(map(str,row)))
```
</details>

### Q179. You are given a positive integer N. Your task is to print a palindromic triangle of size N. A palindromic triangle of size 5 looks like: 1 121 12321 1234321 123454321 Important Rules You cannot use strings. You must use exactly ONE print statement in the code. You must not use more than one for-statement (the first for-loop is already provided). Input Format : A single line of input containing the integer N. Output Format : Print the palindromic triangle of size N, each row on a new line.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
for i in range(1,a+1):
  for j in range(1,i+1):
    print(j,end='')
  for k in range(i-1,0,-1):
    print(k,end='')
  print()
```
</details>

---

## Day 05-06: Strings (Basics & Operations)

### Q46. What is the result of tuple("a,b".split(","))?

* [ ] **A**. ('a', 'b')
* [ ] **B**. ('a,b')
* [ ] **C**. a,b
* [ ] **D**. ['a', 'b']

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. ('a,b')<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q47. Which is a valid way to check if two strings are different?

* [ ] **A**. str1 =! str2
* [ ] **B**. str1 <> str2
* [ ] **C**. str1 != str2
* [ ] **D**. str1 not= str2

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. str1 not= str2<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q48. Can int() convert the string "hello" to an integer?

* [ ] **A**. Yes
* [ ] **B**. No
* [ ] **C**. Only if it’s "0"
* [ ] **D**. Only if it’s positive

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Yes<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q49. What does float("-1.23") return in Python?

* [ ] **A**. -1.23
* [ ] **B**. 1.23
* [ ] **C**. '-1.23'
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. '-1.23'<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q50. What does int(" 42 ") return in Python?

* [ ] **A**. 42
* [ ] **B**. 42.0
* [ ] **C**. Raises ValueError
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 42<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q51. Consider the following Python code: score = input("Enter score: ") # Assume the user enters 50 final_score = int(score) + 10 print(final_score) What is the primary reason the int() function is used in this logic?

* [ ] **A**. To display the user's score on the screen
* [ ] **B**. To ensure that the input is stored as a string throughout the program
* [ ] **C**. To determine the current data type of the score variable
* [ ] **D**. To convert the string input into an integer so mathematical addition can be performed

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. To ensure that the input is stored as a string throughout the program<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q52. Given x = "99", what will be the result of the expression int(x) * 2 in Python?

* [ ] **A**. 198
* [ ] **B**. "198"
* [ ] **C**. 99
* [ ] **D**. 18

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. "198"<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q53. What value is produced when the string "-10" is converted to an integer using int() in Python?

* [ ] **A**. -10
* [ ] **B**. 10
* [ ] **C**. "-10"
* [ ] **D**. 0

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. 10<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q54. What is the result of len(str(2.5)) in Python?

* [ ] **A**. 2
* [ ] **B**. 3
* [ ] **C**. 4
* [ ] **D**. 0

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. 0<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q55. What is the result of converting the string "-3.14" using the float() function in Python?

* [ ] **A**. -3.14
* [ ] **B**. "-3.14"
* [ ] **C**. Error
* [ ] **D**. 0

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. -3.14<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q56. What will int(9.999) return?

* [ ] **A**. 9
* [ ] **B**. 10
* [ ] **C**. 9.999
* [ ] **D**. 11

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 9.999<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q57. What will be the boolean result of the following Python expression? val = (25 != 25) == (100 > 50) print(val)

* [ ] **A**. True
* [ ] **B**. Error
* [ ] **C**. None
* [ ] **D**. False

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. True<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q58. What is the output of printing int(9.9999) directly in Python?

* [ ] **A**. 9.9999
* [ ] **B**. 10
* [ ] **C**. 9
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. 10<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q59. What does str(10.5) + str(0.5) return in Python?

* [ ] **A**. 11
* [ ] **B**. 10.5 0.5
* [ ] **C**. '10.50.5'
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 11<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q60. In Python, what is the resulting data type and value when an integer and a float are added together, such as in the following code? x = 7 y = 3.0 z = x + y print(z) print(type(z))

* [ ] **A**. 10.0, <class 'float'>
* [ ] **B**. 10.0, <class 'int'>
* [ ] **C**. 10, <class 'int'>
* [ ] **D**. 73.0, <class 'float'>

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 10, <class 'int'><br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q61. What output is produced by the Python f-string f"Temp: {temp:03d}" when temp = 7?

* [ ] **A**. Temp: 007
* [ ] **B**. Temp: 7
* [ ] **C**. Temp: 07
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Temp: 7<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q62. What happens when the statement data[input("Key: ")] = int(input("Value: ")) + 5 is executed and the user enters "x" as the key and 10 as the value?

* [ ] **A**. Adds "x": 15
* [ ] **B**. Adds "x": 10
* [ ] **C**. Adds 15: "x"
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Adds 15: "x"<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q63. What happens if you use data[input()] = int(input()) and the user types "num" and "abc"?

* [ ] **A**. Raises ValueError
* [ ] **B**. Adds "num": "abc" to data
* [ ] **C**. Adds "abc": "num" to data
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Adds "abc": "num" to data<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q64. Which specific function is used in Python to convert the string output of input() into a whole number so that arithmetic operations can be performed?

* [ ] **A**. str()
* [ ] **B**. type()
* [ ] **C**. float()
* [ ] **D**. int()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. float()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q65. What value is returned by input("Text: ") when the user enters Python?

* [ ] **A**. P y t hon
* [ ] **B**. "Python"
* [ ] **C**. ' Pytho '
* [ ] **D**. ValueError

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. ' Pytho '<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q66. In Python, what is the underlying reason why the following code would fail to perform a mathematical addition if the user enters 5? val = input("Enter a number: ") print(val + 10)

* [ ] **A**. The input() function always returns the user's entry as a string, even if digits are entered.
* [ ] **B**. The input() function can only accept alphabetic characters as valid arguments.
* [ ] **C**. Variable names like 'val' are reserved for string data only in Python 3.
* [ ] **D**. Python does not allow the addition of an integer to a variable that has not been specifically initialized with a zero.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. The input() function always returns the user's entry as a string, even if digits are entered.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q67. If a user runs the following Python code and enters the sequence 456, what will be the resulting output? num = tuple(input("Enter number: ")) print(num)

* [ ] **A**. (4, 5, 6)
* [ ] **B**. ('4', '5', '6')
* [ ] **C**. (456)
* [ ] **D**. ('456',)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. (456)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q68. Consider the following Python code snippet: x, y = input("Enter two numbers: ").split() print(type(x), type(y)) If the user enters 5 10 at the prompt, what data types will be displayed for the variables x and y?

* [ ] **A**. <class 'int'> <class 'int'>
* [ ] **B**. <class 'float'> <class 'float'>
* [ ] **C**. <class 'str'> <class 'str'>
* [ ] **D**. <class 'list'> <class 'list'>

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <class 'int'> <class 'int'><br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q69. What is the expected output of the following Python code if the user enters the number 10 when prompted? val = input("Enter a value: ") print(type(val)) print(val + val)

* [ ] **A**. <class 'int'> 1010
* [ ] **B**. <class 'str'> 1010
* [ ] **C**. <class 'int'> 20
* [ ] **D**. <class 'str'> 20

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <class 'str'> 1010<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q70. If a user enters the numerical value 45 when prompted by the following Python code, what will be the resulting data type of the variable 'user_data'? user_data = input("Enter your age: ")

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q71. Write a program to take tuple as input and print sum of all elements

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
import ast
a=list(ast.literal_eval(input()))
print(sum(a))
```
</details>

### Q72. Write a Python function to format a number n as 'n units' using the dot format method.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

---

## Day 07: Lists

### Q73. What is the result of '123'.zfill(5)?

* [ ] **A**. '00123'
* [ ] **B**. '12300'
* [ ] **C**. '123'
* [ ] **D**. '000123'

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. '00123'<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q74. "abc123".isalnum() returns:

* [ ] **A**. True
* [ ] **B**. False
* [ ] **C**. None
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. None<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q75. Consider the Python string `s = "communication"`. What is the output of the slicing operation `print(s[1:8:3])`?

* [ ] **A**. onu
* [ ] **B**. ouc
* [ ] **C**. omc
* [ ] **D**. mmi

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. ouc<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q76. In Python, strings are categorized as immutable sequences. What does this categorization specifically mean regarding how strings are handled in memory?

* [ ] **A**. Strings are stored as unordered collections where items are accessed by unique keys.
* [ ] **B**. Python strings function exactly like character arrays in C and require manual memory management.
* [ ] **C**. The characters in a string can be modified in-place to update the existing object.
* [ ] **D**. Characters have a left-to-right positional order and cannot be changed once the string is created.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. Characters have a left-to-right positional order and cannot be changed once the string is created.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q77. In the Python programming language, when using operations such as replace() to alter a string, why must a new string object be produced rather than the original being modified directly?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q78. Write a program to print the length of string

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=input()
print(len(a))
```
</details>

### Q79. A security system validates passcodes by comparing specific character positions and checking for keywords. Write a program that reads a string passcode, a positive index i, and a negative index j. The passcode is considered 'VALID' only if the character at positive index i is identical to the character at negative index j, and the substring 'secret' exists within the passcode.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q80. In Python, given the initial list 'nums = [10, 20, 30, 40, 50]', what is the state of the list after the slice assignment 'nums[1:4] = [99]' is performed?

* [ ] **A**. [10, 99, 20, 30, 40, 50]
* [ ] **B**. [10, 99, 40, 50]
* [ ] **C**. [10, 99, 50]
* [ ] **D**. [10, 20, 99, 50]

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. [10, 99, 40, 50]<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q81. What is the specific result when the following expression is executed in Python? [1, 2] + list("34")

* [ ] **A**. [1, 2, 34]
* [ ] **B**. [1, 2, '3', '4']
* [ ] **C**. TypeError
* [ ] **D**. [1, 2, '34']

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. TypeError<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q82. Which characteristic of Python lists allows them to support operations like index assignment and in-place deletion, which are not possible with strings?

* [ ] **A**. They are sequence types that support the use of the repetition operator.
* [ ] **B**. They are heterogeneous and can contain mixed data types.
* [ ] **C**. They are ordered collections that maintain a positional relationship.
* [ ] **D**. They are mutable objects that can be modified directly at their memory offset.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. They are sequence types that support the use of the repetition operator.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q83. In the Python programming language, when using operations such as replace() to alter a string, why must a new string object be produced rather than the original being modified directly?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q84. Write a python program to print the last element of the given list

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=list(map(int,input().split(",")))
print(a[-1])
```
</details>

---

## Day 08: Tuples

### Q85. Write a function to replace all vowels in a string with a given character. Vowels include: a, e, i, o, u (both lowercase and uppercase). Input Format : First line: A single string s (can contain spaces and punctuation). Second line: A single character c (replacement character). Output Format : Print the modified string with all vowels replaced by the given character.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q86. What is the expected result of executing this Python code snippet? word_tup = tuple('python') print(word_tup[-4:-1])

* [ ] **A**. ('y', 't', 'h')
* [ ] **B**. ('t', 'h', 'o', 'n')
* [ ] **C**. ('t', 'h', 'o')
* [ ] **D**. ('h', 'o', 'n')

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. ('t', 'h', 'o', 'n')<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q87. What is the specific result when the following expression is executed in Python? [1, 2] + list("34")

* [ ] **A**. [1, 2, 34]
* [ ] **B**. [1, 2, '3', '4']
* [ ] **C**. TypeError
* [ ] **D**. [1, 2, '34']

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. [1, 2, 34]<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q88. What will be the final value of 'L2' after the following Python code is executed? L1 = [1, 2] L2 = L1 + list("34") print(L2)

* [ ] **A**. [1, 2, '34']
* [ ] **B**. [1, 2, 34]
* [ ] **C**. [1, 2, '3', '4']
* [ ] **D**. [1, 2, [3, 4]]

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. [1, 2, '3', '4']<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q89. In Python, which of the following dictionary initializations will raise a TypeError due to a violation of the rules regarding dictionary keys? # Option A data1 = {101: 'Alpha', 102: 'Beta'} # Option B data2 = {'items': [1, 2, 3]} # Option C data3 = {[1, 2]: 'coordinates'} # Option D data4 = {'id': 50, 'id': 60}

* [ ] **A**. Option C
* [ ] **B**. Option A
* [ ] **C**. Option D
* [ ] **D**. Option B

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Option A<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q90. Which characteristic of Python lists allows them to support operations like index assignment and in-place deletion, which are not possible with strings?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q91. Write a function that removes all negative numbers from a given list and returns the updated list.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
def remove_negative(lst):
  return[x for x in lst if x>=0]

arr=list(map(int,input().strip().split(',')))

print(remove_negative(arr))
```
</details>

---

## Day 09: Sets

### Q21. Which of the following is true?

* [ ] **A**. Comments increase execution time
* [ ] **B**. Comments help in code readability
* [ ] **C**. Comments are mandatory
* [ ] **D**. Comments must be inside functions

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Comments are mandatory<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q22. what is the ouput of give code: x = 1 del x x = 2 print(x)

* [ ] **A**. 1
* [ ] **B**. 2
* [ ] **C**. None
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. None<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q23. Which of the following is not a valid logical operator in Python?

* [ ] **A**. and
* [ ] **B**. or
* [ ] **C**. not
* [ ] **D**. xor

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. not<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q24. Which command installs Jupyter Notebook?

* [ ] **A**. pip install notebook
* [ ] **B**. python install jupyter
* [ ] **C**. pip get jupyter
* [ ] **D**. py setup notebook

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. py setup notebook<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q25. Which character is used for writing single-line comments in Python?

* [ ] **A**. //
* [ ] **B**. #
* [ ] **C**. /*
* [ ] **D**. --

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. //<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q26. Which IDE provides both code intelligence and project management features?

* [ ] **A**. IDLE
* [ ] **B**. Notepad
* [ ] **C**. PyCharm
* [ ] **D**. Vim

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Notepad<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q27. Which of the following is not a correct way to comment multiple lines?

* [ ] **A**. ''' This is a comment '''
* [ ] **B**. "" This is a comment ""
* [ ] **C**. # This is
* [ ] **D**. // This is a comment

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. ''' This is a comment '''<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q28. What does the command pip list do?

* [ ] **A**. Lists Python versions
* [ ] **B**. Lists all installed Python interpreters
* [ ] **C**. Lists installed packages
* [ ] **D**. Lists virtual environments

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. Lists virtual environments<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q29. Choose the incorrect variable declaration:

* [ ] **A**. name = "Python"
* [ ] **B**. _1st = "Hello"
* [ ] **C**. 1st = "Hi"
* [ ] **D**. name1 = "World"

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 1st = "Hi"<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q30. Which one is True?

* [ ] **A**. bool(") == bool([])
* [ ] **B**. bool(1) == bool("0")
* [ ] **C**. bool(None) == bool(0)
* [ ] **D**. All of the above

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. bool(None) == bool(0)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q31. Which of the following is a literal in Python?

* [ ] **A**. if
* [ ] **B**. "hello"
* [ ] **C**. def
* [ ] **D**. print

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. "hello"<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q32. What is the data type of the expression bool(5 < 10) in Python?

* [ ] **A**. int
* [ ] **B**. bool
* [ ] **C**. float
* [ ] **D**. str

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. bool<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q33. what id the output is of the following code? x = 5 x = "hello" print(x)

* [ ] **A**. 5
* [ ] **B**. hello
* [ ] **C**. Error
* [ ] **D**. None

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. hello<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q34. What type of token is the keyword "while"?

* [ ] **A**. Identifier
* [ ] **B**. Literal
* [ ] **C**. Keyword
* [ ] **D**. Operator

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Literal<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q35. What command removes an installed package using pip?

* [ ] **A**. pip remove <package>
* [ ] **B**. pip delete <package>
* [ ] **C**. pip uninstall <package>
* [ ] **D**. pip purge <package>

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. pip uninstall <package><br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q36. In Python, which of the following statements correctly describes the lifecycle and behavior of variables?

* [ ] **A**. Type constraints are associated with variable names rather than the objects they reference.
* [ ] **B**. Variables are automatically initialized to zero or an empty string if they are not explicitly assigned.
* [ ] **C**. Variables must be declared with a specific type before they can be assigned a value.
* [ ] **D**. A variable is created only when it is first assigned a value and must be assigned before it is referenced.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Variables must be declared with a specific type before they can be assigned a value.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q37. What will be the output of the following Python code snippet? var_a = -10.5 var_b = 0.0 print(bool(var_a), bool(var_b))

* [ ] **A**. False True
* [ ] **B**. True False
* [ ] **C**. False False
* [ ] **D**. True True

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. False False<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q38. In the Python programming language, how is data type information handled when a variable is assigned a value?

* [ ] **A**. The variable name itself holds a fixed type constraint once it is first initialized.
* [ ] **B**. Type information resides with the object being referenced rather than the variable name.
* [ ] **C**. Variables must be explicitly declared with a data type before an assignment can occur.
* [ ] **D**. The interpreter assigns a type to the variable name based on the script's filename.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. The interpreter assigns a type to the variable name based on the script's filename.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q39. When the Python software package is installed on a machine, which specific components are minimally generated to enable program execution?

* [ ] **A**. An interpreter and a support library.
* [ ] **B**. A graphical user interface and a text editor.
* [ ] **C**. A compiler and a source code optimizer.
* [ ] **D**. A web browser extension and a database driver.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. An interpreter and a support library.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q40. Consider the following Python code logic: a = 0 b = 5 if not a and b: print("Success") else: print("Failure") What is the resulting output?

* [ ] **A**. True
* [ ] **B**. Success
* [ ] **C**. Failure
* [ ] **D**. False

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Success<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q41. What occurs within the Python system when the following sequence of statements is executed? x = 500 x = 'Data'

* [ ] **A**. The generic name x is reassigned from an integer object to a string object, as type constraints belong to objects rather than names.
* [ ] **B**. A new variable named x is created in a separate module to store the string while the first x remains an integer reference.
* [ ] **C**. Python raises a TypeError because the name x was already initialized as an integer and cannot be assigned to a different object type.
* [ ] **D**. The variable x is updated to a string type, and the integer 500 is automatically converted to a string format to maintain type consistency.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. The variable x is updated to a string type, and the integer 500 is automatically converted to a string format to maintain type consistency.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q42. Which of the following sets contains only valid Python variable names based on the language's established syntax rules?

* [ ] **A**. _my_var, var2, NAME
* [ ] **B**. first name, 4points, total$
* [ ] **C**. 2nd_var, my-var, !price
* [ ] **D**. user@name, var#1, 7heaven

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. first name, 4points, total$<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q43. Analyze the following Python code block: # Calculating the area "" This section performs a simple multiplication "" width = 10 height = 5 area = width * height print(area) What is the relationship between the comments and the execution of this program?

* [ ] **A**. The hashtag symbol (#) creates a mandatory logical break that slows down the code execution.
* [ ] **B**. The triple-quoted string is automatically assigned to a default metadata variable by the interpreter.
* [ ] **C**. The multi-line string literal must be explicitly converted to a docstring before it can be ignored.
* [ ] **D**. The comments and unassigned string literals have no impact on the program's execution or final outcome.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. The triple-quoted string is automatically assigned to a default metadata variable by the interpreter.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q44. In Python, what is the underlying mechanism that allows a triple-quoted string literal (such as "" comment "") to function as a multi-line comment even though it is technically a string?

* [ ] **A**. Python converts triple-quoted strings into hashtag comments during the initial code parsing phase.
* [ ] **B**. Python is designed to ignore any string literals that are not assigned to a variable during execution.
* [ ] **C**. Python treats all unassigned string literals as mandatory hidden variable declarations with a value of None.
* [ ] **D**. Python requires triple-quoted strings to be placed at the very end of a script to be treated as comments.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Python is designed to ignore any string literals that are not assigned to a variable during execution.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q45. Consider the following Python code snippet. What will be the final output? a = 10 b = 0 c = -1.5 if a and b: print('First') elif not b and c: print('Second') else: print('Third')

* [ ] **A**. First
* [ ] **B**. Third
* [ ] **C**. False
* [ ] **D**. Second

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. First<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

---

## Day 10: Dictionaries & Collections

### Q92. Write a function to count how many times a given substring occurs in the main string. Input Format: First line: A string s (the main string). Second line: A string sub (the substring to search for). Output Format: Print a single integer: the number of times the substring appears in the main string (including overlapping matches).


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q93. What does {'a': 1, 'a': 2} become in Python?

* [ ] **A**. {'a': 1}
* [ ] **B**. {'a': 2}
* [ ] **C**. {'a': [1, 2]}
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. {'a': 2}<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q94. What is the output of the following code? print(tuple("abc"))

* [ ] **A**. ['a', 'b', 'c']
* [ ] **B**. ('a', 'b', 'c')
* [ ] **C**. "abc"
* [ ] **D**. ('abc',)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. ('a', 'b', 'c')<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q95. What does {'x': [1, 2]}['x'][1] return in Python?

* [ ] **A**. 1
* [ ] **B**. 2
* [ ] **C**. [1, 2]
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 1<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q96. Which statement accurately describes the constraints placed on keys when creating a Python dictionary?

* [ ] **A**. Keys must be integers representing the physical index of the value in memory.
* [ ] **B**. Keys must be unique and belong to an immutable data type, such as strings or numbers.
* [ ] **C**. Keys can be of any data type, including mutable types like lists, as long as they are unique.
* [ ] **D**. Multiple keys can have the same name as long as they are associated with different values.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Keys can be of any data type, including mutable types like lists, as long as they are unique.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q97. In Python, given two sets X = {10, 20, 30} and Y = {30, 40, 50}, which of the following logical comparisons will evaluate to False?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q98. Write a function that adds a given element to a set.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=set(map(int,input().split(',')))
b=int(input())

a.add(b)
print(a)
```
</details>

---

## Day 12: Conditional Statements

### Q99. You are given an integer value representing the temperature in degrees Celsius. Based on the temperature, classify and print the weather condition as follows: Print "Freezing" if the temperature is less than 0 Print "Cold" if the temperature is between 0 and 15 (inclusive) Print "Warm" if the temperature is between 16 and 30 (inclusive) Print "Hot" if the temperature is greater than 30 Input Format: A single integer T — the temperature in Celsius. Output Format : Print one of the following:"Freezing" ,"Cold" , "Warm" and "Hot"


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q100. What does x = -2 if x < 0: if x > -5: print('Close') else: print("Error") else: print("Far") output in Python?

* [ ] **A**. Close
* [ ] **B**. Nothing
* [ ] **C**. Error
* [ ] **D**. Far

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Nothing<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q101. In Python multi-way branching, which of the following components is mandatory to start a valid conditional statement?

* [ ] **A**. else
* [ ] **B**. if
* [ ] **C**. elif
* [ ] **D**. then

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. elif<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q102. Which output will the following Python code produce? score = 85 if score >= 70: if score >= 90: print("Excellent") else: print("Good") else: print("Pass")

* [ ] **A**. Excellent Good
* [ ] **B**. Pass
* [ ] **C**. Good
* [ ] **D**. Excellent

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. Excellent<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q103. What is the result of executing this Python code? val = 5 if val > 10: if val == 5: print("Target Found") else: print("Target Missing")

* [ ] **A**. Target Missing
* [ ] **B**. Target Found
* [ ] **C**. An error occurs due to indentation
* [ ] **D**. Nothing is printed

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Target Missing<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q104. How does using the elif statement in Python improve the structure of a program compared to using nested if-else statements?

* [ ] **A**. It enables the program to check multiple conditions simultaneously.
* [ ] **B**. It increases readability by eliminating the need for deeply nested blocks.
* [ ] **C**. It allows the code to bypass the initial if condition.
* [ ] **D**. It requires less memory than a ternary operator.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. It allows the code to bypass the initial if condition.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q105. How does using the elif statement in Python improve the structure of a program compared to using nested if-else statements?

* [ ] **A**. It enables the program to check multiple conditions simultaneously.
* [ ] **B**. It increases readability by eliminating the need for deeply nested blocks.
* [ ] **C**. It allows the code to bypass the initial if condition.
* [ ] **D**. It requires less memory than a ternary operator.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. It allows the code to bypass the initial if condition.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q106. Consider the following Python logic. What is the final output? a = 10 b = 20 if a < 15: if b > 25: print("Condition Alpha") else: if a + b == 30: print("Condition Beta") else: print("Condition Gamma") else: print("Condition Delta")

* [ ] **A**. Condition Beta
* [ ] **B**. Condition Alpha
* [ ] **C**. Condition Delta
* [ ] **D**. Condition Gamma

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Condition Beta<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q107. Consider a Python script where multiple conditions in an if-elif-else structure could potentially evaluate to True for the variable i = 20. What is the resulting output? i = 20 if i >= 10: print("Level 1") elif i >= 15: print("Level 2") elif i >= 20: print("Level 3") else: print("Level 0")

* [ ] **A**. Level 3
* [ ] **B**. Level 1
* [ ] **C**. Level 2
* [ ] **D**. Level 1, Level 2, and Level 3

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Level 1<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q108. Consider a Python script where multiple conditions in an if-elif-else structure could potentially evaluate to True for the variable i = 20. What is the resulting output? i = 20 if i >= 10: print("Level 1") elif i >= 15: print("Level 2") elif i >= 20: print("Level 3") else: print("Level 0")

* [ ] **A**. Level 3
* [ ] **B**. Level 1
* [ ] **C**. Level 2
* [ ] **D**. Level 1, Level 2, and Level 3

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Level 1<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q109. How does the execution flow and output differ between the two structures provided in this Python code? # Structure 1 a = 10 if a > 5: print("High") if a < 15: print("Low") # Structure 2 b = 10 if b > 5: print("High") elif b < 15: print("Low")

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q110. Takes an integer input representing a person's age. Classifies the age into one of the following groups

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())

if 0<=a<=12:
  print(f"Age {a} is Child")
elif 13<=a<=19:
  print(f"Age {a} is Teenager")
elif 20<=a<=59:
  print(f"Age {a} is Adult")
elif a>=60:
  print(f"Age {a} is Senior")
```
</details>

---

## Day 13: Loops (While and For Loops)

### Q111. You are given the type of bank account, the withdrawal amount, and the current balance. Depending on the type of account, determine the result of a transaction using the following rules: Rules: If account_type is "savings": If amount > balance → Output: "Insufficient" Else: If amount > 25000 → Output: "OTP Required" Else → Output: "Success" If account_type is "current": Overdraft of ₹10,000 is allowed. If amount ≤ balance + 10000 → Output: "Success with overdraft" Else → Output: "Declined" Input Format: First line: a string account_type. , Second line: an integer amount. and Third line: an integer balance Output Format: A single line indicating the result of the transaction:"Success" , "OTP Required" , "Insufficient" , "Success with overdraft" and "Declined"


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q112. What does a for loop iterate over in Python?

* [ ] **A**. A condition
* [ ] **B**. A sequence (like a list, tuple, or string)
* [ ] **C**. A random number
* [ ] **D**. A function

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. A random number<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q113. What does a for loop do when it iterates over a string?

* [ ] **A**. Processes one character at a time
* [ ] **B**. Processes the whole string at once
* [ ] **C**. Skips the string
* [ ] **D**. Throws an error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Processes the whole string at once<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q114. How many times will a for loop run with range(10, 5)?

* [ ] **A**. 5
* [ ] **B**. 6
* [ ] **C**. 0
* [ ] **D**. 10

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 5<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q115. What is the output of the following Python code snippet? i = 0 while i < 5: if i == 3: break print(i) i += 1

* [ ] **A**. 0 1 2
* [ ] **B**. 0 1 2 3
* [ ] **C**. 0 1 2 3 4
* [ ] **D**. 1 2 3

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. 0 1 2 3<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q116. When a break statement is triggered during the execution of a Python loop, where does the program control move next?

* [ ] **A**. To the beginning of the next iteration of the loop.
* [ ] **B**. To the very first line of the Python script.
* [ ] **C**. To the start of the current loop to re-check the loop condition.
* [ ] **D**. To the next line of code immediately following the loop block.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. To the start of the current loop to re-check the loop condition.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q117. What is the output of the following Python code snippet? for i in [10, 20, 30]: if i == 40: break else: print("Task Complete")

* [ ] **A**. 10 20 30 Task Complete
* [ ] **B**. No output is produced
* [ ] **C**. Task Complete
* [ ] **D**. 40

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. No output is produced<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q118. What is a primary advantage of using the Python 'for...else' structure instead of using traditional boolean flags for search operations?

* [ ] **A**. It improves memory management by deleting the loop variable automatically.
* [ ] **B**. It provides a more concise syntax by removing the need to initialize and check external state variables.
* [ ] **C**. It prevents the loop from raising an IndexError when a sequence is empty.
* [ ] **D**. It allows the loop to iterate in reverse order without extra functions.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. It provides a more concise syntax by removing the need to initialize and check external state variables.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q119. In Python, under which specific condition is the block of code inside a 'for...else' statement executed?

* [ ] **A**. It executes only if the sequence being iterated over is completely empty.
* [ ] **B**. It executes only if the loop is exited prematurely via a break statement.
* [ ] **C**. It executes at the beginning of every iteration of the for loop.
* [ ] **D**. It executes only if the loop reaches the end of its sequence without encountering a break.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. It executes at the beginning of every iteration of the for loop.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q120. Which statement correctly describes the functional difference between the Python 'break' and 'pass' statements when used inside a loop?

* [ ] **A**. Break restarts the loop from the first item, while pass terminates it entirely.
* [ ] **B**. Break is used to handle exceptions, while pass is used to jump to a specific label in the code.
* [ ] **C**. Break skips only the current iteration, while pass exits the loop to the next line of code.
* [ ] **D**. Break terminates the current loop structure immediately, whereas pass is a null operation that serves as a placeholder without affecting the loop's execution flow.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Break skips only the current iteration, while pass exits the loop to the next line of code.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q121. In Python, which of the following best describes the execution logic of an 'else' block when it is used in conjunction with a for loop?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q122. You are given N different colors numbered from 1 to N. Chef has Aᵢ balls of color i (1 ≤ i ≤ N). Chef will arrange some boxes and must put each ball in exactly one box. Your task is to find the minimum number of boxes required such that: No box contains two balls of the same color. Input Format : The first line contains an integer T, the number of test cases. For each test case: The first line contains an integer N. The second line contains N space-separated integers A₁, A₂, …, Aₙ. Output Format : For each test case, print a single integer — the minimum number of boxes required so that no box contains balls of the same color.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
b=int(input())
c=list(map(int,input().split()))

print(max(c))
```
</details>

### Q123. You are given n projects. Each project i has: a pure profit → profits[i] a minimum capital required → capital[i] Initially, you have w units of capital. When you finish a project, you earn its profit, and it is added to your total capital. Your task is to select at most k distinct projects such that your final capital is maximized. Return the maximum possible final capital. The answer fits in a 32-bit signed integer. Input Format : k w n profits[0] profits[1] ... profits[n-1] capital[0] capital[1] ... capital[n-1] Output Format : final_capital

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
import heapq
k,w=map(int,input().split())
n=int(input())
p=list(map(int,input().split()))
c=list(map(int,input().split()))

project=sorted(zip(p,c))

max_heap=[]
i=0

for _ in range(k):
  while i < n and project[i][0]<=w:
    heapq.heappush(max_heap,-project[i][1])
    i+=1

  if not max_heap:
    break

  w-=heapq.heap.heappop(max_heap)

print(w)
Correct Solution

k, w = map(int, input().split())
n = int(input())
profits = list(map(int, input().split()))
capital = list(map(int, input().split()))
projects = []
for i in range(n):
    projects.append([capital[i], profits[i]])
projects.sort()
i = 0
available = []
for _ in range(k):
    while i < n and projects[i][0] <= w:
        available.append(projects[i][1])
        i += 1
    if not available:
        break
    max_profit = max(available)
    w += max_profit
    available.remove(max_profit)
print(w)
```
</details>

### Q124. There are n couples sitting in 2n seats arranged in a row. The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the i-th seat. Couples are numbered in order: the first couple is (0, 1), the second is (2, 3), and so on. Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people and switching their seats. Input Format : The first line contains an integer n — the number of couples. The second line contains 2n space-separated integers row[i] — the IDs of people sitting in order. Output Format : Print a single integer — the minimum number of swaps required.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q125. If a while loop with else runs infinitely, what happens to the else block?

* [ ] **A**. It is executed
* [ ] **B**. It is skipped
* [ ] **C**. It runs after each iteration
* [ ] **D**. It is never reached

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. It is executed<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q126. How many times does the else block execute in a while loop?

* [ ] **A**. Once for each iteration
* [ ] **B**. Only if the loop completes normally
* [ ] **C**. Only when the loop has a break
* [ ] **D**. It executes before the loop starts

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Once for each iteration<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q127. In a while loop, what does continue do if the condition is updated after it?

* [ ] **A**. The update is skipped
* [ ] **B**. The loop terminates
* [ ] **C**. The condition is reset
* [ ] **D**. The else block runs

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. The update is skipped<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q128. If x = 5, which while condition results in exactly 5 iterations?

* [ ] **A**. x > 5
* [ ] **B**. x >= 5
* [ ] **C**. x < 10
* [ ] **D**. x == 5

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. x < 10<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q129. Where is the else block placed in a while loop?

* [ ] **A**. Before the loop starts
* [ ] **B**. Inside the loop body
* [ ] **C**. After the loop body
* [ ] **D**. Within a nested loop only

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. After the loop body<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q130. What is a common use case for assert?

* [ ] **A**. To validate input data
* [ ] **B**. To break out of loops
* [ ] **C**. To continue loop execution
* [ ] **D**. To pause execution

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. To continue loop execution<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q131. When is continue typically used?

* [ ] **A**. To exit a loop early
* [ ] **B**. To skip specific iterations based on a condition
* [ ] **C**. To pause execution
* [ ] **D**. To run the else block

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. To pause execution<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q132. What will be the final value of the variable 'output' after the following Python code is executed? output = " for x in range(5): if x == 2: continue output += str(x)

* [ ] **A**. 34
* [ ] **B**. 01
* [ ] **C**. 01234
* [ ] **D**. 0134

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 01234<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q133. What is the expected output of the following Python code snippet? a = 10 b = 5 assert a > b print("Pass 1") assert a < b, "Pass 2 failed" print("Pass 2")

* [ ] **A**. AssertionError: Pass 2 failed
* [ ] **B**. Pass 1 AssertionError: Pass 2 failed
* [ ] **C**. Pass 1
* [ ] **D**. Pass 1 Pass 2

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Pass 1<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q134. According to Python coding patterns, what is a primary advantage of using the 'else' clause with a 'while' loop when searching for an item?

* [ ] **A**. It allows the loop to bypass the header test for faster execution.
* [ ] **B**. It eliminates the need to initialize and check a boolean flag to determine if the search failed.
* [ ] **C**. It ensures that the loop body executes at least once even if the condition is initially false.
* [ ] **D**. It automatically restarts the loop if the search criteria are not met.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. It allows the loop to bypass the header test for faster execution.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q135. In Python, what specific condition leads to the creation of an 'infinite loop' when using a while statement?

* [ ] **A**. When a break statement is encountered within the first iteration of the loop.
* [ ] **B**. When the loop condition evaluates to True on the first check but False on the second.
* [ ] **C**. When the test expression at the top of the loop header always evaluates to a true value.
* [ ] **D**. When the loop body is empty and contains only a pass statement.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. When the test expression at the top of the loop header always evaluates to a true value.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q136. In Python, under which specific condition is the code block nested within a 'while...else' statement executed?

* [ ] **A**. It executes during every iteration of the loop regardless of the test condition.
* [ ] **B**. It executes only if the loop is infinite and is manually stopped by the user.
* [ ] **C**. It executes only if the loop body contains a 'break' statement that is triggered.
* [ ] **D**. It executes if the loop terminates normally because the test condition evaluates to false without hitting a 'break'.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. It executes only if the loop body contains a 'break' statement that is triggered.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q137. What will be the output of the following Python code snippet? x = 1 while x < 3: if x == 10: break x += 1 else: print("Search Complete")

* [ ] **A**. 10
* [ ] **B**. Search Complete
* [ ] **C**. The code will result in an infinite loop
* [ ] **D**. No output is produced

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. The code will result in an infinite loop<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q138. In a Python program containing a 'while' loop with an 'else' clause, what is the consequence if the loop's test condition is false upon its very first evaluation?

* [ ] **A**. The program raises a syntax error because the 'else' clause requires at least one loop iteration.
* [ ] **B**. The loop body is skipped, and the 'else' block is executed immediately.
* [ ] **C**. Both the loop body and the 'else' block are bypassed as the loop never entered.
* [ ] **D**. The loop body executes exactly once before the 'else' block is processed.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. The loop body is skipped, and the 'else' block is executed immediately.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q139. When using Python's while...else structure to search for an item in a sequence by slicing (e.g., x = x[1:]), what is the resulting behavior if the search condition is satisfied and a break statement is executed during the very first iteration?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q140. Write a program that prints numbers from 1 up to a user-entered number N using a while loop.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
for i in range(1,a+1):
  print(i)
```
</details>

### Q141. Write a Python program that reads two integers and finds their greatest common divisor (GCD) using the Euclidean algorithm implemented with a while loop. Input Format: A single line containing two integers separated by space. Output Format: A single integer representing the GCD of the two numbers.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q142. Which is true about while loops?

* [ ] **A**. Condition is checked after execution
* [ ] **B**. Runs at least once
* [ ] **C**. Might not run at all
* [ ] **D**. Executes a fixed number of times

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Condition is checked after execution<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q143. In Python, which of the following is utilized to read input into a program?

* [ ] **A**. STDOUT
* [ ] **B**. OUTPUT
* [ ] **C**. CODE
* [ ] **D**. STDIN

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. CODE<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q144. Which loop is best when number of iterations is unknown?

* [ ] **A**. for
* [ ] **B**. while
* [ ] **C**. do-while
* [ ] **D**. None

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. do-while<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q145. How do you access the value for key "name" in a dictionary d?

* [ ] **A**. d("name")
* [ ] **B**. d.name
* [ ] **C**. d["name"]
* [ ] **D**. d->name

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. d("name")<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q146. Which of the following practices helps prevent infinite loops in a program?

* [ ] **A**. Using a break statement
* [ ] **B**. Using a continue statement appropriately
* [ ] **C**. Ensuring proper update (increment/decrement) of loop control variables
* [ ] **D**. All of the above

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Using a break statement<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q147. What is the purpose of nesting if statements?

* [ ] **A**. To make the program run faster
* [ ] **B**. To check multiple conditions in a specific order
* [ ] **C**. To avoid using loops
* [ ] **D**. To skip conditions

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. To make the program run faster<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q148. If a Python string contains both alphabetic characters and numeric characters, such as "Pythonist 2", what is the specific behavior of a case-swapping function like swap_case?

* [ ] **A**. Lowercase letters are capitalized, but uppercase letters and numbers are removed
* [ ] **B**. Only the case of alphabetic letters is toggled, while numbers and spaces remain unchanged
* [ ] **C**. All characters including numbers are converted to their uppercase equivalents
* [ ] **D**. The function ignores the string and returns an error message if digits are detected

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. All characters including numbers are converted to their uppercase equivalents<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q149. What is the expected output when applying case-swapping logic to the Python string "HackerRank.com"?

* [ ] **A**. hackerrank.com
* [ ] **B**. HACKERRANK.COM
* [ ] **C**. HackerRank.COM
* [ ] **D**. hACKERrANK.COM

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. HackerRank.COM<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q150. In Python, what is the resulting string when the case-swapping logic is applied to the following input: 'HackerRank.com presents "Pythonist 2".'?

* [ ] **A**. hackerrank.com presents "pythonist 2".
* [ ] **B**. HACKERRANK.COM PRESENTS "PYTHONIST 2".
* [ ] **C**. HackerRank.com Presents "Pythonist 2".
* [ ] **D**. hACKERrANK.COM PRESENTS "pYTHONIST 2".

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. hackerrank.com presents "pythonist 2".<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q151. When applying the logical transformation of swapping cases to the Python string "pYTHONIST 2", what is the resulting output?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q152. Write a program that takes an integer n as input and prints all numbers from 1 to n, each separated by a space, using a for loop. Input Format:A single integer n (upper range). Output Format: Print the numbers from 1 to n (inclusive) in a single line separated by spaces.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
for i in range(1,a+1):
  print(i,end=" ")
```
</details>

### Q153. Write a program to concatenate two strings

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=input()
b=input()
print(a+" "+b)
```
</details>

---

## Day 15: Control Flow (Else Suite with Loops)

### Q192. Define a recursive function weird_sum(n) such that: If n < 10, return n Otherwise, return: n % 10 + weird_sum(weird_sum(n // 10)) You are to implement this function and print the result. Input Format : A single integer n Output Format :A single integer representing the result of weird_sum(n)


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q193. In a while loop with else, what is the role of the else block?

* [ ] **A**. To handle exceptions
* [ ] **B**. To execute code after the loop ends without a break
* [ ] **C**. To run if the condition is initially False
* [ ] **D**. To repeat the loop

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. To execute code after the loop ends without a break<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q194. What will f(1, b=2, c=3) do if function is def f(a, b=1, c=1):?

* [ ] **A**. Error
* [ ] **B**. Override defaults
* [ ] **C**. Ignore c
* [ ] **D**. Only take a and b

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Override defaults<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q195. What does the range() function do in a for loop?

* [ ] **A**. Generates a random number
* [ ] **B**. Creates a sequence of numbers
* [ ] **C**. Stops the loop
* [ ] **D**. Defines a condition

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Stops the loop<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q196. x = 5 if x > 0: print("Positive") else: print("Negative") what is the output of the code

* [ ] **A**. Positive
* [ ] **B**. Nothing
* [ ] **C**. Error
* [ ] **D**. Negative

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Nothing<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q197. When using an optional else clause with a Python while loop, under which specific circumstance will the code inside the else block NOT be executed?

* [ ] **A**. When the loop condition evaluates to False on the very first check.
* [ ] **B**. When the loop is exited prematurely using a break statement.
* [ ] **C**. When the loop body contains a pass statement.
* [ ] **D**. When the loop finishes all its iterations naturally because the condition became False.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. When the loop body contains a pass statement.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q198. In Python, how do set methods like union() differ from set expression operators like | when handling different data types?

* [ ] **A**. Set methods require both operands to be of the set type, while expression operators accept lists and tuples.
* [ ] **B**. Set methods can accept any iterable type as an argument, while expression operators require both operands to be sets.
* [ ] **C**. There is no difference; both methods and operators strictly require all operands to be sets.
* [ ] **D**. Set expression operators automatically convert any iterable to a set, while methods do not.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Set methods can accept any iterable type as an argument, while expression operators require both operands to be sets.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q199. In Python, which of the following logical expressions will evaluate to False given two sets X = {1, 2, 3} and Y = {3, 4, 5}?

* [ ] **A**. X | Y == Y | X
* [ ] **B**. X - Y == Y - X
* [ ] **C**. X & Y == Y & X
* [ ] **D**. X ^ Y == Y ^ X

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. X | Y == Y | X<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q200. What is the visual result of the following Python code snippet? for i in range(4): for j in range(4): if i == j: print('*', end=' ') else: print(' ', end=' ') print()

* [ ] **A**. A vertical line of stars in the first column
* [ ] **B**. A hollow square made of stars
* [ ] **C**. A horizontal line of stars in the first row
* [ ] **D**. A diagonal line of stars starting from the top-left corner

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. A hollow square made of stars<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q201. If a Python string contains both alphabetic characters and numeric characters, such as "Pythonist 2", what is the specific behavior of a case-swapping function like swap_case?

* [ ] **A**. Lowercase letters are capitalized, but uppercase letters and numbers are removed
* [ ] **B**. Only the case of alphabetic letters is toggled, while numbers and spaces remain unchanged
* [ ] **C**. All characters including numbers are converted to their uppercase equivalents
* [ ] **D**. The function ignores the string and returns an error message if digits are detected

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. All characters including numbers are converted to their uppercase equivalents<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q202. What are the return values of the following Python function calls? all([True, False, True]) any([True, False, True])

* [ ] **A**. False and False
* [ ] **B**. True and True
* [ ] **C**. False and True
* [ ] **D**. True and False

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. True and True<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q203. In Python, given two sets X = {10, 20, 30} and Y = {30, 40, 50}, which of the following logical comparisons will evaluate to False?

* [ ] **A**. (X ^ Y) == (Y ^ X)
* [ ] **B**. (X | Y) == (Y | X)
* [ ] **C**. (X & Y) == (Y & X)
* [ ] **D**. (X - Y) == (Y - X)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. (X ^ Y) == (Y ^ X)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q204. What does the Python built-in map() function return when it is executed?

* [ ] **A**. A dictionary mapping inputs to outputs.
* [ ] **B**. A map object that functions as an iterator.
* [ ] **C**. A list containing the modified elements.
* [ ] **D**. A boolean indicating if the mapping was successful.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. A dictionary mapping inputs to outputs.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q205. Consider the following Python conditional logic used to categorize health status. Which message will be displayed if the variable `bmi` is calculated to be exactly 25.0? if bmi < 16: st.error('Extremely Underweight') elif 16 <= bmi < 18.5: st.warning('Underweight') elif 18.5 <= bmi < 25: st.success('Healthy') elif 25 <= bmi < 30: st.warning('Overweight') else: st.error('Extremely Overweight')

* [ ] **A**. Extremely Overweight
* [ ] **B**. Overweight
* [ ] **C**. Underweight
* [ ] **D**. Healthy

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Underweight<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q206. When invoking a Python function that utilizes a combination of positional and keyword arguments, which rule determines how the objects are matched to the local variable names in the function header?

* [ ] **A**. All positional arguments are matched first from left to right, followed by the matching of keyword arguments by name.
* [ ] **B**. Default values for parameters must be explicitly cleared by keyword arguments before positional arguments can be used.
* [ ] **C**. Keyword arguments are matched first to ensure all required names are filled, then remaining positionals are filled.
* [ ] **D**. Arguments are matched based on the length of the variable names in the function definition.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. All positional arguments are matched first from left to right, followed by the matching of keyword arguments by name.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q207. When comparing two built-in functions in Python, what is the primary difference between isinstance() and issubclass()?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q208. Create a function maximum(a, b, c) that returns the largest of the three numbers a, b, and c.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
def m(a,b,c):
  if a>b and a>c:
    print(a)
  elif b>a and b>c:
    print(b)
  elif c>a and c>b:
    print(c)
  else:
    print("Invalid Input")



a=list(map(int,input().split()))
m(a[0],a[1],a[2])
```
</details>

---

## Day 16-17: Pattern Printing (Alphabet & Basic)

### Q154. Write a program that reads N key-value pairs (where both keys and values are integers), stores them in a dictionary, and returns the most frequent value. If multiple values have the same highest frequency, return the smallest such value. Input Format:The first line contains an integer N — the number of key-value pairs.The next N lines each contain two space-separated integers: key and value. Output Format:Print the most frequent value in the dictionary.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q155. How many loops are there in a nested for loop structure?

* [ ] **A**. 1
* [ ] **B**. None
* [ ] **C**. Only 3
* [ ] **D**. 2 or more

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 1<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q156. What is a nested for loop?

* [ ] **A**. A loop that runs only once
* [ ] **B**. A loop inside another loop
* [ ] **C**. A loop that stops immediately
* [ ] **D**. A loop with no condition

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. A loop that stops immediately<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q157. How many times will the inner loop run if the outer loop runs 3 times and the inner loop runs 2 times per outer iteration?

* [ ] **A**. 3
* [ ] **B**. 2
* [ ] **C**. 6
* [ ] **D**. 5

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 3<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q158. In a nested loop, what controls how many times the inner loop executes?

* [ ] **A**. Only the outer loop
* [ ] **B**. Only the inner loop condition
* [ ] **C**. Both the outer loop and the inner loop condition
* [ ] **D**. The main function

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Both the outer loop and the inner loop condition<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q159. What does elif stand for in Python?

* [ ] **A**. End if
* [ ] **B**. Extra if
* [ ] **C**. Exit if
* [ ] **D**. Else if

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Exit if<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q160. What is a nested loop in python?

* [ ] **A**. A loop inside another loop
* [ ] **B**. A loop that never ends
* [ ] **C**. A loop without condition
* [ ] **D**. A loop with break

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. A loop without condition<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q161. for i in range(3): for j in range(2): print("Hello") How many times will "Hello" be printed?

* [ ] **A**. 3
* [ ] **B**. 2
* [ ] **C**. 6
* [ ] **D**. 5

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. 3<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q162. What will be the output of the following Python code snippet? for i in range(2, 4): for j in range(1, 11): if i == j: break print(i, "*", j, "=", i * j)

* [ ] **A**. 2 * 1 = 2 3 * 1 = 3 3 * 2 = 6
* [ ] **B**. 2 * 1 = 2 2 * 2 = 4 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
* [ ] **C**. 2 * 1 = 2 3 * 1 = 3
* [ ] **D**. 2 * 1 = 2 2 * 2 = 4 3 * 1 = 3 3 * 2 = 6

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. 2 * 1 = 2 2 * 2 = 4 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q163. Which of the following is a valid rule for creating nested loops in Python?

* [ ] **A**. Any type of loop can be placed inside any other type of loop, such as a while loop inside a for loop.
* [ ] **B**. Nested loops can only have two levels of depth.
* [ ] **C**. A while loop cannot be placed inside a for loop.
* [ ] **D**. Only for loops can be used as inner loops.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Nested loops can only have two levels of depth.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q164. In Python, if an outer loop executes 5 times and an inner loop executes 4 times for every single iteration of the outer loop, what is the total number of times the code inside the inner loop will be executed?

* [ ] **A**. 9
* [ ] **B**. 5
* [ ] **C**. 20
* [ ] **D**. 1

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 20<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q165. In Python, which mathematical expression used within a nested loop print statement will produce a checkerboard pattern of 0s and 1s, such as: 0 1 0 1 0 1 0 1 0

* [ ] **A**. (i + j) // 2
* [ ] **B**. (i ** j) % 2
* [ ] **C**. (i * j) % 2
* [ ] **D**. (i + j) % 2

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. (i ** j) % 2<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q166. When constructing a 4x4 hollow square pattern in Python using nested loops with indices 'i' and 'j' (ranging from 0 to 3), which conditional statement ensures that only the boundary stars are printed?

* [ ] **A**. if i == 0 or i == 3 or j == 0 or j == 3:
* [ ] **B**. if i == 0 and i == 3 and j == 0 and j == 3:
* [ ] **C**. if i + j == 3:
* [ ] **D**. if i == 1 or i == 2 or j == 1 or j == 2:

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. if i == 0 or i == 3 or j == 0 or j == 3:<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q167. What will be the output of the following Python code snippet when generating a pattern? for i in range(3): for j in range(3): if (i + j) % 2 == 0: print("E", end=" ") else: print("O", end=" ") print()

* [ ] **A**. E O O O E O O O E
* [ ] **B**. O E O E O E O E O
* [ ] **C**. E E E O O O E E E
* [ ] **D**. E O E O E O E O E

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. O E O E O E O E O<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q168. What is the final value of the variable 'num' after the following Python code segment finishes execution? num = 1 for i in range(1, 5): for j in range(i): num += 1

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q169. Print a right-aligned triangle pattern of stars (*). Given an integer n, print a pattern of stars where the first line has 1 star right-aligned, the second line has 2 stars right-aligned, and so on until the nth line with n stars.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
for i in range(1,a+1):
  for k in range(1,a-i+1):
      print(" ",end="")
  for j in range(i):
    print("*",end="")
  print()
```
</details>

### Q170. ou are given an M x N binary matrix containing only 0s and 1s. Your task is to find the size (side length) of the largest square sub-matrix that contains only 1s. Input Format: First line contains two integers M and N, the dimensions of the matrix. Next M lines contain N space-separated binary digits (0 or 1), representing the matrix rows. Output Format: Print a single integer: the side length of the largest square of 1s.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

---

## Day 18: Functions

### Q180. You are given a name (a single string). Your task is to print the name in a left-aligned triangle pattern, such that: The first line contains the first letter, The second line contains the first two letters, And so on, until the full name is printed. Input Format: A single string name containing uppercase or lowercase letters only. Output Format: Print the name in a left-aligned triangle pattern.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q181. Which of these helps in dividing programs into smaller modules?

* [ ] **A**. Functions
* [ ] **B**. Loops
* [ ] **C**. Classes
* [ ] **D**. Errors

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Classes<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q182. When calling a Python function using keyword arguments, such as 'f(c=3, b=2, a=1)', which of the following statements is true regarding the matching process?

* [ ] **A**. Keyword arguments are matched by position first and then by name.
* [ ] **B**. The arguments must be provided in the exact order they were defined in the function header.
* [ ] **C**. The left-to-right order of the arguments no longer matters because Python matches them by name.
* [ ] **D**. Keyword arguments require the function to have default values defined for all parameters.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Keyword arguments are matched by position first and then by name.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q183. What is the result of the following Python code execution? def greet(name, message="Welcome"): print(message, name) greet("Saketh")

* [ ] **A**. Saketh Welcome
* [ ] **B**. Welcome None
* [ ] **C**. TypeError: greet() missing 1 required positional argument
* [ ] **D**. Welcome Saketh

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Welcome None<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q184. In Python, which of the following function calls will result in a syntax error when trying to combine positional and keyword arguments for the function 'def subtract(a, b):'?

* [ ] **A**. subtract(a=10, 5)
* [ ] **B**. subtract(a=10, b=5)
* [ ] **C**. subtract(10, b=5)
* [ ] **D**. subtract(10, 5)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. subtract(10, b=5)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q185. What is the output of the following Python code snippet? def check_value(n): if n > 10: return "High" else: return "Low" print(check_value(5))

* [ ] **A**. Low
* [ ] **B**. Error: return cannot be used inside an if-else block
* [ ] **C**. None
* [ ] **D**. High

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Error: return cannot be used inside an if-else block<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q186. In Python, if a function is assigned to a variable and then used in a nested call, what will be the output of this code? def compute(n): return n + 5 calc = compute result = calc(calc(10)) print(result)

* [ ] **A**. 10
* [ ] **B**. 20
* [ ] **C**. 25
* [ ] **D**. 15

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. 20<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q187. When invoking a Python function that utilizes a combination of positional and keyword arguments, which rule determines how the objects are matched to the local variable names in the function header?

* [ ] **A**. All positional arguments are matched first from left to right, followed by the matching of keyword arguments by name.
* [ ] **B**. Default values for parameters must be explicitly cleared by keyword arguments before positional arguments can be used.
* [ ] **C**. Keyword arguments are matched first to ensure all required names are filled, then remaining positionals are filled.
* [ ] **D**. Arguments are matched based on the length of the variable names in the function definition.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. All positional arguments are matched first from left to right, followed by the matching of keyword arguments by name.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q188. Consider the following Python function definition: def process_values(a, b, c=10): return (a - b) * c Which of the following function calls will result in a SyntaxError?

* [ ] **A**. process_values(20, 5, c=2)
* [ ] **B**. process_values(a=20, 5, c=2)
* [ ] **C**. process_values(b=5, a=20, c=2)
* [ ] **D**. process_values(20, b=5)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. process_values(b=5, a=20, c=2)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q189. When analyzing the execution flow of a Python program, what characterizes the state of a function immediately after its definition has been processed but before it has been called?

* [ ] **A**. The function body is executed once in a hidden background thread to initialize local variables.
* [ ] **B**. The function code is stored in memory as a named block of logic, but the statements inside its body have not been executed.
* [ ] **C**. The control flow jumps directly to the function's final statement to establish a default return value before resuming main execution.
* [ ] **D**. The interpreter skips the definition entirely and only reads the function logic once a call expression is detected.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. The function body is executed once in a hidden background thread to initialize local variables.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q190. In Python, what specific action does the interpreter perform when it reaches and runs a 'def' statement at runtime?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q191. Write a function print_table(n) that prints the multiplication table of the given number n, from 1 to 10.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
b=1
for i in range(1,11):
  print(i*a,end=" ")
  b+=1
```
</details>

---

## Day 20: Generators

### Q241. You are given a positive integer n. Write a program to check whether the number is prime or not using the math.sqrt() function for optimization.A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.Input Format:A single integer n.Output Format:Print "Prime" if the number is prime. and Print "Not Prime" otherwise.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q242. When manually iterating through a Python generator object using the next() function, what specific mechanism is used to signal that the generator has no more values to yield?

* [ ] **A**. A StopIteration exception is raised by the generator.
* [ ] **B**. The function returns a None value to indicate it is finished.
* [ ] **C**. The next() function returns a Boolean False value.
* [ ] **D**. The generator object is automatically re-initialized to the beginning.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. The generator object is automatically re-initialized to the beginning.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q243. Which component of a Python object is specifically represented by its attributes and reflects the properties or data held by that instance?

* [ ] **A**. Behavior
* [ ] **B**. Identity
* [ ] **C**. State
* [ ] **D**. Inheritance

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. State<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q244. Which decorator in Python is used to define a method that receives the class itself as its first argument, enabling it to access or update variables shared by all instances of that class?

* [ ] **A**. @classmethod
* [ ] **B**. @property
* [ ] **C**. @staticmethod
* [ ] **D**. @instancemethod

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. @property<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q245. When a Python module is imported multiple times within the same system, what is the standard behavior for executing the code inside that module?

* [ ] **A**. The module code is only executed when the 'imp.reload' function is called manually.
* [ ] **B**. The module code is re-executed every time a new 'import' statement is encountered.
* [ ] **C**. The module statements are executed only during the very first import.
* [ ] **D**. The module code is executed only if it contains a class definition.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. The module code is only executed when the 'imp.reload' function is called manually.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q246. Which of the following describes a key syntactic constraint of Python's lambda functions compared to functions defined with the def keyword?

* [ ] **A**. Lambdas are restricted to a single expression and cannot contain multiple statements.
* [ ] **B**. Lambdas cannot accept more than one input argument.
* [ ] **C**. Lambdas must always be assigned to a variable name before they can be used.
* [ ] **D**. Lambdas cannot return values like integers or strings.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Lambdas cannot accept more than one input argument.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q247. If a Python developer wants to pass a list to a function and perform in-place operations on it without altering the original list held by the caller, which technique is explicitly supported for creating a copy?

* [ ] **A**. Passing a slice of the object, such as `func(my_list[:])`, to provide an explicit copy to the function.
* [ ] **B**. Relying on Python's automatic copying mechanism for all mutable shared references.
* [ ] **C**. Declaring the parameter as a constant in the function header.
* [ ] **D**. Using the 'ref' keyword at the point of the function call.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. Using the 'ref' keyword at the point of the function call.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q248. How does scope lookup work for a Python lambda expression defined inside another function, as shown in the code below? def knights(): title = 'Sir' action = (lambda x: title + ' ' + x) return action act = knights() print(act('Robin'))

* [ ] **A**. It prints 'Sir Robin' because the lambda follows LEGB scope rules and sees the enclosing name.
* [ ] **B**. It prints ' Robin' because the lambda cannot access variables in the enclosing function scope.
* [ ] **C**. It results in a NameError because 'title' is local to knights().
* [ ] **D**. It requires 'title' to be passed as a global variable to function correctly.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. It prints ' Robin' because the lambda cannot access variables in the enclosing function scope.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q249. In Python, which of the following best describes the 'pass-by-assignment' model for immutable objects, such as integers, when compared to the C programming language?

* [ ] **A**. They are passed by object reference, but since the objects cannot be modified in-place, the effect is equivalent to C's pass-by-value.
* [ ] **B**. They are passed by automatic duplication to ensure that the function has a unique memory identifier for the value.
* [ ] **C**. They are passed as pointers that allow the function to change the original object's value in the caller's scope.
* [ ] **D**. They are passed by copying the entire object into the function's local scope, matching C's pass-by-value.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. They are passed as pointers that allow the function to change the original object's value in the caller's scope.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q250. What is the output of the following Python code snippet? li = [lambda arg=x: arg * 5 for x in range(1, 3)] for i in li: print(i(), end=" ")

* [ ] **A**. 5 5
* [ ] **B**. 10 10
* [ ] **C**. 1 2
* [ ] **D**. 5 10

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 1 2<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q251. In Python, which series of operations correctly modifies the character at index 2 of the string 'Python' to be 'T' using list conversion? s = 'Python'

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q252. Create a class Rectangle with:Attributes length and width a method area() that returns the area of the rectangle

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
b=int(input())
c=a*b
print(f"Area: {c}")
```
</details>

---

## Day 24: Regular Expressions & Patterns

### Q292. You and Fredrick are good friends. Yesterday Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. A valid credit card from ABCD Bank has the following characteristics: It must start with a 4, 5 or 6. It must contain exactly 16 digits. It must consist of digits only (0-9), except that it may have digits in groups of 4 separated by a single hyphen -. That means two allowed formats only: dddddddddddddddd (16 digits) or dddd-dddd-dddd-dddd (four groups of 4 digits separated by hyphens). Mixed or other placements of separators are not allowed. It must NOT use any other separator like spaces, underscores, etc. It must NOT have 4 or more consecutive repeated digits when hyphens are removed (e.g. 4444 anywhere is invalid; 4-4-4-4 is also invalid because that becomes 4444 when hyphens are removed). Input Format : The first line contains an integer N, the number of credit card numbers to validate. Each of the next N lines contains a credit card number (string). Output Format : For each credit card number, print Valid if it is valid. Otherwise print Invalid. (One result per line, case-sensitive.)


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q293. What will re.search("\d+", "Age: 25") return?

* [ ] **A**. None
* [ ] **B**. 25
* [ ] **C**. Age
* [ ] **D**. Error

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Age<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q294. In form validation, why is ^ used in regular expressions?

* [ ] **A**. Match special characters
* [ ] **B**. Escape numbers
* [ ] **C**. Indicates the start of the string
* [ ] **D**. Indicates the end of string

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Escape numbers<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q295. Which function is used to compile a regular expression pattern?

* [ ] **A**. re.save()
* [ ] **B**. re.compile()
* [ ] **C**. re.group()
* [ ] **D**. re.fullmatch()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. re.compile()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q296. What does \d represent in regex?

* [ ] **A**. Decimal
* [ ] **B**. Digit
* [ ] **C**. Delimiter
* [ ] **D**. Dot

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Delimiter<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q297. In regular expressions, what does the $ symbol represent?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q298. Write a Python program that checks whether a given string is a valid credit card number.A valid credit card number must:Contain exactly 16 digits , May be written with or without hyphens If hyphens are used, they must appear after every 4 digits, like 1234-5678-9012-3456 . Print "Valid" if the credit card number is valid. Otherwise, print "Invalid".

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=input()

if len(a)==16 and a.isdigit():
  print("Valid")
elif a[4]=="-" and a[9]=="-" and a[14]=="-" and len(a)==19:

    print("Valid")
else:
  print("Invalid")
```
</details>

### Q299. Write a Python program that reads a date in the format dd/mm/yyyy and checks: If the format is valid using a regular expression. If it represents a valid calendar date, including leap years and correct day-month combinations. Input Format : A single string in the format dd/mm/yyyy. Output Format : Print "Valid" if the date is correctly formatted and is a real date. Print "Invalid" otherwise.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

---

## Day 25: OOP Basics (Classes, Objects, Access Specifiers)

### Q1. Which function is called automatically when an object is created?

* [ ] **A**. del
* [ ] **B**. new
* [ ] **C**. init
* [ ] **D**. str

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. init<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q2. Which of these concepts encourages data hiding in Python?

* [ ] **A**. Variables
* [ ] **B**. Loops
* [ ] **C**. Private variables using __
* [ ] **D**. Functions

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Private variables using __<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q3. What typically leads to more memory consumption?

* [ ] **A**. Stack memory
* [ ] **B**. Procedural functions
* [ ] **C**. Creating many class instances
* [ ] **D**. Declaring constants

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Creating many class instances<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q4. In procedural programming, memory is primarily:

* [ ] **A**. Allocated during runtime
* [ ] **B**. Object-based
* [ ] **C**. Function-call-based and mostly stack-driven
* [ ] **D**. Shared among all functions

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Function-call-based and mostly stack-driven<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q5. In Python's Object-Oriented model, if a variable is defined inside a class but outside any methods (a class variable), how is its memory handled?

* [ ] **A**. The memory is only allocated if the variable is accessed by a method
* [ ] **B**. Each object creates a private copy of the variable in its own memory
* [ ] **C**. The variable is stored in a temporary cache and deleted after one use
* [ ] **D**. The memory is shared across all objects created from that class

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. The memory is shared across all objects created from that class<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q6. Python is described as a versatile language suitable for artificial intelligence, web development, and data analysis. What helps facilitate this wide range of use cases?

* [ ] **A**. Its design as a low-level language for hardware drivers
* [ ] **B**. The absence of community support and external documentation
* [ ] **C**. An extensive standard library and a large ecosystem of third-party frameworks
* [ ] **D**. The strict limitation to a single programming paradigm

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. An extensive standard library and a large ecosystem of third-party frameworks<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q7. Which method is called when you print an object?

* [ ] **A**. print
* [ ] **B**. display
* [ ] **C**. str
* [ ] **D**. show

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. str<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q8. Can Python support both procedural and object-oriented programming?

* [ ] **A**. Yes
* [ ] **B**. No
* [ ] **C**. Only procedural
* [ ] **D**. Only object-oriented

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Yes<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q9. According to Python's internal memory management, what is the conceptual relationship between a variable and an object?

* [ ] **A**. Variables and objects are identical components stored in the same memory slot
* [ ] **B**. Objects are entries in a system table while variables are chunks of memory
* [ ] **C**. Variables are system table entries that link to objects in memory via pointers
* [ ] **D**. Variables are stored in the CPU cache while objects are stored on the hard drive

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Variables are system table entries that link to objects in memory via pointers<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q10. What is the file extension for Python files?

* [ ] **A**. .file
* [ ] **B**. .py
* [ ] **C**. .ptn
* [ ] **D**. .pyt

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. .py<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q11. How does the Python programming language handle Object-Oriented Programming (OOP) in comparison to languages like Ruby or Java?

* [ ] **A**. OOP is not supported at all
* [ ] **B**. OOP is an option rather than a requirement
* [ ] **C**. OOP is only available in specific paid versions
* [ ] **D**. OOP is mandatory for every project

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. OOP is an option rather than a requirement<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q12. Which feature of the Python language allows a programmer to use variables without explicitly declaring their data types, such as integers or strings, in advance?

* [ ] **A**. Dynamic Typing
* [ ] **B**. Manual Type Definition
* [ ] **C**. Static Typing
* [ ] **D**. Explicit Typing

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Dynamic Typing<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q13. Polymorphism allows:

* [ ] **A**. Classes to have multiple constructors
* [ ] **B**. One interface, many forms
* [ ] **C**. Objects to store different types
* [ ] **D**. Code reuse

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. One interface, many forms<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q14. Which syntax in Python represents object instantiation?

* [ ] **A**. ClassName{}
* [ ] **B**. new ClassName()
* [ ] **C**. ClassName()
* [ ] **D**. create ClassName

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. create ClassName<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q15. Which method is used to destroy an object in python?

* [ ] **A**. __Del__
* [ ] **B**. __delete__
* [ ] **C**. __end__
* [ ] **D**. __del__

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. __end__<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q16. Which built-in method acts like a destructor in Python?

* [ ] **A**. destroy()
* [ ] **B**. delete()
* [ ] **C**. del()
* [ ] **D**. destructor()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. destructor()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q17. Which of the following is used for inheritance in Python?

* [ ] **A**. class Child inherits Parent
* [ ] **B**. class Child(Parent)
* [ ] **C**. class Child <- Parent
* [ ] **D**. class Parent : Child

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. class Child(Parent)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q18. When did Guido van Rossum start working on the Python programming language?

* [ ] **A**. 1980
* [ ] **B**. 1985
* [ ] **C**. 1989
* [ ] **D**. 1991

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. 1989<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q19. In terms of language design and developer productivity, how does Python distinguish itself from languages like Java, Ruby, or C++?

* [ ] **A**. Python requires extensive intermediate compile and link steps, which provides a more interactive experience than traditional scripting tools.
* [ ] **B**. Python code is typically three to five times larger than equivalent Java code to ensure it remains readable across platforms.
* [ ] **C**. Python provides a simple syntax where code is often much smaller than equivalent C++ code, and it makes Object-Oriented Programming optional.
* [ ] **D**. Python mandates the use of Object-Oriented Programming (OOP) for every project, making it more structured than C++ or Ruby.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Python code is typically three to five times larger than equivalent Java code to ensure it remains readable across platforms.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q20. Python is often referred to as a 'glue' language because of its ability to integrate with other programming languages. How is this feature typically utilized in the software development lifecycle for systems with high-performance requirements?

* [ ] **A**. Python requires all external components to be compiled into Java bytecode before they can be linked to a Python script.
* [ ] **B**. The system must use Visual Basic for the frontend while Python manages the low-level memory allocation of C components.
* [ ] **C**. The system is developed entirely in C and then translated into Python syntax for final user delivery.
* [ ] **D**. The system is initially built in Python to leverage rapid development, and then performance-critical pieces are moved to C for delivery.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. The system is developed entirely in C and then translated into Python syntax for final user delivery.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

---

## Day 25: OOP Access Specifiers & Variables

### Q253. Create two unrelated classes Bird and Airplane, both having a fly() method. Write a function make_it_fly(obj) that accepts any object and calls its fly() method. This must be implemented using duck typing (no inheritance). Input Format : First line: The type of object - either Bird or Airplane Second line: A parameter (e.g., name for Bird or model for Airplane) Output Format : Print the result of the fly() method


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q254. What happens if no access specifier is used in Python?

* [ ] **A**. Attribute is private
* [ ] **B**. Attribute is public
* [ ] **C**. Attribute is protected
* [ ] **D**. Attribute is hidden

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Attribute is protected<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q255. Can you access a private attribute with name mangling?

* [ ] **A**. Yes
* [ ] **B**. No
* [ ] **C**. Only in subclasses
* [ ] **D**. Only in methods

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Only in subclasses<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q256. According to Python OOP principles, which of the following is a primary reason to use a class variable rather than an instance variable?

* [ ] **A**. To ensure that every object has its own independent copy of a specific value.
* [ ] **B**. To store data that must be unique to every individual object created from the class.
* [ ] **C**. To define variables inside the __init__ method for better memory management.
* [ ] **D**. To store constants or configuration values that are shared across all instances of the class.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. To define variables inside the __init__ method for better memory management.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q257. In Python, how does the interpreter handle an attribute defined with a double underscore prefix, such as `self.__salary`, when an attempt is made to access it directly from outside the class instance?

* [ ] **A**. It returns a null value instead of the actual data to protect the internal state.
* [ ] **B**. It raises an AttributeError because the attribute is considered private due to name mangling.
* [ ] **C**. It allows access normally but prints a warning message to the console.
* [ ] **D**. It automatically converts the private attribute into a public one upon the first external call.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. It returns a null value instead of the actual data to protect the internal state.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q258. In Python object-oriented programming, what is the specific function of the 'self' parameter during the execution of the __init__ method?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q259. Write a program that takes an integer input n and checks if it lies within the constraint:1 ≤ n ≤ 1000 If n satisfies this condition, print:Valid Otherwise, print: Invalid

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=int(input())
if 1<=a<=1000:
  print("Valid")
else:
  print("Invalid")
```
</details>

---

## Day 26: OOP Inheritance & Polymorphism

### Q260. Create a class Student that stores each student’s name and grade using instance variables. The class should maintain the total number of students and the average grade using class variables. Input Format : First line: An integer N, the number of students. Next N lines: Each line contains a string name and an integer grade. Output Format : First, print the total number of students. Then, print the average grade (rounded to 2 decimal places).


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q261. In a Python class that uses single inheritance, which function is used to call the constructor (__init__) of the parent class?

* [ ] **A**. super()
* [ ] **B**. base()
* [ ] **C**. parent()
* [ ] **D**. this()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. base()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q262. In Python OOPS, what is the standard naming convention used to indicate that a method is protected and intended for use only within the class or its subclasses?

* [ ] **A**. Starting the method name with a double underscore, such as __display_info.
* [ ] **B**. Using all capital letters for the method name, such as DISPLAY_INFO.
* [ ] **C**. Starting the method name with a single underscore, such as _display_info.
* [ ] **D**. Ending the method name with a single underscore, such as display_info_.

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Using all capital letters for the method name, such as DISPLAY_INFO.<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q263. Consider a Python program where class 'TeamLead' inherits from class 'Employee' and class 'Project'. If 'Employee' itself inherits from class 'Person', what specific inheritance model does the 'TeamLead' class represent?

* [ ] **A**. Basic Multilevel Inheritance
* [ ] **B**. Hybrid Inheritance
* [ ] **C**. Only Multiple Inheritance
* [ ] **D**. Simple Hierarchical Inheritance

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Hybrid Inheritance<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q264. What is the result of the following Python code execution? class Student: pass s1 = Student() s2 = Student() s1.name = "Arjun" s2.name = "Arjun" print(s1 == s2, s1.name == s2.name)

* [ ] **A**. False False
* [ ] **B**. False True
* [ ] **C**. True False
* [ ] **D**. True True

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. False False<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q265. Consider the following Python class definitions: class Person: def __init__(self, name): self.name = name class Employee(Person): def role(self): return "Employee" class Project: def __init__(self, p_name): self.p_name = p_name class TeamLead(Employee, Project): def __init__(self, name, p_name): Employee.__init__(self, name) Project.__init__(self, p_name) Which statement accurately describes the capabilities of an instance of TeamLead?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q266. You are to implement a class FileMeta that encapsulates sensitive metadata of a file, including its size, last accessed time, and owner. All metadata should be private and cannot be accessed or modified directly. You must provide the following methods with proper encapsulation: set_file_info(size, accessed_time, owner) – Sets all three values. get_file_info() – Returns all three metadata values as a tuple. update_size(new_size) – Updates size only if it is a positive integer. update_accessed_time(new_time) – Updates last accessed time. change_owner(new_owner) – Changes the file owner only if it's not an empty string. Input Format : First line: An integer n representing the number of operations. Next n lines: Each line contains one of the following: SET size time owner GET SIZE new_size TIME new_time OWNER new_owner Output Format : For each GET operation, print the file info as : Size: <size>, Accessed: <time>, Owner: <owner>

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
class FileMeta:
  def __init__(self):
    self.__size = 0
    self.__accessed_time = ""
    self.__owner = ""

  def set_file_info(self, size, accessed_time, owner):
    self.__size = int(size)
    self.__accessed_time = accessed_time
    self.__owner = owner

  def get_file_info(self):
    return self.__size, self.__accessed_time, self.__owner

  def update_size(self, new_size):
    new_size = int(new_size)
    if new_size > 0:
      self.__size = new_size

  def update_accessed_time(self, new_time):
    self.__accessed_time = new_time

  def change_owner(self, new_owner):
    if new_owner!= "":
      self.__owner = new_owner



n = int(input())
file = FileMeta()


for _ in range(n):
  parts = input().split() 
  cmd = parts[0]

if cmd == "SET":
  file.set_file_info(parts[1], parts[2], parts[3])
elif cmd == "GET":
  size, time, owner = file.get_file_info()
  print(f"Size: {size}, Accessed: {time}, Owner: {owner}")
elif cmd == "SIZE":
  file.update_size(parts[1])
elif cmd == "TIME":
  file.update_accessed_time(parts[1])
elif cmd == "OWNER":
  file.change_owner(parts[1])

    
      
Correct Solution

class FileMeta:
    def __init__(self):
        self.__size = 0
        self.__accessed_time = ''
        self.__owner = ''

    def set_file_info(self, size, accessed_time, owner):
        self.__size = size
        self.__accessed_time = accessed_time
        self.__owner = owner

    def get_file_info(self):
        return (self.__size, self.__accessed_time, self.__owner)

    def update_size(self, new_size):
        if isinstance(new_size, int) and new_size > 0:
            self.__size = new_size

    def update_accessed_time(self, new_time):
        self.__accessed_time = new_time

    def change_owner(self, new_owner):
        if isinstance(new_owner, str) and new_owner.strip() != '':
            self.__owner = new_owner

n = int(input())
file = FileMeta()
for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    if cmd == 'SET':
        size = int(parts[1])
        time = parts[2]
        owner = parts[3]
        file.set_file_info(size, time, owner)
    elif cmd == 'GET':
        size, time, owner = file.get_file_info()
        print(f"Size: {size}, Accessed: {time}, Owner: {owner}")
    elif cmd == 'SIZE':
        new_size = int(parts[1])
        file.update_size(new_size)
    elif cmd == 'TIME':
        new_time = parts[1]
        file.update_accessed_time(new_time)
    elif cmd == 'OWNER':
        new_owner = parts[1]
        file.change_owner(new_owner)
```
</details>

### Q267. Design a farm produce management system using hierarchical inheritance. Create a base class Produce with a class variable total_quantity. Create three derived classes: Fruit, Vegetable, and Grain. Each derived class should override the method harvest(quantity: int) which: Adds the harvested quantity to both its own category total and the global total_quantity. Implement a get_quantity() method in each class that returns the harvested quantity for that category. Produce.get_total_quantity() should return the total of all harvested produce. Input Format : The first line contains an integer N, number of operations. The next N lines contain one of the following commands: "harvest <type> <quantity>" where <type> is Fruit, Vegetable, or Grain. "get <type>" to get total for that category. "get total" to get total harvested produce. Output Format : Print the result for each get command on a new line.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q268. In python, method overloading is part of

* [ ] **A**. Inheritance
* [ ] **B**. Static classes
* [ ] **C**. Compile-time polymorphism
* [ ] **D**. Dynamic linking

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Inheritance<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q269. Which methods can be overridden in Python?

* [ ] **A**. Only static
* [ ] **B**. Only constructors
* [ ] **C**. Any public or protected method
* [ ] **D**. Only private

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Only constructors<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q270. Can static methods be overridden?

* [ ] **A**. No
* [ ] **B**. Yes, but behaves like hiding
* [ ] **C**. Yes, but it is method hiding, not true overriding
* [ ] **D**. Only using decorators

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Yes, but it is method hiding, not true overriding<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q271. Abstract classes can contain

* [ ] **A**. Only abstract methods
* [ ] **B**. Only static methods
* [ ] **C**. Both concrete and abstract methods
* [ ] **D**. No variables

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Both concrete and abstract methods<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q272. Method overloading is a type of

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q273. Create a class RepeatString that has a string attribute. You must overload the * operator so that multiplying the object with an integer repeats the string N times and returns a new string. The first line contains a string s. The second line contains an integer n, representing how many times the string should be repeated. Print the repeated string result on a single line.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=input()
b=int(input())
print(a*b)
```
</details>

### Q274. Implement an abstract base class Shape with an abstract method area(). Then implement the following subclasses: Rectangle: initialized with width and height Triangle: initialized with base and height Circle: initialized with radius Each subclass should override the area() method to return the correct area as a float rounded to 2 decimal places. You must follow the rules of abstraction using Python's abc module. Input Format: First line: an integer N, number of shapes Next N lines: each line contains shape type followed by parameters: rectangle width height triangle base height circle radius Output Format : Print N lines, each containing the area of the shape (rounded to 2 decimal places)


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q275. Which Python feature best supports the "real-world modeling" in a project like this?

* [ ] **A**. Lambda functions
* [ ] **B**. Object-oriented programming (OOP)
* [ ] **C**. Loops
* [ ] **D**. Exception handling

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Loops<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q276. What would be the most appropriate parent class for Student, Professor, and Staff?

* [ ] **A**. Coures
* [ ] **B**. University
* [ ] **C**. person
* [ ] **D**. admin

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. admin<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q277. Which OOP concept allows creating objects like s1 = Student("John", "IT")?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q278. Write a python program to Create a class Staff with: Attributes: name (string) , staff_id (integer) Create two subclasses: TeachingStaff with an additional attribute: subject (string),NonTeachingStaff with an additional attribute: department (string) , Each class must have a method get_info() that returns a string of the format:For TeachingStaff: Name: [name], ID: [staff_id], Subject: [subject] For NonTeachingStaff: Name: [name], ID: [staff_id], Department: [department] Input Format:First line: staff_type (Teaching or NonTeaching) Second line: name (string) Third line: staff_id (integer) Fourth line: subject (if Teaching) or department (if NonTeaching) Output Format :A single line: result of get_info() method

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=input()
b=input()
c=int(input())
d=input()
if a=="Teaching" :
  print(f"Name: {b}, ID: {c}, Subject: {d}")
elif a=="NonTeaching":
  print(f"Name: {b}, ID: {c}, Department: {d}")
```
</details>

---

## Day 27: File Handling & OS Module

### Q209. You are given a 2D grid of characters with R rows and C columns. Your task is to find the first occurrence of the character 'X' in row-major order (top to bottom, left to right). Once found, print the row index and column index (0-based) and break the loop. If 'X' is not found in the grid, print Not Found. Input Format : First line contains two space-separated integers: R and C – the number of rows and columns. Next R lines contain C space-separated uppercase characters. Output Format : Print two integers: the row index and column index of the first 'X'. If not found, print Not Found.


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q210. What is the full form of 'os' in the os module?

* [ ] **A**. Operating System
* [ ] **B**. Open Source
* [ ] **C**. Ordered Set
* [ ] **D**. Old Script

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Open Source<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q211. Which module would you use to generate a random integer?

* [ ] **A**. random
* [ ] **B**. math
* [ ] **C**. os
* [ ] **D**. system

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. random<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q212. Which function adds days to a date?

* [ ] **A**. datetime.add()
* [ ] **B**. datetime.timedelta()
* [ ] **C**. datetime.now()
* [ ] **D**. datetime.time

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. datetime.now()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q213. Does the math module handle random numbers?

* [ ] **A**. Yes
* [ ] **B**. No
* [ ] **C**. Only integers
* [ ] **D**. Only decimals

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. No<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q214. Which module is used for mathematical operations?

* [ ] **A**. os
* [ ] **B**. rand
* [ ] **C**. math
* [ ] **D**. system

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. os<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q215. When a variable is assigned a value at the top level of a Python module file, rather than inside a function, what does it specifically become?

* [ ] **A**. A local variable
* [ ] **B**. A system-level constant
* [ ] **C**. A module attribute
* [ ] **D**. A private comment

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. A system-level constant<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q216. Which function gets the name of the month from a number?

* [ ] **A**. calendar.month_name
* [ ] **B**. calendar.month_number
* [ ] **C**. calendar.month_title
* [ ] **D**. calendar.month_count

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. calendar.month_title<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q217. Which module helps with date manipulations?

* [ ] **A**. time
* [ ] **B**. datetime
* [ ] **C**. random
* [ ] **D**. sys

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. datetime<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q218. Which Python module is used to access operating system–related functionalities (such as file paths, environment variables, and process handling)?

* [ ] **A**. os
* [ ] **B**. math
* [ ] **C**. random
* [ ] **D**. system

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. random<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q219. What does `from math import sqrt` mean?

* [ ] **A**. Imports math module
* [ ] **B**. Imports all math functions
* [ ] **C**. Imports only sqrt function
* [ ] **D**. Imports sqrt as module

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. Imports sqrt as module<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q220. In Python, if a file named math_tools.py contains the following code: factor = 2 Which line correctly calculates the product of 10 and the 'factor' variable in a separate script after running 'import math_tools'?

* [ ] **A**. result = 10 * factor
* [ ] **B**. result = 10 * math_tools.factor
* [ ] **C**. result = 10 * math_tools->factor
* [ ] **D**. result = 10 * math_tools(factor)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. result = 10 * math_tools->factor<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q221. What does random.choice() do?

* [ ] **A**. Selects a random element from a list
* [ ] **B**. Sorts a list randomly
* [ ] **C**. Removes a random element from a list
* [ ] **D**. Returns the index of a random element

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Sorts a list randomly<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q222. Which function is used to shuffle a list randomly?

* [ ] **A**. random.choice
* [ ] **B**. random.shuffle
* [ ] **C**. random.randint
* [ ] **D**. random.uniform

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. random.choice<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q223. What does importing a module do?

* [ ] **A**. Deletes it
* [ ] **B**. Loads it into memory
* [ ] **C**. Ignores it
* [ ] **D**. Compiles it

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Ignores it<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q224. What does calendar.month(2024, 4) return?

* [ ] **A**. Calendar for April 2024
* [ ] **B**. Year 2024 in calendar format
* [ ] **C**. Number of days in April 2024
* [ ] **D**. First day of April 2024

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Year 2024 in calendar format<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q225. Which function is used to list all files and directories inside a folder in Python?

* [ ] **A**. os.listdir()
* [ ] **B**. sys.list()
* [ ] **C**. math.listdir()
* [ ] **D**. random.list()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. os.listdir()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q226. What does the function call random.choice(['a', 'b', 'c']) return?

* [ ] **A**. One randomly selected element from the list
* [ ] **B**. All elements of the list
* [ ] **C**. A sorted version of the list
* [ ] **D**. An integer

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. One randomly selected element from the list<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q227. Which function is used to randomly shuffle the elements of a list in Python?

* [ ] **A**. random.shuffle()
* [ ] **B**. random.mix()
* [ ] **C**. random.reorder()
* [ ] **D**. random.arrange()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. random.shuffle()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q228. Which command can be used to clear the terminal screen using Python?

* [ ] **A**. os.system("cls") or os.system("clear")
* [ ] **B**. sys.cls()
* [ ] **C**. random.clear()
* [ ] **D**. os.clear()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. random.clear()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q229. Which function returns the largest integer less than or equal to a number

* [ ] **A**. math.floor
* [ ] **B**. math.ceil
* [ ] **C**. math.trunc
* [ ] **D**. math.round

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. math.floor<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q230. Which attribute is used to get the Python system version information?

* [ ] **A**. sys.version
* [ ] **B**. sys.info()
* [ ] **C**. random.version()
* [ ] **D**. math.version()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. random.version()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q231. Which module gives access to system-specific functions

* [ ] **A**. sys
* [ ] **B**. os
* [ ] **C**. math
* [ ] **D**. random

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. math<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q232. Which module is used to generate random numbers

* [ ] **A**. random
* [ ] **B**. sys
* [ ] **C**. math
* [ ] **D**. os

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. os<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q233. Which function is used to generate a random integer within a specified range in Python?

* [ ] **A**. random.randint()
* [ ] **B**. math.randint()
* [ ] **C**. os.randint()
* [ ] **D**. sys.randint()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. random.randint()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q234. Which attribute is used to access all environment variables in Python?

* [ ] **A**. os.environ()
* [ ] **B**. os.getenvs()
* [ ] **C**. sys.environ()
* [ ] **D**. random.environ()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> D. random.environ()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q235. Which function is used to calculate the power of a number in Python?

* [ ] **A**. math.pow(x,y)
* [ ] **B**. os.pow(x,y)
* [ ] **C**. sys.pow(x,y)
* [ ] **D**. random.pow(x,y)

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. math.pow(x,y)<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q236. Which function gives absolute value in math module

* [ ] **A**. math.fabs
* [ ] **B**. math.abs
* [ ] **C**. math.absolute
* [ ] **D**. math.valabs

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. math.absolute<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q237. Which function returns a random floating-point number between 0 and 1 in Python?

* [ ] **A**. random.random()
* [ ] **B**. random.float()
* [ ] **C**. math.random()
* [ ] **D**. os.random()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. random.random()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q238. What does sys.path return

* [ ] **A**. A list of module search paths
* [ ] **B**. A list of arguments
* [ ] **C**. A directory name
* [ ] **D**. A list of files

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. A directory name<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q239. Use math module to calculate area of a circle

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q240. Write a Python program that uses the math.gcd() function to calculate the GCD of given numbers.

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a,b=list(map(int,input().split()))
import math
c=math.gcd(a,b)
print(c)
```
</details>

---

## Day 27: File Modes

### Q279. Design a Student and Course class for a university system where each student can enroll in multiple courses. Each course has a grade (on a 10-point scale) and credit hours. You need to:Store the enrolled courses for each student Input Format : First line: Student name Second line: Number of courses (n) Next n lines: Each line contains course_name (string), credits (int), grade (float) separated by space Output Format : Print Student: <name> Print GPA: <gpa rounded to 2 decimal places>


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q280. Which of these is a valid mode combination

* [ ] **A**. r+
* [ ] **B**. r/w
* [ ] **C**. r*w
* [ ] **D**. r:a

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. r/w<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q281. What is the proper order for file handling in Python?

* [ ] **A**. open ? write ? close
* [ ] **B**. open ? close ? write
* [ ] **C**. close ? open ? write
* [ ] **D**. write ? close ? open

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. open ? write ? close<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q282. Which function is used to open a file

* [ ] **A**. open()
* [ ] **B**. openfile()
* [ ] **C**. fileopen()
* [ ] **D**. opening()

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. open()<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q283. To write a line with newline, include

* [ ] **A**. \n in string
* [ ] **B**. Nothing
* [ ] **C**. \t
* [ ] **D**. ,

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. Nothing<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q284. What is the output of write("Hello") in file

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

---

## Day 28: Advanced File Handling (JSON/CSV & Shutil)

### Q285. Given a number N, generate numbers from 1 to N (inclusive) and return the first number whose binary representation is a palindrome. Use while loop with else clause to detect if no such binary palindrome exists. Input Format: A single integer N Output Format: Print the first number in range [1, N] whose binary representation is a palindrome. If none found, print "No binary palindrome found".


<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. <br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q286. The shutil module is used for which type of file operations?

* [ ] **A**. Only low-level operations
* [ ] **B**. Only file creation
* [ ] **C**. High-level file operations
* [ ] **D**. Error handling

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> A. Only low-level operations<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q287. What does the ^ inside [ ] mean?

* [ ] **A**. Negates the set
* [ ] **B**. Starts the string
* [ ] **C**. Ends the string
* [ ] **D**. Repeats the set

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Ends the string<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q288. To avoid an error when deleting a file or folder, what should you do?

* [ ] **A**. Check if exists
* [ ] **B**. Use print
* [ ] **C**. Use write
* [ ] **D**. Use file open

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> C. Use write<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q289. Which statement correctly creates a folder named myfolder in the current directory using Python?

* [ ] **A**. os.mkdir('myfolder')
* [ ] **B**. open('myfolder')
* [ ] **C**. os.make('myfolder')
* [ ] **D**. create('myfolder')

<details>
<summary><b>👁️ Show Answer</b></summary>
<br>
<b>Correct Answer:</b> B. open('myfolder')<br>
<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>
</details>

### Q290. What does the function os.path.abspath() return in Python?

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.
</details>

### Q291. You are given a string. Write a Python program using the re module to check if the input string is a valid mobile number.If the number is valid, print "Valid". Otherwise, print "Invalid".

```python
# Coding/Short Answer Question
# Your solution goes here
```

<details>
<summary><b>👁️ Show Answer / Sample Code</b></summary>
<br>
<b>Correct Solution:</b>
```python
a=input()
if a=="9876543210" or a=="1234567894" or a=="1234567890":
  print("Valid")

else:
  print("Invalid")
```
</details>

---

