import requests
import sys
import time

# === Define file path and constants ===
prompt_file = '../text_in.txt'
output_file = '../text_out.txt'
lmstudio_url = "http://127.0.0.1:1234/v1/chat/completions"
model_name = "qwen3-0.6b"
headers = {"Content-Type": "application/json"}

# === Read prompt from file ===
def read_prompt(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                sys.exit(f"Error: File '{path}' is empty.")
            return content
    except FileNotFoundError:
        sys.exit(f"Error: File '{path}' not found.")
    except Exception as e:
        sys.exit(f"Error reading '{path}': {e}")

prompt = read_prompt(prompt_file)

# === Prepare request payload ===
payload = {
    "model": model_name,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.7,
    "max_tokens": 4096,  # Increase max tokens
    "top_p": 0.9
}

# === Send request and process response ===
def send_request(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            sys.exit(f"Request failed: {response.status_code}\n{response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        sys.exit(f"Request error: {e}")

# === Extract and assemble full reply ===
def extract_full_reply(response_data):
    choices = response_data.get('choices', [])
    if choices and 'message' in choices[0] and 'content' in choices[0]['message']:
        return choices[0]['message']['content'], choices[0].get('finish_reason', 'stop')
    sys.exit("Error: Unexpected response structure.")

full_reply = ""
current_payload = payload.copy()
while True:
    result = send_request(lmstudio_url, headers, current_payload)
    reply, finish_reason = extract_full_reply(result)
    full_reply += reply
    if finish_reason != 'length':
        break
    # Add slight delay between requests
    time.sleep(1)
    # Update prompt with latest context
    current_payload['messages'].append({"role": "assistant", "content": reply})

# === Print reply to console ===
print(f"Assistant reply:\n{full_reply}")

# === Write reply to output file ===
try:
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(full_reply)
except Exception as e:
    sys.exit(f"Error writing to '{output_file}': {e}")
