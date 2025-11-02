---
title: "Python"
weight: 1
pre: "<b>1.1.</b>"
chapter: false
---

## Round
``` python
round(3.5)
```
Result: ```>>> 4```
``` python
round(2.5)
```
Result: ```>>> 2```

"For **halfway numbers** that **end with .5**, the number is **rounded to the nearest even integer**. This is called **banker’s rounding**." 
<p style="text-align: right;"> - Automate the Boring Stuff with Python by Al Swigart, Chapter 1 - </p>

## Value comparision
``` python
42 == 42
```
Result: ```True```
``` python
42 == 42.0
```
Result: ```True```
``` python
42 == '42'
```
Result: ```False```

" The expression **42 == '42'** evaluates to **False** because Python considers the integer 42 to be different from the string '42'. However, Python does consider the **integer 42** to be the **same** as the **float 42.0**."
<p style="text-align: right;"> - Automate the Boring Stuff with Python by Al Swigart, Chapter 2 - </p>

## bool() funtion

When used in conditions, **0, 0.0, and '' (the empty string)** are considered **False**, while **all other values** are considered **True**.
<p style="text-align: right;"> - Automate the Boring Stuff with Python by Al Swigart, Chapter 3 - </p>

## None value

In Python, a value called **None** represents the **absence of a value**. The None value is the **only value** of the **NoneType data type**. (Other programming languages might call this value null, nil, or undefined). Just like the Boolean True and False values, you must always write None with a capital N.

This value-without-a-value can be helpful when you need to store something that shouldn’t be confused for a real value in a variable. One place where **None** is used is as the **return value of print()**. The print() function displays text on the screen, and doesn’t need to return anything in the same way len() or input() does. But since all function calls need to evaluate to a return value, print() returns None. To see this in action, enter the following into the interactive shell:

```python
spam = print('Hello!')
```
Result: ```Hello!```
```python
None == spam
```
Result: ```True```

Behind the scenes, Python adds **return None** to the end of any **function definition with no return statement**. This behavior resembles the way in which a while or for loop implicitly ends with a continue statement. Functions also **return None** if you use a **return statement without a value** (that is, just the return keyword by itself).
<p style="text-align: right;"> - Automate the Boring Stuff with Python by Al Swigart, Chapter 4 - </p>

## Named Parameters

On the other hand, Python identifies named parameters by the name placed before them in the function call. You’ll also hear named parameters called keyword parameters or keyword arguments, though they have nothing to do with Python keywords. Programmers often use named parameters to provide optional arguments. For example, the print() function uses the optional parameters end and sep to specify separator characters to print at the end of its arguments and between its arguments, respectively. 

```python
print('Hello')
print('World')
```
Result: 
```
Hello
World
```
```python
print('Hello', end='')
print('World')
```
Result: ```HelloWorld```

```python
print('cats', 'dogs', 'mice')
```
Result: ```cats dogs mice```
```python
print('cats', 'dogs', 'mice', sep=',')
```
Result: ```cats,dogs,mice```