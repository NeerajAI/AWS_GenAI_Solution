import json 
import boto3

bedrock = boto3.client("bedrock-runtime")
def lambda_handler(event, context):
    prompt = event['prompt']
    payload = {
        "anthropic_version" : "bedrock-2023-05-31",
        "max_tokens": 200,
        "messages":[
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body = json.dumps(payload)
    )
    result = json.loads(response['body'].read())

    return result

