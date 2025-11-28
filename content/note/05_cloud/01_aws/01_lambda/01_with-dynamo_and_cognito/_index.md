---
linkTitle: 'With Dynamo and Cognito'
title: "Lambda Funtion to update Dynamo and Cognito using Python"
<<<<<<<< HEAD:content/note/05_cloud/01_aws/02_lambda/02_with-dynamo_and_cognito/_index.md
weight: 2
========
weight: 1
>>>>>>>> 8b17006269396c49f617707010661f97de79c048:content/note/05_cloud/01_aws/01_lambda/01_with-dynamo_and_cognito/_index.md
---

```python
import boto3
import json
import os

# Create client and handler
dynamodb = boto3.resource('dynamodb')
cognito_client = boto3.client('cognito-idp')

# Get environment variables
TABLE_NAME = os.environ.get('TABLE_NAME')
USER_POOL_ID = os.environ.get('USER_POOL_ID')

table = dynamodb.Table(TABLE_NAME)

def build_update_params(updates):
    update_expression = "SET "
    expression_names = {}
    expression_values = {}
    
    # Use #name and #email to avoid reserved words
    attribute_map = {
        "name": "#name",
        "email": "#email",
    }
    
    for key, value in updates.items():
        if key in attribute_map:
            placeholder = f":{key}"
            attr_name = attribute_map[key]
            
            update_expression += f"{attr_name} = {placeholder}, "
            expression_values[placeholder] = value
            expression_names[attr_name] = key

    update_expression = update_expression.rstrip(", ")

    return update_expression, expression_names, expression_values

def lambda_handler(event, context):
    try:

        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event
                        
        user_id = body.get('userId')
        updates = body.get('updates') 

        if not user_id or not updates:
            return {'statusCode': 400, 'body': 'Lỗi: Thiếu "userId" hoặc "updates"'}

        update_expr, attr_names, attr_values = build_update_params(updates)

        if not attr_values:
            return {'statusCode': 400, 'body': 'Không có trường hợp lệ nào để cập nhật'}

        dynamo_response = table.update_item(
            Key={'userId': user_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=attr_names,
            ExpressionAttributeValues=attr_values,
            ReturnValues="UPDATED_NEW"
        )

        if 'email' in updates:
            new_email = updates['email']
            try:
                cognito_client.admin_update_user_attributes(
                    UserPoolId=USER_POOL_ID,
                    Username=user_id, 
                    UserAttributes=[
                        {
                            'Name': 'email',
                            'Value': new_email
                        },
                        {
                            'Name': 'email_verified',
                            'Value': 'true'
                        }
                    ]
                )
            except Exception as e:
                print(f"Cognito Error: {e}")
                return {
                    'statusCode': 500,
                    'body': f'Update DynamoDB success, but failed to update Cognito: {str(e)}'
                }

        success_body = {
            "message": "Update success",
            "updatedAttributes": dynamo_response.get('Attributes')
        }
        return {
            'statusCode': 200,
            'body': json.dumps(success_body)
        }

    except Exception as e:
        print(f"Unknow error: {e}")
        return {
            'statusCode': 500,
            'body': f'Error when handle request: {str(e)}'
        }
```

---

## Declare and initialize

```py
import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
cognito_client = boto3.client('cognito-idp')

TABLE_NAME = os.environ.get('TABLE_NAME')
USER_POOL_ID = os.environ.get('USER_POOL_ID')

table = dynamodb.Table(TABLE_NAME)
```

- ```import boto3```: Thư viện (**SDK**) chính thức của **AWS** cho **Python**, dùng để tương tác với các **AWS Service**
- ```import json```: Dùng để xử lý dữ liệu **JSON** (ví dụ: ```event["body"]```)
- ```import os```: Dùng để đọc các **Environment variables** trong **Configuration** của **Lambda**
- ```dynamodb = boto3.resource('dynamodb')```: Sử dụng giao diện "resource" (cấp cao, dễ dùng hơn) của ```boto3``` cho **DynamoDB**
- ```cognito_client = boto3.client('cognito-idp')```: Sử dụng giao diện "client" (cấp thấp, chi tiết hơn) cho **Cognito Identity Provider**
- ```TABLE_NAME = os.environ.get('TABLE_NAME')```: Tên của bảng **DynamoDB** chứa thông tin người dùng
- ```USER_POOL_ID = os.environ.get('USER_POOL_ID')```: ID của **Cognito User Pool** nơi người dùng được quản lý
- ```table = dynamodb.Table(TABLE_NAME)```: Tạo một đối tượng **Table** cụ thể từ dynamodb resource, trỏ đến bảng có tên là ```TABLE_NAME```. Điều này giúp thực hiện các thao tác (như ```update_item```) trực tiếp trên bảng đó

