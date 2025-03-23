import time
import requests

API_KEY = "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"
model_name = "bartowski/Llama-3.2-3B-Instruct-uncensored-GGUF"
API_URL = f"https://api-inference.huggingface.co/models/{model_name}"

def generate_text(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 100
        }
    }
    
    while True:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        elif response.status_code == 503:
            try:
                # Try to parse the JSON response
                error_info = response.json()
                print(f"Model is loading. Estimated time: {error_info.get('error', {}).get('estimated_time', 'unknown')} seconds.")
            except ValueError:
                # If response is not JSON, print raw error message
                print("Error: Model is loading. Response not in JSON format.")
            
            # Wait for the estimated time or 20 seconds if not available
            time.sleep(error_info.get('error', {}).get('estimated_time', 20))  # Default to 20 if not provided
        else:
            return f"Error: {response.status_code}, {response.text}"

# Example usage
prompt = "Tell me about quantum computing."
generated_text = generate_text(prompt)
print(generated_text)
