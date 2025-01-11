import os
import json
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "probabilityplaymakers"
USERS_KEY = "users.json"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

def load_users_from_s3() -> dict:
    """
    Loads the users dictionary from a JSON file in S3.
    Returns an empty dict if the file doesn't exist or on error.
    """
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=USERS_KEY)
        content = response["Body"].read()
        users_dict = json.loads(content)
        return users_dict
    except ClientError as e:
        print(f"Could not load users from S3: {e}")
        return {}

def save_users_to_s3(users_dict: dict) -> bool:
    """
    Saves the given users dictionary to S3 as JSON.
    Returns True if successful, False otherwise.
    """
    try:
        json_str = json.dumps(users_dict)
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=USERS_KEY,
            Body=json_str,
            ContentType="application/json"
        )
        return True
    except ClientError as e:
        print(f"Could not save users to S3: {e}")
        return False
