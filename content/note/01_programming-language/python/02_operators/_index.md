---
title: "Operators"
menuPre: '02. '
weight: 2
---

## Comparison Operator

Input
```python
42 == 42
```

Output
```
True
```

<br>

Input
```python
42 == 42.0
```

Output
```
True
```

- The expression **42 == '42'** evaluates to **False** because Python considers the integer 42 to be different from the string '42'. However, Python does consider the **integer 42** to be the **same** as the **float 42.0**.

Input
```python
42 == '42'
```

Output
```
False
```

---

## The ```in``` and ```not in``` Operators

Input
```python
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)
```

Output
```
True
False
False
True
```

---