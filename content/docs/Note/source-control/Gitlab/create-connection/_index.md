---
title: "Create Connection"
weight: 1
---

# Connect local repository to Gitlab

## Create SSH Key

```powershell
ssh-keygen -t ed25519 -C "email-gitlab-cua-ban@example.com"
```

- Can skip the key password if not necessary

## Show Key

```powershell
cat ~/.ssh/id_ed25519.pub
```

## Add key to Gitlab

1. Đăng nhập vào GitLab.com.
2. Click vào ảnh đại diện (avatar) của bạn ở góc trên bên phải, chọn Preferences.
3. Trong menu điều hướng bên trái, chọn SSH Keys.
4. Paste (dán) key từ terminal vào ô "Key".
5. Đặt tên cho key
6. Nhấn nút Add key.

## Check connection

```powershell
ssh -T git@gitlab.com
```