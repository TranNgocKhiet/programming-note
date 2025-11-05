---
title: "Comparision"
weight: 6
chapter: false
---

## List and Tuple Type Conversion

```python
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))
```
Result:
```
('cat', 'dog', 5)
['cat', 'dog', 5]
['h', 'e', 'l', 'l', 'o']
```

## Comparing Dictionarie and List

```python
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # The order of list items matters
```
Result:
```
False
```

```python
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham) # The order of dictionary key-value pairs doesn't matter
```
Result:
```
True
```

