---
title: "04_Functions"
weight: 4
chapter: false
---

## The round() Function

- For **halfway numbers** that **end with .5**, the number is **rounded to the nearest even integer**. This is called **banker’s rounding**.

```python
round(3.5)
```
Result 
```
4
```

```python
round(2.5)
```
Result: 
```
2
```

## The bool() Function

- When used in conditions, **0, 0.0, and '' (the empty string)** are considered **False**, while **all other values** are considered **True**.

## The print() Function

```python
def greet(name="Guest"):
    print(f'Hello, {name}!')

greet()
greet("Bob")
```
Result:
```
Hello, Guest!
Hello, Bob!
```

### Named Parameters

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
Result: 
```
HelloWorld
```

```python
print('cats', 'dogs', 'mice')
```
Result: 
```
cats dogs mice
```

```python
print('cats', 'dogs', 'mice', sep=',')
```
Result: 
```
cats,dogs,mice
```

### The Multiple Assignment Trick

```python
def get_person_information():
    name = 'Alice'
    age = 30
    city = 'New York'
    return name, age, city

name, age, city = get_person_information()
print(f'Name: {name}, Age: {age}, City: {city}')
```
Result:
```
Name: Alice, Age: 30, City: New York
```

### Anonymous Function

```python
double = lambda x: x * 2
print(double(5))
```
Result:
```
10
```

```python
data = [(1,5), (3,2), (2,7)]
sorted_data = sorted(data, key = lambda x: x[1]) # Sort by second value in tuples
print(sorted_data)
```
Result:
```
[(3, 2), (1, 5), (2, 7)]
```   

```python
numbers = [1, 2, 3, 4, 5, 6]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)
```
Result: 
```
[2, 4, 6]
```   

## Generator and yield

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

for value in gen:
    print(value)
```
Result:
```
1
2
3
```

## Function and class decorators

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

## Context manager

Những hàm có dạng ```__name__``` được gọi là Phương thức Dunder (Dunder Methods) hoặc Phương thức Ma thuật (Magic Methods). "Dunder" là viết tắt của "Double Underscore" (hai dấu gạch dưới).

Đây là một phương thức đặc biệt mà Python sẽ tự động gọi trong một hoàn cảnh cụ thể. Bạn (lập trình viên) không nên gọi trực tiếp các hàm này.

Ví dụ đơn giản:
- Khi bạn viết a + b, Python sẽ bí mật gọi a.__add__(b).
- Khi bạn viết len(my_list), Python sẽ bí mật gọi my_list.__len__().
- Khi bạn viết with ... as f:, Python sẽ bí mật gọi f.__enter__().
- Khi bạn viết obj = MyClass(), Python sẽ bí mật gọi obj.__init__() (sau khi đã gọi __new__).

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