
# Local LLM Server Setup and Usage Guide

This guide walks you through setting up a local server using **Ollama** to interact with a language model and running your Python code to query the model.

### Prerequisites
1. **Python 3.8 or higher** installed on your machine.
2. **Ollama** installed (steps below).

---

## Step 1: Install Ollama
Download and install [Ollama](https://ollama.com/) on your machine. This will allow you to run the LLaMA model locally.

## Step 2: Set Up the Virtual Environment
1. **Create a Virtual Environment** (if you haven’t already):
   ```bash
   python3 -m venv env-name
   ```
   
2. **Activate the Virtual Environment**:
   In your bash terminal, run:
   ```bash
   source env-name/bin/activate
   ```
   For example
   ```bash
   source llm-env/bin/activate
   ```
   
   Ensure you’re in the virtual environment by checking that your prompt shows the environment name (e.g., `(env-name)`).

3. **Install Required Dependencies**:
   ```bash
   pip install flask requests langchain pydantic
   ```

## Step 3: Run the Ollama Server
1. **Start the Server**:
   From the Server folder, Run the following command to start the server:
   ```bash
   python Ollama_Server.py
   ```
   
   This will host a local server on `http://localhost:5001/chat`, which serves as the endpoint for querying the model.

## Step 4: Run the Python Code to Query the Model
1. **Write Your Python Script** (e.g., `Chat.py`), or use the following template:

   ```python
   import SLM

   # Initialize LocalLLM with the specified endpoint URL
   llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

   # Query the model
   response = llm._call("Tell me a joke")
   print("Response from model:", response)
   ```

2. **Run the Script**:
   Execute your Python script to get a response from the model:
   ```bash
   python Chat.py
   ```

---

## Example Output
When you run the script, you should see a response printed to the terminal:

```plaintext
Response from model: Why did the chicken cross the road? To get to the other side!
```

---

### Additional Notes
- If you prefer to use a `chat` method instead of `_call`, add it to the `LocalLLM` class.
- The server setup in `Ollama_Server.py` must be running whenever you query the model.
