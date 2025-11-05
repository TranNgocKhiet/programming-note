---
title: "01_Data-structures"
weight: 1
chapter: false
---

## NoneType

- In Python, a value called **None** represents the **absence of a value**. The None value is the **only value** of the **NoneType data type**. (Other programming languages might call this value null, nil, or undefined). Just like the Boolean True and False values, you must always write None with a capital N.

```python
spam = print('Hello!')
None == spam
```
Result: 
```
True
```

## Sequence Data Types

- Lists aren’t the only data types that represent ordered sequences of values. For example, strings and lists are actually similar if you consider a string to be a “list” of single text characters. The Python sequence data types include lists, strings, range objects returned by range(), and tuples (explained in “The Tuple Data Type” on page 127). Many of the things you can do with lists can also be done with strings and other values of sequence types.

## Mutable and Immutable Data types

- A list value is a mutable data type: you can add, remove, or change its values; however, a string is immutable: it cannot be changed

```python
name = 'Zophie a cat'
name[7] = 'the'
```
Result:
```
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
```

- The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string
print(new_name)

```python
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]
```
Result:
```
Zophie the cat
```

