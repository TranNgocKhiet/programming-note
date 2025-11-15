---
title: "Dictionary Data Type"
weight: 2
---

## Syntax

Input
```python
my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print(my_cat['size'])
print('My cat has ' + my_cat['color'] + ' fur.')
```

Output
```
fat
My cat has gray fur
```

<br>

Input
```python
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[12345])
print(spam[42])
print(spam[0])
```

Output
```
Luggage Combination
The Answer
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
KeyError: 0
```

---

## Returning Values | ```values()```

Input
```python
spam = {'color': 'red', 'age': 42}
for v in spam.values():
  print(v)
```

Output
```
red
42
```

---

## Returning Keys | ```keys()```

Input
```python
spam = {'color': 'red', 'age': 42}
for k in spam.keys():
  print(k)
```

Output
```
color
age
```

---

## Returning Keys and Values | ```items()```

Input
```python
spam = {'color': 'red', 'age': 42}
for i in spam.items():
  print(i)
```

Output
```
('color', 'red')
('age', 42)
```

---

## Checking Whether a Key Exists | ```get()```

- Dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key doesn’t exis

Input
```python
picnic_items = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.') 
print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')
```

Output
```
I am bringing 2 cups.
I am bringing 0 eggs.
```

---

## Setting Default Values | ```setdefault()```

- The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key doesn’t exist; if the key does exist, the setdefault() method returns the key’s value

Input
```python
spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))  # Sets 'color' key to 'black'
print(spam.setdefault('color', 'white'))  # Does nothing
```

Output
```
black
black
```

## View object

Input
```python
spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))
```

Output
```
dict_keys(['color', 'age'])
['color', 'age']
```

---

## The Multiple Assignment Trick

Input
```python
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
  print('Key: ' + str(k) + ' Value: ' + str(v))
```

Output
```
Key: color Value: red
Key: age Value: 42
```

---