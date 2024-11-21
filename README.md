
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
   pip install -r requirements.txt
   ```

## Step 3: Run the Ollama Server
1. **Switch to the Ollama model of your choice**:
   Change the model in this part of the Ollama_Server.py:
   ```python
   result = subprocess.run(
      ["ollama", "run", "llama3.2:1b"],
      input=prompt,
      capture_output=True,
      text=True  # Ensures output is decoded to a string automatically
   )
   ```
2. **Start the server**:
   From the server folder, Run the following command to start the server:
   ```bash
   python Ollama_Server.py
   ```
   
   This will host a local server on `http://localhost:5001/chat`, which serves as the endpoint for querying the model.

## Step 4: Run the Python Code to Query the Model
1. **Write Your Python Script** (e.g., `RAG.py`), or use the following template:

   ```python
   import slm

   # Initialize LocalLLM with the specified endpoint URL
   llm = slm.local_llm(endpoint_url="http://localhost:5001/chat")

   # Query the model
   response = llm._call("Tell me a joke")
   print("Response from model:", response)
   ```
2. **enter your API key for any tools used in the Script**

3. **Run the Script**:
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
