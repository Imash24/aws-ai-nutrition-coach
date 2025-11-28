import json
import boto3
import time
import os
from datetime import datetime

# Clients for Bedrock and DynamoDB
bedrock = boto3.client("bedrock-runtime")
dynamodb = boto3.client("dynamodb")

TABLE = os.environ["TABLE_NAME"]
MODEL_ID = os.environ["MODEL_ID"]

def lambda_handler(event, context):
    # 1) Parse HTTP request body
    body_str = event.get("body", "{}")
    try:
        body = json.loads(body_str)
    except:
        body = {}

    prompt = body.get("prompt")
    user_id = body.get("userId", "defaultUser")

    if not prompt:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "prompt required"})
        }

    # 2) Build Llama 3 prompt (instruction style)
    system_message = (
        "You are a strict but friendly fitness coach. "
        "First line MUST be: 'Estimated: ~XXX kcal' if the user describes food. "
        "Then give simple, practical advice and 2-3 improvements. "
        "If the user asks workout questions, give sets, reps, and rest time. "
        "Avoid medical claims."
    )

    llama_prompt = (
        "<|begin_of_text|>"
        "<|start_header_id|>system<|end_header_id|>\n"
        f"{system_message}\n"
        "<|start_header_id|>user<|end_header_id|>\n"
        f"{prompt}\n"
        "<|start_header_id|>assistant<|end_header_id|>\n"
    )

    request_body = {
        "prompt": llama_prompt,
        "max_gen_len": 300,
        "temperature": 0.7
    }

    # 3) Call Llama 3 on Bedrock
    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        contentType="application/json",
        body=json.dumps(request_body)
    )

    payload = json.loads(response["body"].read())

    # Llama 3 Instruct returns 'generation'
    ai_output = payload.get("generation")

    if not ai_output:
        ai_output = "Model did not return output. Please try again."

    # 4) Save to DynamoDB
    timestamp = str(int(time.time()))
    date_str = datetime.utcnow().strftime("%Y-%m-%d")

    dynamodb.put_item(
        TableName=TABLE,
        Item={
            "userId": {"S": user_id},
            "timestamp": {"S": timestamp},
            "prompt": {"S": prompt},
            "response": {"S": ai_output},
            "date": {"S": date_str}
        }
    )

    # 5) Return JSON response
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({"fitness_coach_reply": ai_output})
    }
