---
title: "List Data Type"
weight: 1
---

## Syntax

Input
```python
squares = [x**2 for x in range(10)]
print(squares)
```

Output
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

<br>

Input
```python
products = [i * j for j in range(3) for i in range(3)]
print(products)
```

Output
```
[0, 0, 0, 0, 1, 2, 0, 2, 4]
```

<br>

Input
```python
words = ['apple', 'banana', 'orange']
lengths = [len(word) for word in words]
print(lengths)
```

Output
```
[5, 6, 6]
```

---

## Finding Index | ```index()```

Input
```Python
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
```

Output
```
0
```

<br>

Input
```Python
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka')) # When the list contains duplicates of the value, the method returns the index of its first appearance
```

Output
```
1
```

---

## Adding Values | ```append()```

Input
```Python
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
```

Output
```
['cat', 'dog', 'bat', 'moose']
```

<br>

Input
```Python
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)
```

Output
```
['cat', 'chicken', 'dog', 'bat']
```

---

## Removing Values | ```remove()```

Input
```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
```

Output
```
['cat', 'rat', 'elephant']
```

- If the value appears multiple times in the list, the method will remove only the first instance of it

Input
```python
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)
```

Output
```
['bat', 'rat', 'cat', 'hat', 'cat']
```

---

## Pop Values | ```pop()```

Input
```python
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop()
print(popped_element)
print(my_list)
```

Output
```
5
[1, 2, 3, 4]
```
---

## Sorting Values | ```sort()```

Input
```python
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
print(spam)
```

Output
```
[-7, 1, 2, 3.14, 5]
['Ants', 'Badgers', 'Cats', 'Dogs', 'Elephants']
```

<br>

Input
```python
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort(reverse=True)
print(spam)
```

Output
```
['Elephants', 'Dogs', 'Cats', 'Badgers', 'Ants']
```

- sort() uses ASCIIbetical order rather than actual alphabetical order for sorting strings, this means uppercase letters come before lowercase letters, placing the lowercase a after the uppercase Z

Input
```python
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)
```

Output
```
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```

- Can’t sort lists that have both number values and string values in them, as Python doesn’t know how to compare these values

Input
```python
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
print(spam)
```

Output
```
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
```

<br>

Input
```python
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
```

Output
```
['a', 'A', 'z', 'Z']
```

---

## Reversing Values | ```reverse()```

Input
```python
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)
```

Output
```
['moose', 'dog', 'cat']
```

---

## List Item Enumeration | ```enumerate()```

Input
```python
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
```

Output
```
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
```

---

## Negative Indexes

Input
```python
spam = ['cat', 'bat', 'rat', 'elephant']
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
```

Output
```
The elephant is afraid of the bat.
```

---

## Slices

Input
```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
```

Output
```
['cat', 'bat', 'rat', 'elephant']
['bat', 'rat']
['cat', 'bat', 'rat']
```

<br>

Input
```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
print(spam[:])
```

Output
```
['cat', 'bat']
['bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
```

---

## The Multiple Assignment Trick

Input
```python
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size, color, disposition)
```

Output
```
fat gray loud
```

---