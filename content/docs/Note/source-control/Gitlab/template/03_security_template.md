---
title: "Security Template"
weight: 3
---

# Security Template on Gitlab

## Static Application Security Testing (SAST)

```yml
Jobs/SAST.gitlab-ci.yml
```

- Template này thêm một job quét mã nguồn tĩnh
- Nó hoạt động như một người "soi" code tự động, đọc qua code (Java, Python, C#, Go...) ngay cả khi chúng chưa được build hay chạy
- Nó tìm kiếm các mẫu code "nguy hiểm" có thể dẫn đến lỗ hổng, như nguy cơ SQL Injection hoặc xử lý dữ liệu đầu vào (nguy cơ XSS)

---

## Dynamic Application Security Testing (DAST)

```yml
Jobs/DAST.gitlab-ci.yml
```

- Template này chạy một job "tấn công" ứng dụng web đang chạy
- Nó không đọc code. Thay vào đó, nó hoạt động như một hacker "mũ trắng"
- Sau khi đã build và deploy ứng dụng (ví dụ, deploy vào một "review environment"), job DAST sẽ cố gắng "tấn công" ứng dụng đó từ bên ngoài
- Nó gửi đi các payload độc hại để tìm các lỗ hổng mà chỉ có thể phát hiện được khi ứng dụng đang chạy (ví dụ: "Chuyện gì xảy ra nếu tôi nhập một đoạn script vào ô tìm kiếm?")

---

## Infrastructure as Code (IaC) Scanning

```yml
Jobs/SAST-IaC.gitlab-ci.yml
```

- Quét các tệp cấu hình hạ tầng
- Thay vì quét code ứng dụng, nó quét các tệp định nghĩa hạ tầng như Terraform (.tf), AWS CloudFormation, hay Dockerfile
- Nó tìm các lỗi "cài đặt" bảo mật, ví dụ: "Bạn đã mở cổng 22 (SSH) cho toàn bộ internet" hoặc "Bạn đã tạo một S3 bucket cho phép truy cập công khai"

---

## Container Scanning

```yml
Jobs/Container-Scanning.gitlab-ci.yml
```

- Quét các ảnh (image) container (ví dụ: Docker image)
- Một Docker image được xây dựng từ nhiều "lớp" (layers), bao gồm một hệ điều hành cơ sở (như Ubuntu) và các thư viện khác
- Job này sẽ "mở" image của bạn ra và đối chiếu danh sách tất cả các phần mềm bên trong với một cơ sở dữ liệu về lỗ hổng đã biết (CVEs)
- Nó sẽ cảnh báo bạn nếu, ví dụ, "Image của bạn đang dùng một phiên bản OpenSSL đã lỗi thời và có lỗ hổng nghiêm trọng."

---

## Secret Detection

```yml
Jobs/Secret-Detection.gitlab-ci.yml
```

- Quét code và lịch sử commit để tìm thông tin nhạy cảm (secrets) bị lộ
- Đây là một lỗi rất phổ biến. Lập trình viên đôi khi vô tình "commit" (đẩy) các thông tin nhạy cảm như API key, mật khẩu database, hoặc token truy cập vào Git
- Job này sẽ quét toàn bộ dự án của bạn (bao gồm cả lịch sử) để tìm các chuỗi văn bản trông giống như một "secret" và cảnh báo bạn ngay lập tức

---

## Dependency Scanning + License Scanning

```yml
Jobs/Dependency-Scanning.gitlab-ci.yml
```

<br>

```yml
Jobs/License-Scanning.gitlab-ci.yml
```

- Quét các thư viện bên ngoài (dependencies) mà dự án sử dụng
- Dependency Scanning:
<br>$emsp; + Hầu hết các dự án đều dùng thư viện mã nguồn mở (ví dụ: từ npm, pip, maven). 
<br>$emsp; + Job này kiểm tra các file quản lý thư viện (như package.json, requirements.txt) và báo cho bạn biết nếu bạn đang "dùng một thư viện X phiên bản 1.2, mà phiên bản đó vừa được phát hiện có lỗ hổng bảo mật."

- License Scanning:
<br>$emsp; + Tương tự, job này kiểm tra "giấy phép" (license) của các thư viện đó để đảm bảo chúng tuân thủ chính sách của công ty bạn (ví dụ: "Dự án này cấm sử dụng các thư viện có giấy phép GPL").

---

## Web-API Fuzzing

```yml
Jobs/API-Fuzzing.gitlab-ci.yml
```

- Thử nghiệm mờ" (Fuzz testing) cho các API (Web-API)
- Job này tự động tạo ra hàng ngàn yêu cầu (request) "ngẫu nhiên" hoặc "dị dạng" và gửi chúng tới các điểm cuối (endpoint) API của bạn
- Mục đích là để xem API của bạn có bị "sập" (crash) hoặc rò rỉ thông tin khi nhận được dữ liệu không mong muốn hay không

---

## Coverage-Guided Fuzzing

```yml
Jobs/Coverage-Fuzzing.gitlab-ci.yml
```

- Một loại "thử nghiệm mờ" thông minh hơn, dùng cho các hàm (function) trong code
- Khác với API Fuzzing (hộp đen), loại này là "hộp trắng"
- Nó "biết" code của bạn. Nó gửi dữ liệu ngẫu nhiên vào một hàm cụ thể (ví dụ: một hàm xử lý ảnh trong C++)
- Sau đó, nó "quan sát" xem dữ liệu đó đã chạy qua những nhánh code nào (gọi là "coverage"). Dựa trên đó, nó "thông minh" tạo ra dữ liệu mới để cố gắng "chạm" tới những nhánh code chưa được kiểm tra, nhằm mục đích tìm ra các lỗi nghiêm trọng như tràn bộ đệm (buffer overflow).

---

## API Scanning

```yml
Jobs/DAST-API.gitlab-ci.yml
```

- Một biến thể của DAST được thiết kế dành riêng cho việc quét API (thay vì quét ứng dụng web đầy đủ).

---