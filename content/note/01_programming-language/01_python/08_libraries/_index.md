---
title: "Libraries"
menuPre: '08. '
weight: 8
---

## Install libraries on Mu editor

1. Ensure you are in the Python 3 mode in the **Mu editor**. The current mode is displayed in the bottom right corner of the window.
2. Click the Admin or cog icon (gear icon) in the bottom right corner of the Mu editor.
3. In the window that appears, select the Third Party Packages tab.
4. Type name of the libraries into the text box. You can install multiple packages by placing each on a new line.
5. Click OK. 

## math

Input
```py
import math
result = math.sqrt(16)
print(result)
```

Output
```
4.0
```

<br>

Input
```py
from math import pi, cos
result = cos(pi)
print(result)
```

Output
```
-1.0
```

---

## numpy

Input
```py
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([[1, 2, 3], [4, 5, 6]])
array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])
addition = array3 + array4
multiplication = array3 * array4
print(array1)
print(array2)
print(addition)
print(multiplication)
```

Output
```
[1 2 3 4 5]
[[1 2 3]
 [4 5 6]]
[5 7 9]
[ 4 10 18]
```

---

## datetime

Input
```py
import datetime
now = datetime.datetime.today()
print(now)
```

Output
```
2025-11-04 20:03:37.981197
```

---

## random

Input
```py
import random
rand_int = random.randint(1, 10)
rand_float = random.random()
print(rand_int)
print(rand_float)
```

Output
```
6
0.8069049490320905
```

---

## os

Input
```py
import os
files = os.listdir('.')
print(files)
```

Output
```
['chapter6_coinFlipStreaks.py', 'chapter6_commaCode.py', 'collatz.py', 'dishonestcapacity.py', 'exitExample.py', 'exm.py', 'hello.py', 'isValidChesSBoard.py', 'matrixscreensaver.py', 'printTable.py', 'rpsGame.py', 'rpsGame_myVersion.py', 'yourName.py', 'zigzag.py']
```

---

## json

Input
```py
import json
data = {'name': 'Alice', 'age': 28, 'city': 'New York'}
json_str = json.dumps(data)
data_back = json.loads(json_str)
print(json_str)
print(data_back)
```

Output
```
{"name": "Alice", "age": 28, "city": "New York"}
{'name': 'Alice', 'age': 28, 'city': 'New York'}
```

---

## pandas

- ```pandas``` là một thư viện Python cực kỳ mạnh mẽ và phổ biến, chuyên dùng để phân tích và xử lý dữ liệu (đặc biệt là dữ liệu dạng bảng)

Input
```py
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Devid'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nAccessing a Column:")
print(df['Name'])

print("\nAccessing a Row:")
print(df.iloc[0])

print("\nApplying a function:")
df['Age'] = df['Age'].apply(lambda x: x + 5)
print(df)
```

Output
```
DataFrame:
      Name  Age        City
0    Alice   25    New York
1      Bob   30  Los Angles
2  Charlie   35     Chicago
3    Devid   40     Houston

Accessing a Column
0      Alice
1        Bob
2    Charlie
3      Devid
Name: Name, dtype: object

Accessing a Row:
Name       Alice
Age           25
City    New York
Name: 0, dtype: object

Applying a function:
      Name  Age        City
0    Alice   30    New York
1      Bob   35  Los Angles
2  Charlie   40     Chicago
3    Devid   45     Houston
```

## matplotlib

Input
```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('line plot')

plt.show()
```

<br>

Input
```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y, color='red', marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter plot')

plt.show()
```

---

## pyperclip

Input
```py
import pyperclip
pyperclip.copy('Hello, world!')
print(pyperclip.paste())
```
Result:
```
Hello, world!
```

<br>

Input
```py
import pyperclip
print(pyperclip.paste())
```
```py
For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:
```

Output
```
For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:
```

---

## random

Input
```Python
import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
```

<br>

Input
```Python
import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
```

---

## copy

- If the list you need to copy contains lists, use the copy.deepcopy() function instead of copy.copy(). The copy.deepcopy() function will copy these inner lists as well.

Input
```py
import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)  # Creates a duplicate copy of the list
cheese[1] = 42  # Changes cheese
print(spam ) # The spam variable is unchanged
print(cheese) # The cheese variable is changed
```

Output
```
['A', 'B', 'C']
['A', 42, 'C']
```

---