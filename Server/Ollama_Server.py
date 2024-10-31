from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Endpoint to chat with the model
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    # Debugging: check and confirm prompt type and content
    print(f"Received prompt: {prompt}")
    print(f"Type of prompt before processing: {type(prompt)}")

    try:
        # Ensure `prompt` is in string format
        if isinstance(prompt, bytes):
            prompt = prompt.decode()  # Decode if `prompt` is bytes
        elif not isinstance(prompt, str):
            prompt = str(prompt)  # Convert to string if it's any other type

        # Confirm prompt is now a string
        print(f"Type of prompt after conversion: {type(prompt)}")

        # Send prompt to subprocess without re-encoding, as `text=True` handles it as a string
        result = subprocess.run(
            ["ollama", "run", "llama3.2:1b"],
            input=prompt,
            capture_output=True,
            text=True  # Ensures output is decoded to a string automatically
        )
        response = result.stdout.strip()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Accessible via localhost:5001