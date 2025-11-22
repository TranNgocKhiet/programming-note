---
title: "Functions"
menuPre: '02. '
weight: 2
---

## Arrow Functions

- Old style

```js
function add(a, b) {
  return a + b;
}
```

- New style

```js
const add = (a, b) => {
  return a + b;
};
```

- Nếu hàm chỉ có 1 dòng return, bạn có thể viết siêu ngắn

```js
const addShort = (a, b) => a + b;
```

- Nếu chỉ có 1 tham số

```js
const sayHello = name => `Hello, ${name}`;
```

## ```map()```

Input
```js
const photoList = [
  { id: "123", title: "Ảnh hoàng hôn" },
  { id: "456", title: "Ảnh bình minh" }
];

const photoTitles = photoList.map(photo => {
  return photo.title;
});

// Dùng cú pháp ngắn gọn hơn:
const photoTitles2 = photoList.map(photo => photo.title);

console.log(photoTitles);
console.log(photoTitles2);
```

Output
```
["Ảnh hoàng hôn", "Ảnh bình minh"]
["Ảnh hoàng hôn", "Ảnh bình minh"]
```

## ```filter()```

Input
```js
const photoList = [
  { id: "123", tags: ["sunset", "beach"] },
  { id: "456", tags: ["morning", "coffee"] },
  { id: "789", tags: ["travel", "sunset"] }
];

const sunsetPhotos = photoList.filter(photo => {
  return photo.tags.includes("sunset"); // .includes() là hàm check mảng
});

// Dùng cú pháp ngắn gọn hơn:
const sunsetPhotos2 = photoList.filter(photo => photo.tags.includes("sunset"));

console.log(sunsetPhotos); // Trả về 2 object có id "123" và "789"
console.log(sunsetPhotos2);
```

Output
```
[{
  id: "123",
  tags: ["sunset", "beach"]
}, {
  id: "789",
  tags: ["travel", "sunset"]
}]
[{
  id: "123",
  tags: ["sunset", "beach"]
}, {
  id: "789",
  tags: ["travel", "sunset"]
}]
```

## Asynchronous | ```Promise```, ```async``` and ```await``` 

### Problem

- JavaScript không "đợi"

Input
```js
const fakeApiCall = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({ id: "123", title: "Ảnh hoàng hôn" });
    }, 2000);
  });
};

console.log("1. Bắt đầu lấy dữ liệu...");
const data = fakeApiCall()// gọi API (việc này mất 2 giây)
console.log(data.title); // In ra "undefined" ngay lập tức
console.log("3. Đã lấy xong");
```

Ouput
```js
"1. Bắt đầu lấy dữ liệu..."
undefined
"3. Đã lấy xong"
```

- Code trên sẽ in ra "1", "undefined", "3" vì nó không đợi API trả về kết quả.

### Solution

- ```Promise```: Tưởng tượng nó là một "lời hứa" (giống như giấy hẹn) rằng "tôi sẽ trả về giá trị cho bạn trong tương lai".
- ```async```/```await```: Là cú pháp hiện đại để làm việc với Promise.
<br>&emsp; + ```async```: Đặt trước một hàm để báo cho JS biết hàm này sẽ làm việc bất đồng bộ.
<br>&emsp; + ```await```: Đặt trước một ```Promise``` (như gọi API) để "tạm dừng" hàm và chờ cho đến khi có kết quả.

Input
```js
const fakeApiCall = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({ id: "123", title: "Ảnh hoàng hôn" });
    }, 2000);
  });
};

// Bắt buộc khai báo "async" nếu muốn dùng "await"
const fetchData = async () => {
  console.log("1. Bắt đầu lấy dữ liệu...");

  // Dùng await để "chờ" lời hứa được thực hiện
  const data = await fakeApiCall(); 

  // Code ở đây chỉ chạy SAU KHI await hoàn thành (sau 2 giây)
  console.log("2. Dữ liệu đã về:", data);
  console.log("3. Đã lấy xong");
};

fetchData();
```

Output
```js
"1. Bắt đầu lấy dữ liệu..."
"2. Dữ liệu đã về:", {
  id: "123",
  title: "Ảnh hoàng hôn"
}
"3. Đã lấy xong"
```

## Modules | ```import``` and ```export```

- Bạn có 2 file: ```utils.js``` (công cụ) và ```main.js``` (chính).

- ```utils.js``` (Dùng ```export``` để "xuất" hàm ra ngoài):

Input
```js
export const add = (a, b) => a + b;

export const subtract = (a, b) => a - b;
```

- ```main.js``` (Dùng ```import``` để "nhập" hàm về dùng):
  
Input
```js
import { add, subtract } from "./utils.js";

console.log(add(5, 3));
console.log(subtract(10, 4));
```

Output
```
8
6
```

## Destructuring

Input
```js
const photo = {
  id: "123",
  title: "Ảnh hoàng hôn",
  tags: ["sunset", "beach"]
};

// Cách viết cũ:
// const title = photo.title;
// const tags = photo.tags;

// Cách viết mới (Destructuring):
const { title, tags } = photo;

console.log(title);
console.log(tags);
```

Output
```
"Ảnh hoàng hôn"
["sunset", "beach"]
``