---

## build_update_params Function

- ```def build_update_params(updates):```: Khai báo tên hàm, tên tham số
- ```update_expression = "SET "```: Chuỗi lệnh ```SET``` cho **DynamoDB** (ví dụ: ```SET #name = :name, #email = :email```)
- ```expression_names = {}```: Một dictionary để map tên giữ chỗ (placeholder) với tên thuộc tính thật. Ví dụ: ```{"#name": "name"}```. Điều này rất quan trọng để tránh lỗi với các từ khóa dự trữ (reserved words) của **DynamoDB** (như ```name```)
- ```expression_values = {}```: Một dictionary để map tên giữ chỗ với giá trị thật. Ví dụ: ```{":name": "John Doe"}```. Điều này giúp ngăn ngừa lỗi SQL injection (mặc dù đây là **NoSQL**, nguyên tắc tương tự) 

```py
attribute_map = {
    "name": "#name",
    "email": "#email",
}
```
- Định nghĩa một ```attribute_map```. Nó chỉ định rằng nếu ```updates``` có chứa "name" hoặc "email", chúng ta sẽ sử dụng tên giữ chỗ là ```#name``` và ```#email``` trong ```UpdateExpression```

```py
for key, value in updates.items():
    if key in attribute_map:
        placeholder = f":{key}"
        attr_name = attribute_map[key]
            
        update_expression += f"{attr_name} = {placeholder}, "
        expression_values[placeholder] = value
        expression_names[attr_name] = key
```
- ```for key, value in updates.items():```: Lặp qua từng cặp ```key``` (tên trường) và ```value``` (giá trị mới) trong dictionary ```updates``` mà người dùng gửi lên
- ```if key in attribute_map:```: (**Quan trọng**) Chỉ xử lý nếu ```key``` (ví dụ: "name") có trong ```attribute_map```. Nếu người dùng gửi một trường không có trong map (ví dụ: ```{"age": 30}```), nó sẽ bị bỏ qua
- Nếu trường hợp lệ:
<br>&emsp; + ```placeholder = f":{key}"```: Tạo tên giữ chỗ cho giá trị (ví dụ: ```:name```)
<br>&emsp; + ```update_expression += f"{attr_name} = {placeholder}, "```: Thêm vào chuỗi ```update_expression``` (ví dụ: ```SET #name = :name, ``` )
<br>&emsp; + ```expression_values[placeholder] = value```: Thêm giá trị vào ```expression_values``` (ví dụ: ```{":name": "John Doe"}```)
<br>&emsp; + ```expression_names[attr_name] = key```: Thêm tên vào ```expression_names``` (ví dụ: ```{"#name": "name"}```)

- ```update_expression = update_expression.rstrip(", ")```: Xóa dấu phẩy và khoảng trắng thừa ở cuối chuỗi ```update_expression```
- ```return update_expression, expression_names, expression_values```: Trả về 3 thành phần đã được xây dựng

---

## lambda_handler Function

### Update DynamoDB

- ```def lambda_handler(event, context):```: Khai báo tên hàm, tên tham số
- ```try:```: Bắt đầu một khối ```try...except``` lớn để bắt bất kỳ lỗi không mong muốn nào

```py
if "body" in event:
    body = json.loads(event["body"])
else:
    body = event
```
- Xử lý ```event```. Nếu **Lambda** này được kích hoạt bởi **API Gateway**, dữ liệu POST/PUT sẽ nằm trong ```event["body"]``` dưới dạng một chuỗi JSON. Cần ```json.loads``` để biến nó thành dictionary. Nếu không, (ví dụ: chạy test trực tiếp trong **Lambda**), event chính là ```body```

- ```user_id = body.get('userId')```: Lấy ```userId```
- ```updates = body.get('updates')```: Lấy dictionary ```updates```

```py
if not user_id or not updates:
            return {'statusCode': 400, 'body': 'Lỗi: Thiếu "userId" hoặc "updates"'}
```
- Kiểm tra xem ```userId``` và ``` updates``` có tồn tại không. Nếu thiếu, trả về lỗi ```400 Bad Request```

