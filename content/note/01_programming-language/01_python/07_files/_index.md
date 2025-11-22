---
title: "Files"
menuPre: '07. '
weight: 7
---

## Read and write

Input
```py
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

Output
```
Hello, world!
This is a test file

Hello, world!
This is a test file

Appending a new line.
```

---

## Read line

Input
```py
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

Output
```
Line 1
Line 2
Line 3

 Line 1
 Line 2

```

---

## Write lines

Input
```py
with open('example.txt', 'w') as file:
    file.write('Single line using write()\n')

lines = ['line 1\n', 'line 2\n', 'line 3\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)

with open('example.txt', 'r') as file:
    content = file.read()
print("Using writelines():\n", content)
```

Output
```
Using writelines():
 line 1
line 2
line 3

```

---