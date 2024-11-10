# Video Translation

This project contains a server and client library to simulate a video translation job with status polling.

## Files

- `server.py`: It uses Flask to simulate the status API and the simulate_processing function updates the status after a delay.
- `client.py`: A client library that polls the server's `/status` endpoint with exponential backoff. VideoTranslationClient class uses exponential backoff and handles retries, which aligns with the assignment requirements.
- `test_integration.py`: Runs a test to demonstrate the client library's polling functionality. The function wait_for_completion allow us to test the entire polling mechanism.

## Setup Instructions

1. **Install Dependencies:**

   ```bash
   pip install Flask requests
   ```

2. **Start the Server:**

   ```bash
   python server.py
   ```

3. **Run the Client:**

   ```bash
   python client.py
   ```

4. **Run the Integration Test:**

   ```bash
   python test_integration.py
   ```

## How It Works

The client polls the server's `/status` endpoint with an exponential backoff strategy, stopping once it gets a `completed` or `error` status, or after reaching the maximum retries.
