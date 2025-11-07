---
title: "05_Parameters"
weight: 5
chapter: false
---

# Parameters

## ```*args```

- Đây là một hàm đơn giản, nhận vào hai tham số và trả về tổng của chúng:

Input
```python
def foo(x, y):
    return x + y

print(foo(1, 2))
```

Output
```
3
```

- Bây giờ, vấn đề của chúng ta là cần tính tổng của tất cả các số được truyền vào hàm, nhưng không biết trước số lượng của chúng. Đây là lúc là cú pháp *args cực kỳ hữu ích, bởi nó cũng giúp chúng ta có thể truyền một số lượng tham số tuỳ ý vào hàm.

Input
```python
def foo(*args):
    result = 0
    for x in args:
        result += x
    return result

print(foo(1, 2))
print(foo(1, 2, 3))
```

Output
```
3 
6
```

- Về lý thuyết, chúng ta có thể đặt *args ở bất cứ đâu chúng ta muốn trong định nghĩa hàm. Tuy nhiên, nếu đặt ở giữa, chúng ta sẽ không thể gọi hàm được bởi mọi lời gọi sẽ đều gặp lỗi. Nguyên nhân là do *args sẽ nhận toàn bộ các tham số "còn lại" sau khi các tham số đầu tiên đã có giá trị, do đó, các tham số phía sau *args sẽ không bao giờ được truyền vào nữa.

---

## ```**kwargs```

- Cách sử dụng **kwargs cũng tương tự như như *args, tuy nhiên, nó không dùng cho các tham số thông thường truyền vào lần lượt, mà nó được sử dụng cho các tham số đặt tên (thuật ngữ chính xác là named arguments hoặc keyword arguments).

```python
def foo(a=0, b=1):
    return a + b

print(foo())
print(foo(1, 2))
print(foo(b=3, a=4))
```

Output
```
1
3
7
```

<br>

Input
```python
def foo(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print(foo(a=1, b=2))
```

Output
```
a 1
b 2
```

- Lưu ý rằng, với cách sử dụng **kwargs thì kwargs trong hàm sẽ nhận giá trị là một dict với key là các tham số được truyền kèm giá trị tương ứng của chúng.

---

## Notice for ```*args``` and ```**kwargs``

- Thứ tự khi khai báo các tham số này rất quan trọng và không thể thay đổi được. Thứ tự đúng sẽ là:
1. Các tham số bình thường
2. *args
3. **kwargs

---

## Upack with ```*``` and ```**```

### When calling function

- Cú pháp * và ** khi gọi hàm sẽ yêu cầu unpack giá trị được truyền vào trước khi thực hiện hàm đó. Và khi unpack, hàm sẽ nhận các tham số đơn lẻ như các tham số riêng biệt vậy.

- Chúng ta có thể sử dụng unpack để truyền tham số vào cho hàm. Nói một cách đơn giản thì cú pháp * được xử dụng với một đối tượng iterable, còn ** chỉ có thể dùng được với dict mà thôi.

Input
```python
def foo(**kargs):
    for data in kargs.items():
        print(data, end='')
    print()

x = (1, 2, 3)
y = {'a': 7, 'b': 8, 'c': 9}
print(x)
print(*x)
foo(**y)
```

Output
```
(1, 2, 3)
1 2 3
('a', 7)('b', 8)('c', 9)
```

---

### When define variables

- Một nhu cầu khá thường xuyên của lập trình viên đó là chia giá trị một list (hoặc tuple) vào các biến riêng biệt.

Input
```python
x = [1, 2, 3, 4, 5, 6]
a, *b, c = x
print(a)
print(b)
print(c)
```

Output
```
1
[2, 3, 4, 5]
6
```

- Một vấn đề nho nhỏ là cú pháp ** không áp dụng được khi gán biến để unpack một dict được.

---

### Other cases

- Một điều thú vị là unpack có thể áp dụng với mọi đối tượng iterable, nó sẽ rất cần thiết nếu chúng ta cần làm "phẳng" 2 hay nhiều list.

```python
list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
print([*list1, *list2, *list3])
```

Output
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<br>

Input
```python
dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}
print({**dict1, **dict2})
```

Output
```
{'A': 1, 'B': 2, 'C': 3, 'D': 4}
```

---