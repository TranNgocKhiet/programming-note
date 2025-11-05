---
title: "01_Data-structures"
weight: 1
chapter: false
---

## NoneType

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 4 - Functions](https://automatetheboringstuff.com/3e/chapter4.html)"
{style="text-align: right;"}

In Python, a value called **None** represents the **absence of a value**. The None value is the **only value** of the **NoneType data type**. (Other programming languages might call this value null, nil, or undefined). Just like the Boolean True and False values, you must always write None with a capital N.

```python
spam = print('Hello!')
None == spam
```
Result: 
```
True
```

## Sequence Data Types

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 6 - Lists](https://automatetheboringstuff.com/3e/chapter6.html)"
{style="text-align: right;"}

Lists aren’t the only data types that represent ordered sequences of values. For example, strings and lists are actually similar if you consider a string to be a “list” of single text characters. The Python sequence data types include lists, strings, range objects returned by range(), and tuples (explained in “The Tuple Data Type” on page 127). Many of the things you can do with lists can also be done with strings and other values of sequence types.

## Mutable and Immutable Data types

```python
name = 'Zophie a cat'
name[7] = 'the' # A list value is a mutable data type: you can add, remove, or change its values; however, a string is immutable: it cannot be changed
```
Result:
```
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
```

```python
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12] # The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string
print(new_name)
```
Result:
```
Zophie the cat
```

## List

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 6 - Lists](https://automatetheboringstuff.com/3e/chapter6.html)"
{style="text-align: right;"}

```python
squares = [x**2 for x in range(10)]
print(squares)
```
Result:
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
products = [i * j for j in range(3) for i in range(3)]
print(products)
```
Result:
```
[0, 0, 0, 0, 1, 2, 0, 2, 4]
```

```python
words = ['apple', 'banana', 'orange']
lengths = [len(word) for word in words]
print(lengths)
```
Result:
```
[5, 6, 6]
```

### Random Selection and Ordering

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 6 - Lists](https://automatetheboringstuff.com/3e/chapter6.html)"
{style="text-align: right;"}

```Python
import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
```

```Python
import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
```

### Finding Values

```Python
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
```
Result:
```
0
```

```Python
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka')) # When the list contains duplicates of the value, the method returns the index of its first appearance
```
Result:
```
1
```

{style="text-align: right;"}

### Adding Values

```Python
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
```
Result:
```
['cat', 'dog', 'bat', 'moose']
```

```Python
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)
```
Result:
```
['cat', 'chicken', 'dog', 'bat']
```

### Removing Values

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
```
Result:
```
['cat', 'rat', 'elephant']
```

```python
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # If the value appears multiple times in the list, the method will remove only the first instance of it
print(spam)
```
Result:
```
['bat', 'rat', 'cat', 'hat', 'cat']
```

### Sorting Values

```python
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
print(spam)
```
Result:
```
[-7, 1, 2, 3.14, 5]
['Ants', 'Badgers', 'Cats', 'Dogs', 'Elephants']
```

```python
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort(reverse=True)
print(spam)
```
Result:
```
['Elephants', 'Dogs', 'Cats', 'Badgers', 'Ants']
```

```python
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort() # sort() uses ASCIIbetical order rather than actual alphabetical order for sorting strings, this means uppercase letters come before lowercase letters, placing the lowercase a after the uppercase Z
print(spam)
```
Result:
```
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```

```python
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort() # Can’t sort lists that have both number values and string values in them, as Python doesn’t know how to compare these values
print(spam)
```
Result:
```
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
```
```python
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
```
Result:
```
['a', 'A', 'z', 'Z']
```

### Reversing Values

```python
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)
```
Result:
```
['moose', 'dog', 'cat']
```

### The Multiple Assignment Trick

```python
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size, color, disposition)
```
Result:
```
fat gray loud
```

### List Item Enumeration

```python
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
```
Result:
```
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
```

