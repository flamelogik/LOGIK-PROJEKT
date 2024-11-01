#!/bin/bash

# Prompt the user to enter the project name
read -p "Enter the project name (use only lowercase letters, numbers, and hyphens): " PROJECT_NAME

# Send the project name to Zapier webhook
curl -X POST -H "Content-Type: application/json" -d "{\"project_name\":\"$PROJECT_NAME\"}" https://hooks.zapier.com/hooks/catch/9358762/290g3p1/
echo "Project '$PROJECT_NAME' sent to Zapier."

# Create an S3 bucket with the same project name in us-east-1
aws s3api create-bucket --bucket "$PROJECT_NAME" --region us-east-1

if [ $? -eq 0 ]; then
    echo "S3 bucket '$PROJECT_NAME' created successfully in us-east-1."
else
    echo "Failed to create S3 bucket '$PROJECT_NAME'. Please check the AWS CLI configuration and bucket naming constraints."
fi

