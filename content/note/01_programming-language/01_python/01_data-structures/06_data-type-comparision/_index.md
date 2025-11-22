---
title: "Data Type Comparision"
weight: 6
---

## List and Tuple Type Conversion

Input
```py
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))
```

Output
```
('cat', 'dog', 5)
['cat', 'dog', 5]
['h', 'e', 'l', 'l', 'o']
```

---

## Comparing Dictionarie and List

Input
```py
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # The order of list items matters
```

Ouput
```
False
```

<br>

Input
```py
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': ' t', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  The order of dictionary key-value pairs doesn't matter
```

Output
```
True
```

---

