# 🚀 AWS CI/CD Contact Form API

A serverless backend API to receive contact form submissions, built with AWS services and deployed via a full CI/CD pipeline using GitHub ➔ CodePipeline ➔ CodeBuild ➔ Lambda.

---

## 🧰 Tech Stack

- **AWS Lambda** – Backend logic (Python 3.9)
- **API Gateway** – Exposes the API endpoint
- **DynamoDB** – Stores contact form submissions
- **IAM Roles** – Controls Lambda permissions
- **GitHub** – Source code repository
- **AWS CodeBuild** – Builds Lambda artifacts
- **AWS CodePipeline** – Automates CI/CD
- **S3** – Stores build artifacts

---

## 📁 Project Structure

aws-ci-cd-pipeline/ ├── lambda/ │ 
                    └── contact-form/ │ 
                        ├── handler.py # Lambda function code │ 
                        └── requirements.txt # (Optional) external libraries 
                    ├── buildspec.yml # CI/CD instructions for CodeBuild 
                    └── README.md # You're reading this :)

## 🧪 Features

- Submit contact form: `POST /submit`
- Stores `name`, `email`, and `message` in DynamoDB
- Fully automated CI/CD using GitHub and AWS CodePipeline
- Easy to extend with file uploads (via S3)

---

## 📦 Sample API Payload

```json
POST /submit
Content-Type: application/json

{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "message": "Hello from Lambda!"
}


🚧 Deployment Flow

GitHub Push
   ⬇
AWS CodePipeline
   ⬇
CodeBuild (zip Lambda code)
   ⬇
Upload to S3 as artifact
   ⬇
Manual or Automated Lambda Update (Coming soon)

🛠 Setup Instructions

    Create DynamoDB table: ContactFormSubmissions with email as the primary key.

    Create Lambda function: Upload zipped Lambda from lambda/contact-form.

    Create IAM Role for Lambda with:

    AmazonDynamoDBFullAccess

    AWSLambdaBasicExecutionRole

Create HTTP API in API Gateway and connect it to Lambda.

    Set Environment Variable for Lambda:

    TABLE_NAME = ContactFormSubmissions

Create CodeBuild Project:

Source: GitHub

Use buildspec.yml

Create CodePipeline:

Trigger on GitHub commits

Build with CodeBuild

Upload to S3

📌 To-Do / Improvements
 Automate Lambda deployment using CodeDeploy or SAM

 Add email notification (SES)

 Add S3 support for file uploads

 Add unit tests and monitoring (CloudWatch)

📸 Screenshots (optional)
Add screenshots of API Gateway, Lambda test, or DynamoDB data here

🙋‍♂️ Author
Your Name
Jegadeesh K