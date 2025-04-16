#!/bin/bash
# Basic AWS/GCP enumeration

echo "[*] AWS IAM Roles"
aws iam list-roles

echo "[*] S3 Buckets"
aws s3 ls

echo "[*] GCP IAM Policy"
gcloud projects get-iam-policy YOUR_PROJECT_ID
