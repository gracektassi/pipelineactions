import json
import boto3
import os
import uuid


table_name = os.environ.get("TABLE_NAME")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)


def handler(event, context):

    method = event["httpMethod"]
    if method == "POST":
        item = json.loads(event["body"])  # Parse the request body
        item["id"] = str(uuid.uuid4())  # Generate a unique ID for the item
        table.put_item(Item=item)  # Save the item in DynamoDB

        # Return a response with the item ID
        return {
            "statusCode": 200,
            "body": json.dumps({"id": item["id"]}),
            "headers": {
                    "Access-Control-Allow-Origin": "*",  # Allow all origins
                    "Access-Control-Allow-Methods": "POST, GET",  # Allow POST and GET methods
                    "Access-Control-Allow-Headers": "Content-Type",  # Allow Content-Type header
                },
            
        }
    if method == "GET":
        empl_id = event["queryStringParameters"]["id"]
        response = table.get_item(Key={"id": empl_id})
        if "Item" in response:
            return {
                "statusCode": 200,
                "body": json.dumps(response["Item"]),
                "headers": {
                    "Access-Control-Allow-Origin": "*",  # Allow all origins
                    "Access-Control-Allow-Methods": "POST, GET",  # Allow POST and GET methods
                    "Access-Control-Allow-Headers": "Content-Type",  # Allow Content-Type header
                },
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps("Not found"),
                "headers": {
                    "Access-Control-Allow-Origin": "*",  # Allow all origins
                    "Access-Control-Allow-Methods": "POST, GET",  # Allow POST and GET methods
                    "Access-Control-Allow-Headers": "Content-Type",  # Allow Content-Type header
                },
            }
