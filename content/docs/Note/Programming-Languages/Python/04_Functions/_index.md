---
title: "04_Functions"
weight: 4
chapter: false
---

# Functions

## The round() Function

- For **halfway numbers** that **end with .5**, the number is **rounded to the nearest even integer**. This is called **banker’s rounding**.

Input
```python
round(3.5)
```

Output
```
4
```

<br>

Input
```python
round(2.5)
```

Output
```
2
```

---

## The bool() Function

- When used in conditions, **0, 0.0, and '' (the empty string)** are considered **False**, while **all other values** are considered **True**.

## The print() Function

Input
```python
def greet(name="Guest"):
    print(f'Hello, {name}!')

greet()
greet("Bob")
```

Output
```
Hello, Guest!
Hello, Bob!
```

---

### Named Parameters

Input
```python
print('Hello')
print('World')
```

Output
```
Hello
World
```

<br>

Input
```python
print('Hello', end='')
print('World')
```

Output
```
HelloWorld
```

<br>

Input
```python
print('cats', 'dogs', 'mice')
```

Output
```
cats dogs mice
```

<br>

Input
```python
print('cats', 'dogs', 'mice', sep=',')
```

Output
```
cats,dogs,mice
```

---

### The Multiple Assignment Trick

Input
```python
def get_person_information():
    name = 'Alice'
    age = 30
    city = 'New York'
    return name, age, city

name, age, city = get_person_information()
print(f'Name: {name}, Age: {age}, City: {city}')
```

Output
```
Name: Alice, Age: 30, City: New York
```

---

### Anonymous Function

Input
```python
double = lambda x: x * 2
print(double(5))
```

Output
```
10
```

<br>

Input
```python
data = [(1,5), (3,2), (2,7)]
sorted_data = sorted(data, key = lambda x: x[1]) # Sort by second value in tuples
print(sorted_data)
```

Output
```
[(3, 2), (1, 5), (2, 7)]
```   

<br>

Input
```python
numbers = [1, 2, 3, 4, 5, 6]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)
```

Output
```
[2, 4, 6]
```   

---

## Generator and yield

Input
```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

for value in gen:
    print(value)
```

Output
```
1
2
3
```

---

## Function and class decorators

Input
```python
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Function complete"

print(slow_function())
```

Input
```python
def add_method_decorator(cls):
    def new_method(self):
        return "This is a new method"
    cls.new_method = new_method
    return cls

@add_method_decorator
class MyClass:
    def existing_method(self):
        return "This is an existing method"

obj = MyClass()

print(obj.existing_method())
print(obj.new_method())
```

---

## Context manager

Những hàm có dạng ```__name__``` được gọi là Phương thức Dunder (Dunder Methods) hoặc Phương thức Ma thuật (Magic Methods). "Dunder" là viết tắt của "Double Underscore" (hai dấu gạch dưới).

Đây là một phương thức đặc biệt mà Python sẽ tự động gọi trong một hoàn cảnh cụ thể. Bạn (lập trình viên) không nên gọi trực tiếp các hàm này.

Ví dụ đơn giản:
- Khi bạn viết a + b, Python sẽ bí mật gọi a.__add__(b).
- Khi bạn viết len(my_list), Python sẽ bí mật gọi my_list.__len__().
- Khi bạn viết with ... as f:, Python sẽ bí mật gọi f.__enter__().
- Khi bạn viết obj = MyClass(), Python sẽ bí mật gọi obj.__init__() (sau khi đã gọi __new__).

Input
```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Existing the context")

    def do_something(self):
        print("Doing something")

with MyContextManager() as manager:
    manager.do_something()
```

---