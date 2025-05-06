import requests

# LM Studio local server endpoint
lmstudio_url = "http://127.0.0.1:1234/v1/chat/completions"

# Model name as loaded in LM Studio (be sure it's exactly matching)
model_name = "qwen3-0.6b"

# Example user prompt
prompt = "Привет! Объясни, как работает квантовая запутанность."

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Payload to send
payload = {
    "model": model_name,
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7,
    "max_tokens": 512,
    "top_p": 0.9
}

try:
    # Send POST request
    response = requests.post(lmstudio_url, headers=headers, json=payload)

    # Check response status
    if response.status_code == 200:
        # Parse JSON response
        result = response.json()
        # Extract assistant reply
        reply = result['choices'][0]['message']['content']
        print(f"Assistant reply:\n{reply}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
