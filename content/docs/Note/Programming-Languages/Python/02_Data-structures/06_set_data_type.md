---
title: "Set Data Type"
weight: 6
---

# Set Data Type

## Syntax

Input
```python
my_set = {1, 2, 3}
print(my_set)
```

Output
```
{1, 2, 3}
```

---

## Add Values | ```add()```

- Data in set cannot be duplicated

Input
```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(2)
print(my_set)
```

Output
```
{1, 2, 3, 4}
```

---

## Remove Values | ```remove()```

- Data in set cannot be duplicated

Input
```python
my_set = {1, 2, 3, 4}
my_set.remove(4)
print(my_set)
try:
  my_set.remove(5)
except KeyError as e:
  print('Error: ', e)
print(my_set)
```

Output
```
{1, 2, 3}
{1, 2, 3}
```

---

## Discard Values | ```discard()```

Input
```python
my_set = {1, 2, 3, 4}
my_set.discard(4)
print(my_set)
my_set.discard(5)
print(my_set)
```

Output
```
{1, 2, 3}
{1, 2, 3}
```

---

## Set Union | ```union()```

Input
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print(union_set)
```

Output
```
{1, 2, 3, 4, 5, 6}
```

---

## Set Intersection | ```intersection()```

Input
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)
```

Output
```
{3}
```

---