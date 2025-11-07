---
title: "01_Data-structures"
weight: 1
chapter: false
---

# Data Structures

## NoneType

- In Python, a value called **None** represents the **absence of a value**. The None value is the **only value** of the **NoneType data type**. (Other programming languages might call this value null, nil, or undefined). Just like the Boolean True and False values, you must always write None with a capital N.

Input
```python
spam = print('Hello!')
None == spam
```

Ouput
```
True
```

---

## Sequence Data Types

- The Python sequence data types include **lists**, **strings**, **range objects returned by range()**, and **tuples**. 

---

## Mutable and Immutable Data types

- A list value is a mutable data type: you can add, remove, or change its values; however, a string is immutable: it cannot be changed

Input
```python
name = 'Zophie a cat'
name[7] = 'the'
```

Output
```
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
```

- The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string
print(new_name)

Input
```python
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]
```

Output
```
Zophie the cat
```

---