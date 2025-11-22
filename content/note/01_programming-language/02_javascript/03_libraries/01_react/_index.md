---
title: "React"
menuPre: '<i class="fa-brands fa-react"></i> '
weight: 1
---

## JSX (HTML in JavaScript)

- Quy tắc quan trọng:
<br>&emsp; + Code HTML phải được đặt trong dấu ngoặc đơn ```return ()```.
<br>&emsp; + Thẻ class trong HTML đổi tên thành ```className``` (vì ```class``` là từ khóa của **JS**).
<br>&emsp; + Chỉ được trả về một thẻ cha duy nhất (thường dùng ```<div></div>``` hoặc ```<></>``` để bao ngoài).

```jsx
const MyComponent = () => {
  const name = "Bạn";

  return (
    <div className="card">
      <h1>Xin chào, {name}!</h1>
      <p>Đây là React.</p>
    </div>
  );
};
```

## Components

- Component giống như những miếng Lego. Bạn tạo ra các miếng nhỏ (Nút bấm, Thanh menu, Card ảnh) rồi ghép chúng lại thành một trang web lớn.
- Component thực chất chỉ là một Hàm mũi tên (Arrow Function) trả về JSX.
- Tên Component phải Viết Hoa Chữ Cái Đầu (ví dụ: PhotoCard, không phải photoCard).

```jsx
// 1. Tạo miếng Lego nhỏ (Component con)
const NutBam = () => {
  return <button>Bấm vào tôi</button>;
};

// 2. Ghép vào trang chính (Component cha)
const TrangChu = () => {
  return (
    <div>
      <h1>Trang chủ</h1>
      <NutBam /> {/* Dùng như thẻ HTML tự tạo */}
      <NutBam />
    </div>
  );
};
```

## Props

```jsx
// Component con nhận props (title, url)
// { title, url } là destructuring
const PhotoCard = ({ title, url }) => {
  return (
    <div className="card">
      <img src={url} alt={title} />
      <p>{title}</p>
    </div>
  );
};

// Component cha truyền dữ liệu vào
const Gallery = () => {
  return (
    <div>
      <PhotoCard title="Hoàng hôn" url="/sunset.jpg" />
      <PhotoCard title="Bình minh" url="/sunrise.jpg" />
    </div>
  );
};
```

## State | ```useState()```

- Đây là "trái tim" của React. Trong **JS** thường, khi biến thay đổi (x = x + 1), giao diện web không tự cập nhật. Trong **React**, khi State thay đổi, giao diện web tự động vẽ lại (re-render) để hiển thị giá trị mới.

```jsx
import { useState } from 'react'; // Phải import

const LikeButton = () => {
  // Khai báo state: 
  // 'liked' là giá trị hiện tại (true/false)
  // 'setLiked' là hàm để thay đổi giá trị
  const [liked, setLiked] = useState(false); 

  // Hàm xử lý khi click
  const handleClick = () => {
    setLiked(!liked); // Đảo ngược giá trị: true -> false, false -> true
    // Khi setLiked chạy, React sẽ vẽ lại đoạn code bên dưới ngay lập tức
  };

  return (
    <button onClick={handleClick}>
      {/* Dùng toán tử 3 ngôi (giống if/else) để hiển thị chữ */}
      {liked ? "Đã thích ❤️" : "Thích 🤍"}
    </button>
  );
};
```

## Outside Connection | ```useEffect()```

- Bạn dùng ```useEffect``` khi muốn làm việc gì đó ngay khi Component vừa hiện lên (ví dụ: gọi API lấy danh sách ảnh)

```jsx
import { useState, useEffect } from 'react';

const PhotoList = () => {
  const [photos, setPhotos] = useState([]); // State lưu danh sách ảnh

  useEffect(() => {
    // Hàm này chạy 1 lần duy nhất khi trang vừa load
    const fetchPhotos = async () => {
      const res = await fetch('https://api.example.com/photos');
      const data = await res.json();
      setPhotos(data); // Lưu dữ liệu vào state -> Màn hình tự vẽ lại danh sách
    };

    fetchPhotos();
  }, []); // Dấu [] rỗng nghĩa là "chỉ chạy 1 lần đầu tiên"

  return (
    <div>
      {/* Dùng .map() để lặp qua mảng photos và vẽ ra giao diện */}
      {photos.map(photo => (
        <div key={photo.id}>{photo.title}</div>
      ))}
    </div>
  );
};
```