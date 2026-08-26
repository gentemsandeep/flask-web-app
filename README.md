# 🚀 Cloud & DevOps Web Application on Amazon EKS

A production-style Flask web application deployed on **Amazon EKS**
using Docker, Kubernetes, Amazon ECR, Terraform/CloudFormation,
and GitHub Actions CI/CD.

---

## 👨‍💻 About Me

Hi, I'm **Sandeep Gentem**, a Cloud & DevOps enthusiast focused on
building, automating, and deploying scalable applications on the cloud.

I'm currently developing my expertise in:

- ☁️ AWS
- 🐳 Docker
- ☸️ Kubernetes
- 🏗️ Terraform
- 🐧 Linux
- 🔄 CI/CD
- 🐍 Python
- 🔐 Cloud Security

My goal is to build reliable and automated cloud infrastructure
and grow into a Cloud/DevOps Engineering role.

---

# 📌 Project Overview

This project demonstrates how to containerize a Python Flask application,
push the Docker image to Amazon ECR, deploy it to Amazon EKS using
Kubernetes, expose it through an AWS Load Balancer, and automatically
deploy new application versions using GitHub Actions.

---

# 🏗️ Architecture

```text
                         Developer
                             |
                             | git push
                             ↓
                    ┌─────────────────┐
                    │     GitHub      │
                    └────────┬────────┘
                             |
                             ↓
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    └────────┬────────┘
                             |
                        OIDC 🔐
                             |
                             ↓
                    ┌─────────────────┐
                    │    AWS IAM      │
                    └────────┬────────┘
                             |
                 ┌───────────┴───────────┐
                 ↓                       ↓
          Docker Build                 EKS
                 |                       |
                 ↓                       ↓
              Amazon ECR          Kubernetes
                                         |
                                  ┌──────┴──────┐
                                  ↓             ↓
                                Pod           Pod
                                  \             /
                                   \           /
                                    ↓         ↓
                                  Service
                                     |
                                     ↓
                              AWS Load Balancer
                                     |
                                     ↓
                                   Users

# Project Structure

flask-web-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
│
├── deployment.yaml
├── service.yaml
├── configmap.yaml
├── hpa.yaml
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
└── README.md

# CI/CD Pipeline

Developer
    ↓
git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
AWS OIDC
    ↓
IAM Role
    ↓
Docker Build
    ↓
Amazon ECR
    ↓
Amazon EKS
    ↓
kubectl set image
    ↓
Rolling Update

#Security

GitHub Actions
      |
      ↓
OIDC Token
      |
      ↓
AWS IAM
      |
      ↓
Temporary AWS Credentials

