import requests

# model_name = "t5-base"   "t5-small", "t5-large", "t5-3b", "t5-11b"
# model_name = "bigscience/T0_3B"  # "bigscience/T0", "bigscience/T0p", "bigscience/T0pp"
# model_name = "bigscience/bloom-1b"  # "bigscience/bloom-3b", "bigscience/bloom-7b1"
# model_name = "facebook/opt-1.3b"  # "facebook/opt-2.7b", "facebook/opt-6.7b", "facebook/opt-13b", "facebook/opt-20b", "facebook/opt-30b"
# model_name = "facebook/llama-7b"  # "facebook/llama-13b", "facebook/llama-33b", "facebook/llama-65b"
# model_name = "google/flan-t5-base"  # "google/flan-t5-large", "google/flan-t5-xl", "google/flan-t5-xxl"
# model_name = "google/t5-small"  # "google/t5-base", "google/t5-large", "google/t5-3b", "google/t5-11b"


# Define the model name (this is the model you want to use)
model_name ="gpt2" #"bartowski/Llama-3.2-3B-Instruct-uncensored-GGUF"  # Model you want to use
API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
API_KEY = "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"  # Your Hugging Face API key

# Function to get generated text from the model
def generate_text(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    # Prepare the payload with the input prompt
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 40,  # You can adjust the response length as needed
            "num_return_sequences": 1  # Generate a single response, modify if you need more
        }
    }

    # Send request to Hugging Face API
    response = requests.post(API_URL, headers=headers, json=payload)

    # Parse and return the generated text
    if response.status_code == 200:
        return response .json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage

prompt = input("User : ")
generated_text = generate_text(prompt)
print(f"GPT : {generated_text}")

