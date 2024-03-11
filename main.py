from fastapi import FastAPI, HTTPException, Body
import boto3
from boto3.dynamodb.conditions import Attr
from fastapi import status 
from random import randint
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')

# Reference to your DynamoDB table
table = dynamodb.Table('QuestionAnswer')

@app.get("/random-item")
async def read_random_item():
    # Scan the table to get all items (Note: This is not efficient for large tables)
    response = table.scan()

    items = response['Items']
    
    # Select a random item if items exist
    if items:
        random_index = randint(0, len(items) - 1)
        random_item = items[random_index]
        return {"question": random_item["question"], "answer": random_item.get("answer", "")}
    else:
        return {"message": "No items found in the table."}

app = FastAPI()



@app.post("/save-answer", status_code=status.HTTP_200_OK)
async def save_answer(item: dict = Body(...)):
    """
    Save or update an answer in the DynamoDB table.
    Expects a JSON object with 'question' and 'answer'.
    """
    question = item.get("question")
    updated_answer = item.get("answer")
    
    # Ensure the item contains required fields
    if not question or updated_answer is None:
        raise HTTPException(status_code=400, detail="Missing 'question' or 'answer' in the request body.")
    
    try:
        # Update the item in DynamoDB
        response = table.update_item(
            Key={
                'question': question  # Assuming 'question' is the primary key for your table
            },
            UpdateExpression="set answer = :a",
            ExpressionAttributeValues={
                ':a': updated_answer
            },
            ReturnValues="UPDATED_NEW"
        )
        return {"message": "Answer updated successfully", "updatedAttributes": response.get('Attributes')}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