### Negative Indexes

```python
spam = ['cat', 'bat', 'rat', 'elephant']
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
```
Result:
```
The elephant is afraid of the bat.
```

### Slices

```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
```
Result:
```
['cat', 'bat', 'rat', 'elephant']
['bat', 'rat']
['cat', 'bat', 'rat']
```

```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
print(spam[:])
```
Result:
```
['cat', 'bat']
['bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
```

## Tuples

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

### The Tuple Data Type

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 6 - Lists](https://automatetheboringstuff.com/3e/chapter6.html)"
{style="text-align: right;"}

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

```python
eggs = ('hello', 42, 0.5)
eggs[1] = 99 # Tuples, like strings, are immutable: you can’t modify, append, or remove their values
```
Result:
```Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment
```

## List and Tuple Type Conversion

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 6 - Lists](https://automatetheboringstuff.com/3e/chapter6.html)"
{style="text-align: right;"}

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

## The Dictionary Data Type

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 7 - Dictionaries and Structuring Data](https://automatetheboringstuff.com/3e/chapter7.html)"
{style="text-align: right;"}

```python
my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print(my_cat['size'])
print('My cat has ' + my_cat['color'] + ' fur.')
```
Result:
```
fat
My cat has gray fur
```

```python
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[12345])
print(spam[42])
print(spam[0])
```
Result:
```
Luggage Combination
The Answer
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
KeyError: 0
```

### Returning Keys and Values

```python
spam = {'color': 'red', 'age': 42}
for v in spam.values():
  print(v)
```
Result:
```
red
42
```

```python
for k in spam.keys():
  print(k)
```
Result:
```
color
age
```

```python
for i in spam.items():
  print(i)
```
Result:
```
('color', 'red')
('age', 42)
```

```python
print('color' in spam.keys())
print('age' not in spam.keys())
print('red' in spam.values())
```
Result:
```
True
False
True
```

```python
spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))
```
Result:
```
dict_keys(['color', 'age'])
['color', 'age']
```

### The Multiple Assignment Trick

```python
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
  print('Key: ' + str(k) + ' Value: ' + str(v))
```
Result:
```
Key: color Value: red
Key: age Value: 42
```

### Checking Whether a Key Exists

```python
picnic_items = {'apples': 5, 'cups': 2}
# Dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key doesn’t exis
print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.') 
print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')
```
Result:
```
I am bringing 2 cups.
I am bringing 0 eggs.
```

### Setting Default Values

```python
spam = {'name': 'Pooka', 'age': 5}
# The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key doesn’t exist; if the key does exist, the setdefault() method returns the key’s value
print(spam.setdefault('color', 'black'))  # Sets 'color' key to 'black'
print(spam.setdefault('color', 'white'))  # Does nothing
```
Result:
```
black
black
```

## Comparing Dictionaries and Lists

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 7 - Dictionaries and Structuring Data](https://automatetheboringstuff.com/3e/chapter7.html)"
{style="text-align: right;"}

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


## String 

"[Automate the Boring Stuff with Python by Al Swigart](https://automatetheboringstuff.com/), [Chapter 8 - Strings and Text Editing](https://automatetheboringstuff.com/3e/chapter8.html)"
{style="text-align: right;"}

### Escape Characters

```python
print('Say hi to Bob\'s mother.')
```
Result:
```
Say hi to Bob's mother.
```

### Raw Strings

```python
print(r'The file is in C:\Users\Alice\Desktop')
```
Result:
```
The file is in C:\Users\Alice\Desktop
```
### Multiline Strings

```python
print('''Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob''')
```
Result:
```
Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob
```

### Multiline Comments

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

### Indexes and Slices

Strings use indexes and slices the same way lists do. You can think of the string 'Hello, world!' as a list and each character in the string as an item with a corresponding index and negative index.

### The in and not in Operators

You can use the in and not in operators with strings just as you can with list values.

### F-Strings

```python
name = 'Al'
age = 4000
print(f'My name is {name}. I am {age} years old.')
print(f'In ten years I will be {age + 10}')
```
Result:
```
My name is Al. I am 4000 years old.
In ten years I will be 4010
```

### F-String Alternatives: %s and format()

```python
name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))
print('In ten years I will be %s' % (age + 10))
```
Result:
```
My name is Al. I am 4000 years old.
In ten years I will be 4010
```

```python
name = 'Al'
age = 4000
print('My name is {}. I am {} years old.'.format(name, age))
```
Result:
```
My name is Al. I am 4000 years old.
```

```python
name = 'Al'
age = 4000
print('{1} years ago, {0} was born and named {0}.'.format(name, age)) # You can put the index integer (starting at 0) inside the curly brackets to note which of the arguments to format() should be inserted
```
Result:
```
4000 years ago, Al was born and named Al.
```

### Changing the Case

```python
spam = 'Hello, world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
```
Result:
```
HELLO, WORLD!
hello, world!
```

```python
spam = 'Hello, world!'
print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())
```
Result:
```
False
False
True
True
False
False
```

### Checking String Characteristics

```python
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('    '.isspace())
print('This Is Title Case'.istitle())
```
Result:
```
True
False
True
True
True
True
True
```

### Checking the Start or End of a String

```python
print('Hello, world!'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))
```
Result:
```
True
True
False
False
True
True
```

### Joining and Splitting Strings

```python
print(', '.join(['cats', 'rats', 'bats']))
```
Result:
```
cats, rats, bats
```

```python
print('My name is Simon'.split())
print('My name is Simon'.split('m'))
```
Result:
```
['My', 'name', 'is', 'Simon']
['My na', 'e is Si', 'on']
```

### Justifying and Centering Text

```python
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello, World'.rjust(20))
print('Hello'.ljust(10)) 
```
Result:
```
     Hello
               Hello
        Hello, World
Hello     
```

```python
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
```
Result:
```
***************Hello
Hello---------------    
```

```python
print('Hello'.center(20))
print('Hello'.center(20, '='))
```
Result:
```
       Hello        
=======Hello========    
```

### Removing Whitespace

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
Result:
```
Hello, World
Hello, World    
    Hello, World
BaconSpamEggs
BaconSpamEggs
```

### Numeric Code Points of Characters

```python
print(ord('A'))
print(ord('4'))
print(ord('!'))
print(chr(65))
print(ord('A') < ord('B'))
print(chr(ord('A') + 1))
```
Result:
```
65
52
33
A
True
B
```

### Copying and Pasting Strings

1. Ensure you are in the Python 3 mode in the **Mu editor**. The current mode is displayed in the bottom right corner of the window.
2. Click the Admin or cog icon (gear icon) in the bottom right corner of the Mu editor.
3. In the window that appears, select the Third Party Packages tab.
4. Type pyperclip into the text box. You can install multiple packages by placing each on a new line.
5. Click OK. 

```python
import pyperclip
pyperclip.copy('Hello, world!')
print(pyperclip.paste())
```
Result:
```
Hello, world!
```

```python
import pyperclip
print(pyperclip.paste()) # paste whatever you copy from your device, even outside the program
```
```python
For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:
```
Result:
```
For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:
```

## Set

```python
my_set = {1, 2, 3}
print(my_set)
my_set.add(4)
print(my_set)
my_set.add(2)
print(my_set)
my_set.remove(3)
print(my_set)
try:
  my_set.remove(5)
except KeyError as e:
  print('Error: ', e)
my_set.discard(2)
print(my_set)
my_set.discard(5)
print(my_set)
```
Result:
```
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4}
{1, 2, 4}
Error:  5
{1, 4}
{1, 4}
```

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print(union_set)
```
Result:
```
{1, 2, 3, 4, 5, 6}
```

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)
```
Result:
```
{3}
```