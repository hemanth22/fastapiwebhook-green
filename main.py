from fastapi import FastAPI, HTTPException
from fastapi import Request
import requests
import os
import json

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    content_type = request.headers.get("Content-Type")
    
    if content_type == "application/json":
        # Handle JSON payload
        payload = await request.json()
        print("Webhook received (JSON): ", payload)
        payloaddata = json.loads(json.dumps(payload))
        IFTTT_PAYLOAD = {
            "value1": payloaddata["message"],
            "value2": " by ",
            "value3": payloaddata["source"]
         }
        print("Transformed JSON to client: ", IFTTT_PAYLOAD)
        
        # Handle the JSON payload as needed
    elif content_type == "application/x-www-form-urlencoded":
        # Handle form data
        form_data = await request.form()
        print("Webhook received (Form data):", form_data)
        # Handle the form data as needed
    else:
        raise HTTPException(status_code=400, detail="Unsupported content type")

    return {"status": "Webhook received successfully"}
