# Video Translation

This project contains a server and client library to simulate a video translation job with status polling.

## Files

- `server.py`: It uses Flask to simulate the status API and the simulate_processing function updates the status after a delay.
- `client.py`: A client library that polls the server's `/status` endpoint with exponential backoff. VideoTranslationClient class uses exponential backoff and handles retries, which aligns with the assignment requirements.
- `test_integration.py`: It runs a test to demonstrate the client library's polling functionality. The function wait_for_completion allows us to test the entire polling mechanism.

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

## Screenshots

1. **Server Setup**
   <img width="1115" alt="Screenshot 2024-11-10 at 2 49 55 PM" src="https://github.com/user-attachments/assets/f5f3f1f6-8aa0-4aa9-a73e-6e60bda99d2d">
   
   - In this screenshot, the Flask server (server.py) starts up successfully:
      - The server is running in debug mode and is serving the Flask app named server.
      - The server is accessible at http://127.0.0.1:5000.
      - This output confirms that the server is up and ready to accept requests on port 5000.
   

2. **Client Job Status - Completed (Single Attempt)**
   <img width="1117" alt="Screenshot 2024-11-10 at 2 48 28 PM" src="https://github.com/user-attachments/assets/ec5a010d-f564-487b-a864-c461b5e9ef8b">

   - This output shows the status updates from client.py:
      - The script makes an initial attempt to check the job status.
      - The status returns as "completed" on the first attempt, indicating that the job was successfully processed by the server.
      - The final job status is confirmed as "completed," and the process finishes with an exit code of 0, indicating no errors.
    
3. **Client Job Status - Completed (Multiple Attempts)**
   <img width="1122" alt="Screenshot 2024-11-10 at 2 50 49 PM" src="https://github.com/user-attachments/assets/3166838d-c81f-4805-9996-1878f862fb1f">

   - In this output, client.py checks the job status in multiple attempts:
      - Initial attempts show the job status as "pending."
      - After several attempts, the status eventually updates to "completed."
      - The final job status is "completed," and the script finishes with an exit code of 0. 
