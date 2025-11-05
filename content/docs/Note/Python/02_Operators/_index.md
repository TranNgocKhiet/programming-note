---
title: "02_Operators"
weight: 3
chapter: false
---

## Comparison Operator

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 2 - if-else and Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)"
{style="text-align: right;"}

```python
42 == 42
```
Result: 
```
True
```

```python
42 == 42.0
```
Result: 
```
True
```

```python
42 == '42'
```
Result: 
```
False
```

The expression **42 == '42'** evaluates to **False** because Python considers the integer 42 to be different from the string '42'. However, Python does consider the **integer 42** to be the **same** as the **float 42.0**.

## The in and not in Operators

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 6 - Lists](https://automatetheboringstuff.com/3e/chapter6.html)"
{style="text-align: right;"}


```python
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)
```
Result:
```
True
False
False
True
```