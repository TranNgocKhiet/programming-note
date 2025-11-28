---
title: "AWS CloudFormation"
weight: 4
---

## Exmaple project

[smart_office_api_gateway](smart_office_api_gateway.yaml)

[smart_office_lambda_authenticate](smart_office_lambda_authenticate.yaml)

[smart_office_budget](smart_office_budget.yaml)

[smart_office_cognito](smart_office_cognito.yaml)

[smart_office_lambda_crud](smart_office_lambda_crud.yaml)

[smart_office_dynamodb](smart_office_dynamodb.yaml)

[smart_office_lambda_readonly](smart_office_lambda_readonly.yaml)

[smart_office_s3_cloudfront](smart_office_s3_cloudfront.yaml)

## Note

### ```smart_office_cognito.yaml```

- Hướng dẫn sử dụng sau khi Deploy
1. Lấy Mật khẩu: Vì **CloudFormation** không cho phép đặt mật khẩu trực tiếp (để bảo mật), sau khi deploy xong, bạn cần vào **AWS Console** > **Cognito** > **Users**:
<br>&emsp; + Bấm vào từng **user** (```admin```, ```manager1```...).
<br>&emsp; + Chọn **Admin set password**.
<br>&emsp; + Đặt mật khẩu test (ví dụ: ```123456```) và tick chọn **Permanent** (để không bị bắt đổi pass lúc login lần đầu cho tiện).
2. Cấu hình Web (**S3**/**CloudFront**):
<br>&emsp; + Trong code Frontend, bạn sẽ cần 2 thông số từ phần Outputs: ```UserPoolId``` và ```WebClientId```.

### When create Stack

1. Stack Failure Options (Chế độ khi lỗi) - Mẹo Debug
Mặc định, nếu stack bị lỗi ở bất kỳ bước nào, CloudFormation sẽ Rollback (Xóa sạch mọi thứ vừa tạo để quay về trạng thái ban đầu).

Vấn đề: Khi Rollback, mọi log lỗi cũng biến mất theo, rất khó để biết tại sao sai (đặc biệt là với Custom Resource hoặc Lambda).

Lời khuyên (Cho môi trường Dev):

Ở bước "Configure stack options", tìm mục Stack failure options.

Chọn Preserve successfully provisioned resources (Giữ lại tài nguyên đã tạo thành công).

Việc này giúp stack dừng lại ngay chỗ bị lỗi, cho phép bạn vào xem logs để sửa, sau đó update tiếp thay vì phải tạo lại từ đầu.

2. Termination Protection (Chống xóa nhầm) - Sống còn cho Database
Bạn không bao giờ muốn lỡ tay xóa nhầm Stack chứa Database hay User Pool đang chạy thật (Prod).

Lý do: Xóa Stack = Xóa luôn bảng DynamoDB và toàn bộ dữ liệu người dùng bên trong.

Hành động:

Với Stack DynamoDB và Auth (Cognito): Hãy bật Enable termination protection.

Khi bật cái này, nếu ai đó bấm nút "Delete Stack", AWS sẽ từ chối. Muốn xóa, bạn phải vào tắt bảo vệ trước.