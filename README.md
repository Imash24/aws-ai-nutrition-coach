# AI-Fitness-Coach-Serverless-Calorie-Meal-Recommendation-App-AWS-BedRock-
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


**Project Structure**
/project-root
│
├── index.html         # Frontend UI (S3 + CloudFront)
├── function.py        # AWS Lambda backend logic
└── README.md          # Documentation




**How It Works**
1. User opens the UI (index.html)
Hosted on S3
Served globally through CloudFront

2. User enters food details
Example: “I ate 3 dosas and 2 eggs”.

3. API Gateway triggers Lambda
Lambda receives input in JSON.

4. Lambda calls Amazon Bedrock
Uses Llama 3 8B Instruct to generate:
Calorie estimation
Meal suggestions

5. Lambda stores history in DynamoDB
Each entry contains the userId, timestamp, prompt, and model response.

6. Response is returned to the UI.

   


