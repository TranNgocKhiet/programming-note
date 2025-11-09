---
title: "Deployment Template"
weight: 2
---

# Deployment Template on Gitlab

## Cloud and Virtual Machine

```yml
AWS/CF-Provision-and-Deploy-EC2.gitlab-ci.yml
```
- Dùng CloudFormation để tạo hạ tầng và deploy lên EC2
  
```yml
AWS/Deploy-EC2.gitlab-ci.yml
```

- Deploy một ứng dụng lên EC2

```yml
AWS/ECS.gitlab-ci.yml
```

- Deploy lên Dịch vụ AWS ECS
  
```yml
Jobs/Deploy/ECS.gitlab-ci.yml
```

- Một template công việc (job) để deploy lên ECS, thường được dùng bởi Auto DevOps

```yml
Jobs/Deploy.gitlab-ci.yml
```

- Template công việc deploy cơ bản

```yml
GCP.gitlab-ci.yml
```

- Template chung cho Google Cloud Platform

```yml
Heroku.gitlab-ci.yml
```

- Deploy lên Heroku

```yml
Serverless.gitlab-ci.yml
```

- Template chung cho framework Serverless

```yml
AWS/EKS.gitlab-ci.yml
```

- Deploy lên Amazon EKS - Kubernetes

```yml
AWS/lambda-deploy.gitlab-ci.yml
```

- Deploy hàm AWS Lambda

---

## Container & Kubernetes

```yml
OpenShift.gitlab-ci.yml
```

- Dành cho việc triển khai lên nền tảng OpenShift

```yml
Packer.gitlab-ci.yml
```

- Dùng để build và đẩy (push) Docker image

---

## Infrastructure as Code (IaC) Deploying

```yml
Terraform.gitlab-ci.yml
```

- Template chính cho Terraform để quản lý hạ tầng

```yml
Terraform.latest.gitlab-ci.yml
```

- Luôn dùng phiên bản Terraform mới nhất

```yml
Terraform.gitlab-ci.yml
```

- Dùng để tạo các machine image

---

## PaaS Platform & Static Website

```yml
Pages/Auto-DevOps.gitlab-ci.yml
```

- Dùng cho GitLab Pages

```yml
Pages/Hugo.gitlab-ci.yml
```

- Dùng cho trang tĩnh Hugo

```yml
Pages/Jekyll.gitlab-ci.yml
```

- Dùng cho trang tĩnh Jekyll

```yml
Pages/HTML.gitlab-ci.yml
```

- Template cơ bản nhất, nó không "build" gì cả, chỉ đơn giản là lấy một thư mục (thường là public) chứa các tệp HTML/CSS/JS tĩnh của bạn và deploy chúng

```yml
Pages/Gatsby.gitlab-ci.yml
```

- Dùng cho Gatsby để build các trang web tĩnh hiệu suất cao bằng React và GraphQL

```yml
Pages/Docusaurus.gitlab-ci.yml
```

- Dùng để build và deploy các trang web làm bằng Docusaurus. Đây là SSG do Meta (Facebook) tạo ra, rất mạnh mẽ để xây dựng các trang tài liệu (documentation), đặc biệt là cho các dự án React

```yml
Pages/Eleventy.gitlab-ci.yml
```

- Dùng cho Eleventy (11ty). Đây là một SSG hiện đại, linh hoạt và rất nhẹ, không phụ thuộc vào một framework JavaScript cụ thể (như React hay Vue)

```yml
Pages/GitBook.gitlab-ci.yml
```

- Dùng cho GitBook, một công cụ chuyên dụng để xây dựng các cuốn sách trực tuyến, tài liệu kỹ thuật, hoặc cơ sở tri thức (knowledge base) đẹp mắt

```yml
Pages/MkDocs.gitlab-ci.yml
```

- Dùng cho MkDocs, một SSG viết bằng Python, được thiết kế đặc biệt để tạo các trang tài liệu (docs) từ các tệp Markdown một cách nhanh chóng và đơn giản.

```yml
Pages/Pelican.gitlab-ci.yml
```

- Dùng cho Pelican, một SSG khác cũng được viết bằng Python, thường được dùng để tạo blog và các trang web cá nhân.

```yml
Pages/VuePress.gitlab-ci.yml
```

- Dùng cho VuePress, một SSG được phát triển bởi nhóm Vue.js, tối ưu hóa cho việc viết tài liệu kỹ thuật, với các tính năng tích hợp sẵn cho việc này.

---