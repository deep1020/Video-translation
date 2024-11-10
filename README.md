# Video Translation

This project contains a server and client library to simulate a video translation job with status polling.

## Files

- `server.py`: Simulates a backend server that updates job status.
- `client.py`: A client library that polls the server's `/status` endpoint with exponential backoff.
- `test_integration.py`: Runs a test to demonstrate the client library's polling functionality.

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
