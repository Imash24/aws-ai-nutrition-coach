# AWS-AI-nutrition-coach
A fully serverless AI-powered fitness coach built using AWS Bedrock (Llama 3), Lambda, API Gateway, DynamoDB, CloudFront, and S3.

Users can enter their meal, and the system returns:
Estimated calories
Meal improvement suggestions
Simple fitness guidance
All with extremely low cost due to a serverless architecture.



**Features**
1. AI-powered calorie estimation
2. Meal improvement suggestions
3. Fully serverless
4. Fast global delivery via CloudFront
5. Low operational cost
6. DynamoDB-based history storage



**Architecture Overview**
User Browser
     ↓
CloudFront (CDN)
     ↓
S3 (Static Website Hosting)
     ↓
API Gateway (POST /ask)
     ↓
Lambda (Python - function.py)
     ↓
Amazon Bedrock (Llama 3 8B Instruct)
     ↓
DynamoDB (fitness-coach-history table)




**How It Works**
1. User opens the UI (index.html)
Hosted on S3
Served globally through CloudFront

**2. User enters food details**
Example: “I ate 3 dosas and 2 eggs”.

**3. API Gateway triggers Lambda**
Lambda receives input in JSON.

**4. Lambda calls Amazon Bedrock**
Uses Llama 3 8B Instruct to generate:
Calorie estimation
Meal suggestions

**5. Lambda stores history in DynamoD**B
Each entry contains the userId, timestamp, prompt, and model response.

**6. Response is returned to the UI.**


**Deployment Steps**
1. Upload index.html to S3
Enable static website hosting
Make file public

**2. Create Lambda function**
Runtime: Python 3.x
Upload function.py
Attach IAM role with Bedrock + DynamoDB access

**3. API Gateway setup**
HTTP API
POST /ask
Lambda integration
CORS enabled

**4. Link frontend to backend**
Update API URL inside index.html.

**5. DynamoDB**
Table name: fitness-coach-history
Partition key: userId
Sort key: timestamp

**6. Create CloudFront distribution**
Origin = S3 website hosting endpoint

**Deploy**








**Author**

**Ashwin Venkatesan**
AWS | DevOps | Cloud Engineer
   


