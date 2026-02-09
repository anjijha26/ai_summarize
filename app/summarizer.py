from app.hf_client import call_model

MODEL = "facebook/bart-large-cnn"


def summarize(text: str):
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 80,
            "min_length": 30,
            "do_sample": False
        }
    }

    result = call_model(MODEL, payload)
    return result[0]["summary_text"]
