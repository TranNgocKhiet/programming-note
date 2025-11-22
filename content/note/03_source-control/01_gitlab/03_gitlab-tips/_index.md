---
title: "Gitlab tips"
weight: 1
---

## How to pull a branch from remote that is not in local 

- Get the newest change from remote
```
git fetch origin
```

- List all branches to make sure branch appear
```
git branch -a
```

## Prevent direct merge to branch main, need to merge from dev to main

```yml
check_source_branch:
  stage: .pre
  script:
    - echo "Kiểm tra nhánh nguồn..."
    - |
      if [[ "$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME" != "dev" ]]; then
        echo "❌ LỖI: Bạn chỉ được phép merge vào main từ nhánh 'dev'."
        echo "Nhánh hiện tại của bạn là: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME"
        exit 1
      else
        echo "✅ Hợp lệ: Merge từ dev."
      fi
  rules:
    - if: '$CI_MERGE_REQUEST_TARGET_BRANCH_NAME == "main"'
```