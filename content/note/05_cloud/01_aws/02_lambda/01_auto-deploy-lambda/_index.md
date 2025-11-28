---
linkTitle: 'Auto deploy Lambda'
title: "Auto deploy code from S3 to Lambda with Gitlab CI/CD Pipelines"
weight: 1
---

## Template

```yml
stages:
  - deploy

deploy_lambda_job:
  stage: deploy
  image:
    name: amazon/aws-cli:latest
    entrypoint: [""]
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      changes:
        - lambda/**/*
  before_script:
    - yum install -y zip
  script: |
    echo "--- Bắt đầu deploy Lambda (Chạy song song) ---"

    cd lambda

    # Kiểm tra xem có file .py nào không để tránh lỗi nếu folder rỗng
    if ls *.py 1> /dev/null 2>&1; then
      for file in *.py; do
        func_name=$(basename "$file" .py)
        echo ">>> Đang xử lý: $func_name"

        # 1. Zip file
        zip -j "${func_name}.zip" "$file"
        
        # 2. Upload S3
        echo "Upload $func_name lên S3..."
        aws s3 cp "${func_name}.zip" "s3://$S3_BUCKET_LAMBDA/functions/${func_name}.zip" --region $AWS_DEFAULT_REGION
        
        # 3. Update Lambda
        echo "Update code cho Lambda function..."
        aws lambda update-function-code \
          --function-name "$func_name" \
          --s3-bucket "$S3_BUCKET_LAMBDA" \
          --s3-key "functions/${func_name}.zip" \
          --region $AWS_DEFAULT_REGION
          
        # Dọn dẹp
        rm "${func_name}.zip"
      done
    else
      echo "Không tìm thấy file .py nào trong thư mục lambda."
    fi
```

## Code explaination

```yml
rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      changes:
        - lambda/**/*
```

- Chỉ chạy khi code được merge vào nhánh ```main``` và có sự thay đổi file trong thư mục ```lambda/``` 

```yml
before_script:
    - yum install -y zip
```

- Lệnh này cài đặt công cụ ```zip``` vì **AWS Lambda** yêu cầu code phải được nén thành file ```.zip``` trước khi upload. ```-y``` để tự động đồng ý (yes) khi cài đặt

```yml
if ls *.py 1> /dev/null 2>&1; then
```

- ```1> /dev/null```: 
<br>&emsp; + ```1```: Số 1 (Standard Output - stdout) - Nơi xuất ra kết quả bình thường (Ví dụ: danh sách file).
<br>&emsp; + ```>```: Dấu chuyển hướng (Redirect).
<br>&emsp; + ```/dev/null```: Đây là một file đặc biệt trong hệ thống **Linux**. Mọi thứ bạn ném vào đây sẽ biến mất vĩnh viễn. Nó giống như một cái thùng rác không đáy.
<br>&emsp; + **Ý nghĩa**: "Nếu lệnh chạy thành công, hãy ném kết quả vào hố đen (đừng in ra màn hình)".

- ```2>&1```:
<br>&emsp; + ```2```: Số 2 (Standard Error - stderr) - Nơi xuất ra thông báo lỗi (Ví dụ: "File not found").
<br>&emsp; + ```>```: Chuyển hướng.
<br>&emsp; + ```&1```: Tham chiếu đến nơi mà số 1 đang đi tới.
<br>&emsp; + **Ý nghĩa**: "Nếu có lỗi, hãy ném thông báo lỗi vào cùng chỗ với kết quả bình thường (tức là cũng ném vào hố đen luôn)".

- Mục đích của dòng này chỉ là kiểm tra xem có file nào tồn tại hay không (trả về True/False cho lệnh if), chứ bạn không muốn in danh sách file ra, và càng không muốn in lỗi ra.
- Nếu có file: Lệnh ls chạy thành công -> Output bị giấu đi (gọn log).
- Nếu KHÔNG có file: Lệnh ls sẽ la lên "ls: cannot access '.py': No such file or directory"* 
- Nếu không có 2>&1, câu báo lỗi này sẽ hiện đỏ lòm trên màn hình console của GitLab CI, làm bạn tưởng pipeline bị lỗi (dù thực tế logic code đã xử lý trường hợp else rồi).

```yml
func_name=$(basename "$file" .py)
```

- ```basename``` sẽ bỏ phần thư mục cha (vd: ```/lambda/func.py``` -> ```func.py```) và hậu tố được khai báo, trong trường hợp này là ```.py```
- ```$``` sẽ thực thi code bên trong ```()``` trước rồi lấy kết quả gán vào ```func_name```
    
```yml
zip -j "${func_name}.zip" "$file"
```

- Nén file code .py thành file .zip
- ```-j``` (junk paths): Quan trọng - Nó đảm bảo file trong zip không chứa cấu trúc thư mục (vd: không phải lambda/login.py mà chỉ là login.py). Lambda cần file nằm ngay root của gói zip.

```yml
aws s3 cp "${func_name}.zip" "s3://$S3_BUCKET_LAMBDA/functions/${func_name}.zip" --region $AWS_DEFAULT_REGION
```

- Copy file ```zip``` vừa tạo lên **AWS S3**
- ```$S3_BUCKET_LAMBDA```: Biến môi trường (cần được cài đặt trong **GitLab** CI/CD Settings) chứa tên **Bucket**.
- ```$AWS_DEFAULT_REGION```: Biến môi trường chứa **region** (ví dụ: ```ap-southeast-1```).
  
```yml
aws lambda update-function-code \
          --function-name "$func_name" \
          --s3-bucket "$S3_BUCKET_LAMBDA" \
          --s3-key "functions/${func_name}.zip" \
          --region $AWS_DEFAULT_REGION
```

- Lệnh này báo cho AWS Lambda biết cần lấy code mới từ S3
- ```--function-name "$func_name"```: Tên hàm Lambda cần update.
- ```--s3-bucket "$S3_BUCKET_LAMBDA"``` ```--s3-key "functions/${func_name}.zip"```: Đường dẫn tới file zip vừa upload ở bước trên.
- ```--region $AWS_DEFAULT_REGION```: Biến môi trường chứa **region** (ví dụ: ```ap-southeast-1```).

```yml
rm "${func_name}.zip"
```

- Xóa file ```zip``` tạm sau khi đã deploy xong để giữ workspace sạch sẽ cho vòng lặp tiếp theo (hoặc tránh đầy ổ cứng runner).

## Important notice

- **Tên file chứa code phải trùng với tên lambda function, nếu không ci/cd sẽ gặp lỗi**

```yml
- image:
    name: amazon/aws-cli:latest
    entrypoint: [""]
``` 

- Thêm ```entrypoint``` rỗng nếu muốn chạy những lệnh nằm ngoài image đã khái báo
- Ví dụ trên sẽ cho phép chạy lệnh ```sh``` thay vì ```aws sh``` khi không có ```entrypoint: [""]```

```yml
--region $AWS_DEFAULT_REGION
```

- Thêm biến môi trường ```AWS_DEFAULT_REGION``` (như ```ap-southeast-1``` cho Singapore), nếu không ci/cd sẽ gặp lỗi