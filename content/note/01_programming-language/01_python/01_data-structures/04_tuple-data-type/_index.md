weight: 4
---

## Syntax
  
Input
```py
a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)
```

Output
```
10
20
30
```

---

## Multiple data type values

Input
```py
mixed_tuple = (1, 'hello' , 3.14)
print(mixed_tuple)
print(type(mixed_tuple[0]))
print(type(mixed_tuple[1]))
print(type(mixed_tuple[2]))
```

Output
```
(1, 'hello', 3.14)
<class 'int'>
<class 'str'>
<class 'float'>
```

<br>

Input
```py
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
```
Output
```
hello
(42, 0.5)
3
```

---

## Immutable

Input
```py
eggs = ('hello', 42, 0.5)
eggs[1] = 99 
```

Output
```Traceback (most recent call last):
  File "<py-input-0>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment
```

---