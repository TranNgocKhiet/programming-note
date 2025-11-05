---
title: "07_Files"
weight: 7
chapter: false
---

## Read and write
```python
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a test file\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'a') as file:
    file.write('\nAppending a new line.')

with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```
Result:
```
Hello, world!
This is a test file

Hello, world!
This is a test file

Appending a new line.
```

## Read line

```python
with open('example.txt', 'w') as file:
    file.write('Line 1\nLine 2\nLine 3')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print('\n', line1, line2)
```
Result:
```
Line 1
Line 2
Line 3

 Line 1
 Line 2

```

## Write lines

```python
with open('example.txt', 'w') as file:
    file.write('Single line using write()\n')

lines = ['line 1\n', 'line 2\n', 'line 3\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)

with open('example.txt', 'r') as file:
    content = file.read()
print("Using writelines():\n", content)
```
Result:
```
Using writelines():
 line 1
line 2
line 3

```