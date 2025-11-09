---
title: "String Data Type"
weight: 4
---

# String Data Type

- String is like a list of characters, so is inherits list attributes

## Escape Characters | ```\```

Input
```python
print('Say hi to Bob\'s mother.')
```

Output
```
Say hi to Bob's mother.
```

---

## Raw Strings | ```r```

Input
```python
print(r'The file is in C:\Users\Alice\Desktop')
```

Output
```
The file is in C:\Users\Alice\Desktop
```

---

## Multiline Strings | ```''' '''```

Input
```python
print('''Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob''')
```

Output
```
Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob
```

---

## Multiline Comments | ```"""" """"```

Input
```python
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def say_hello():
    """This function prints hello.
    It does not return anything."""
    print('Hello!')
```

---

## F-Strings | ```f```

Input
```python
name = 'Al'
age = 4000
print(f'My name is {name}. I am {age} years old.')
print(f'In ten years I will be {age + 10}')
```

Output
```
My name is Al. I am 4000 years old.
In ten years I will be 4010
```

---

## F-String Alternatives | ```%s``` and ```format()```

Input
```python
name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))
print('In ten years I will be %s' % (age + 10))
```

Output
```
My name is Al. I am 4000 years old.
In ten years I will be 4010
```

<br>

Input
```python
name = 'Al'
age = 4000
print('My name is {}. I am {} years old.'.format(name, age))
```

Output
```
My name is Al. I am 4000 years old.
```

- You can put the index integer (starting at 0) inside the curly brackets to note which of the arguments to format() should be inserted

Input
```python
name = 'Al'
age = 4000
print('{1} years ago, {0} was born and named {0}.'.format(name, age))
```

Output
```
4000 years ago, Al was born and named Al.
```

---

## Changing the Case | ```upper()``` and ```lower()```

Input
```python
spam = 'Hello, world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
```

Output
```
HELLO, WORLD!
hello, world!
```

---

## Checking the Case | ```isupper()``` and ```islower()``

Input
```python
spam = 'Hello, world!'
print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())
```

Output
```
False
False
True
True
False
False
```

---

## Checking String Characteristics | ```isalpha()```, ```isalnum()```, ```isdecimal()```, ```isspace()``` and ```istitle()```

Input
```python
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('    '.isspace())
print('This Is Title Case'.istitle())
```

Output
```
True
False
True
True
True
True
True
```

---

## Checking the Start or End of a String | ```startswith()``` and ```endswith()```

Input
```python
print('Hello, world!'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))
```

Output
```
True
True
False
False
True
True
```

---

## Joining Strings | ```join()```

Input
```python
print(', '.join(['cats', 'rats', 'bats']))
```

Output
```
cats, rats, bats
```

---

## Splitting Strings | ```split()``` 

Input
```python
print('My name is Simon'.split())
print('My name is Simon'.split('m'))
```

Output
```
['My', 'name', 'is', 'Simon']
['My na', 'e is Si', 'on']
```

---

## Justifying Text | ```rjust``` and ```ljust```

Input
```python
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello, World'.rjust(20))
print('Hello'.ljust(10)) 
```

Output
```
     Hello
               Hello
        Hello, World
Hello     
```

<br>

Input
```python
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
```

Output
```
***************Hello
Hello---------------    
```

---

## Centering Text | ```center()```

Input
```python
print('Hello'.center(20))
print('Hello'.center(20, '='))
```

Output
```
       Hello        
=======Hello========    
```

---

## Removing Whitespace | ```strip()```, ```lstrip()``` and ```rstrip()```

Input
```python
spam = '    Hello, World    '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
# A string argument will specify which characters on the ends to strip
print(spam.strip('ampS'))
print(spam.strip('Spam'))  
```

Output
```
Hello, World
Hello, World    
    Hello, World
BaconSpamEggs
BaconSpamEggs
```

---

## Numeric Code Points of Characters | ```ord()``` and ```chr()```

Input
```python
print(ord('A'))
print(ord('4'))
print(ord('!'))
print(chr(65))
print(ord('A') < ord('B'))
print(chr(ord('A') + 1))
```

Output
```
65
52
33
A
True
B
```

---