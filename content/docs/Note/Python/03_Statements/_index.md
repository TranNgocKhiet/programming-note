---
title: "03_Statements"
weight: 4
chapter: false
---

## The global Statement

If you need to modify a global variable from within a function, use the **global statement**. Including a line such as global eggs at the top of a function tells Python, “In this function, eggs refers to the global variable, so **don’t create a local variable with this name**.

```python
def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
```
Result: 
```
spam
```

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 4 - Functions](https://automatetheboringstuff.com/3e/chapter4.html)"
{style="text-align: right;"}