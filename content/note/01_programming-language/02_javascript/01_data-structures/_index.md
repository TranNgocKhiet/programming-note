---
title: "Data Structures"
menuPre: '01. '
weight: 1
---

## ```let```

```js
let count = 0;
count = 1; // OK
```

## ```const```

```js
const name = "Alice";
name = "Bob"; // Error
```

## Object | ```{}```

Input
```js
const photo = {
  id: "123",
  title: "Ảnh hoàng hôn",
  tags: ["sunset", "beach"]
};

console.log(photo.title);
console.log(photo.tags[0]); 
```

Output
```
"Ảnh hoàng hôn"
"sunset"
```

## Array | ```[]```

Input
```js
const photoList = [
  { id: "123", title: "Ảnh hoàng hôn" },
  { id: "456", title: "Ảnh bình minh" }
];

console.log(photoList[0].title);
```

Output
```
"Ảnh hoàng hôn"
```