import os
import requests

HF_TOKEN = os.getenv("HF_Token")

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def call_model(model_name: str, payload: dict):
    url = f"https://router.huggingface.co/hf-inference/models/{model_name}"
    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    return response.json()
