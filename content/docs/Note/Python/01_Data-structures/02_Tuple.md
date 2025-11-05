---
title: "Tuple"
weight: 2
chapter: false
---

## Syntax
  
```python
a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)
```
Result:
```
10
20
30
```

## Multiple data type values

```python
mixed_tuple = (1, 'hello' , 3.14)
print(mixed_tuple)
print(type(mixed_tuple[0]))
print(type(mixed_tuple[1]))
print(type(mixed_tuple[2]))
```
Result:
```
(1, 'hello', 3.14)
<class 'int'>
<class 'str'>
<class 'float'>
```

```python
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
```
Result:
```
hello
(42, 0.5)
3
```

## Immutable

```python
eggs = ('hello', 42, 0.5)
eggs[1] = 99 
```
Result:
```Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment
```