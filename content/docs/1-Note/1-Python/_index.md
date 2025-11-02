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

"For halfway numbers that end with .5, the number is rounded to the nearest even integer. This is called **banker’s rounding**." 
<p style="text-align: right;"> - Automate the Boring Stuff with Python by Al Swigart, chapter 1 - </p>

## Boolean Values
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

" The expression 42 == '42' evaluates to False because Python considers the integer 42 to be different from the string '42'. However, Python does consider the integer 42 to be the same as the float 42.0."
<p style="text-align: right;"> - Automate the Boring Stuff with Python by Al Swigart, chapter 2 - </p>