- ```update_expr, attr_names, attr_values = build_update_params(updates)```: Gọi hàm ```build_update_params``` đã giải thích ở trên
  
```py
if not attr_values:
            return {'statusCode': 400, 'body': 'Không có trường hợp lệ nào để cập nhật'}
```
- Nếu ```attr_values``` rỗng (nghĩa là người dùng đã gửi ```updates``` nhưng không chứa "name" hay "email"), trả về lỗi ```400```

```py
dynamo_response = table.update_item(
    Key={'userId': user_id},
    UpdateExpression=update_expr,
    ExpressionAttributeNames=attr_names,
    ExpressionAttributeValues=attr_values,
    ReturnValues="UPDATED_NEW"
)
```
- ```dynamo_response = table.update_item()```: Đây là lệnh chính thức cập nhật **DynamoDB**
- ```Key={'userId': user_id}```: Chỉ định item nào cần cập nhật (dựa trên **Primary Key**)
- Cung cấp 3 tham số đã được tạo ra bởi hàm ```build_update_params```
- ```ReturnValues="UPDATED_NEW"```: Yêu cầu DynamoDB trả về giá trị mới của các thuộc tính vừa được cập nhật

---

### Update Cognito

```py
if 'email' in updates:
    new_email = updates['email']
    try:
        cognito_client.admin_update_user_attributes(
            UserPoolId=USER_POOL_ID,
            Username=user_id, 
            UserAttributes=[
                { 'Name': 'email', 'Value': new_email },
                { 'Name': 'email_verified', 'Value': 'true' }
            ]
        )
```

- ```if 'email' in updates:```: Chỉ thực hiện khối này nếu email là một trong các trường được yêu cầu cập nhật
- ```new_email = updates['email']```: Lấy địa chỉ email mới
- ```try:```: Bắt đầu một khối ```try...except``` lồng nhau. Điều này rất quan trọng: nó cho phép bắt lỗi **Cognito** một cách riêng biệt
- ```cognito_client.admin_update_user_attributes()```: Gọi hàm ```admin_update_user_attributes``` của **Cognito**
- ```UserPoolId=USER_POOL_ID,```: Chỉ định **UserPoolId**
- ```Username=user_id,```: Chỉ định Username (trong Cognito, Username thường chính là userId hoặc sub của người dùng)
- Cập nhật thuộc tính ```email``` thành giá trị mới, và đồng thời đánh dấu ```email_verified``` là ```true```. Đây là một hành động "admin", giả định rằng email do admin cập nhật là đã được xác thực

```py
except Exception as e:
    print(f"Cognito Error: {e}")
    return {
        'statusCode': 500,
        'body': f'Update DynamoDB success, but failed to update Cognito: {str(e)}'
    }
```
- Nếu có lỗi xảy ra chỉ với **Cognito** (ví dụ: ```email``` không hợp lệ, người dùng không tồn tại trong **Cognito**), hàm sẽ dừng và trả về lỗi **500**, nó nói rõ: "Update DynamoDB success, but failed to update Cognito"

---

### Return Successs and catch general Exception

```py
success_body = {
    "message": "Update success",
    "updatedAttributes": dynamo_response.get('Attributes')
}
return {
    'statusCode': 200,
    'body': json.dumps(success_body)
}
```
- Nếu mọi thứ chạy suôn sẻ (cả **DynamoDB** và **Cognito** (nếu có)), tạo một ```body``` phản hồi thành công. Nó bao gồm các thuộc tính đã được cập nhật lấy từ ```dynamo_response``` (nhờ ```ReturnValues="UPDATED_NEW"```)
- Trả về phản hồi ```200 OK``` với body đã được chuyển thành chuỗi **JSON**

```py
except Exception as e:
    print(f"Unknow error: {e}")
    return {
        'statusCode': 500,
        'body': f'Error when handle request: {str(e)}'
    }
```
- ```except Exception as e:```: Đây là khối ```except``` của ```try``` lớn bên ngoài
- Nếu có bất kỳ lỗi nào khác xảy ra (ví dụ: lỗi parse **JSON**, lỗi **DynamoDB**, lỗi **Evironment variables** bị thiếu...), nó sẽ bị bắt ở đây và trả về lỗi ```500 Internal Server Error```

---