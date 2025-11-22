---
title: "Debugging"
menuPre: '10. '
weight: 10
---

## Exception Handling

Input
```py
def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```

Output
```
21.0
3.5
Error: Invalid argument.
None
42.0
```

<br>

Input
```py
def spam(divide_by):
    return 42 / divide_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
```

Output
```
21.0
3.5
Error: Invalid argument.
```

---

## Raising Exceptions

Input
```py
raise Exception('This is the error message.')
```

Output
```
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

<br>

Input
```py
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    box_print('*', 4, 4)
    box_print('O', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))
```

Output 
```
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
An exception happened: Width must be greater than 2.
An exception happened: Symbol must be a single character string.
```

---

## Assertions

Input
```py
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age
```

Output
``` 
```

<br>

Input
```py
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age
```

Output
```
Traceback (most recent call last):
  File "<py-input-0>", line 1, in <module>
AssertionError
```

---

## The logging Module

Input
```py
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')
```

Output
```
2025-11-02 22:53:01,430 -  DEBUG -  Start of program
2025-11-02 22:53:01,430 -  DEBUG -  Start of factorial(5)
2025-11-02 22:53:01,430 -  DEBUG -  i is 0, total is 0
2025-11-02 22:53:01,430 -  DEBUG -  i is 1, total is 0
2025-11-02 22:53:01,430 -  DEBUG -  i is 2, total is 0
2025-11-02 22:53:01,430 -  DEBUG -  i is 3, total is 0
2025-11-02 22:53:01,430 -  DEBUG -  i is 4, total is 0
2025-11-02 22:53:01,430 -  DEBUG -  i is 5, total is 0
2025-11-02 22:53:01,430 -  DEBUG -  End of factorial(5)
0
2025-11-02 22:53:01,430 -  DEBUG -  End of program
```

---

## Logfiles

Input
```py
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')
```

---

## Logging Levels

| Level    | Logging function   | Description                                                                                                                    |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------|
| DEBUG    | logging.debug()    | The lowest level, used for small details. Usually, you’ll care about these messages only when diagnosing problems.             |
| INFO     | logging.info()     | Used to record information about general events in your program or to confirm that it’s working at various points.             |
| WARNING  | logging.warning()  | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.              |
| ERROR    | logging.error()    | Used to record an error that caused the program to fail to do something.                                                       |
| CRITICAL | logging.critical() | The highest level, used to indicate a fatal error that has caused, or is about to cause, the program to stop running entirely. |

- Passing logging.DEBUG to the basicConfig() function’s level named parameter will show messages from all the logging levels (DEBUG being the lowest level). But after developing your program some more, you may be interested only in errors. In that case, you can set basicConfig()’s level argument to logging.ERROR. This will show only ERROR and CRITICAL messages and will skip the DEBUG, INFO, and WARNING messages.

## Disabled Logging

Input
```py
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
```

Output
```
2025-11-02 22:39:52,251 - CRITICAL -  Critical error! Critical error!
```

<br>

Input
```py
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.critical('Critical error! Critical error!')
logging.disable(logging.ERROR)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
```

Output
```
2025-11-02 22:41:46,767 - CRITICAL -  Critical error! Critical error!
2025-11-02 22:41:46,767 - CRITICAL -  Critical error! Critical error!
```

---

## Finally

Input
```py
try:
    result = 20 / 2
except ZeroDivisionError:
    print("error: division by zero is not allowed.")
else:
    print("Division successful, result is : ", result)
finally:
    print("This block always executes")
```

Output
```
Division successful, result is :  10.0
This block always executes
```

---