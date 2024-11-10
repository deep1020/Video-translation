import requests
import time


class VideoTranslationClient:
    def __init__(self, base_url="http://127.0.0.1:5000/status", max_retries=10, initial_delay=1):
        self.base_url = base_url
        self.max_retries = max_retries  # Maximum retries for polling
        self.initial_delay = initial_delay  # Initial delay in seconds for exponential backoff

    def get_status(self):
        # Fetches the current status from the server. Returns the status as a string if the request is successful, or raises an error otherwise.

        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raises an HTTPError for bad responses (e.g. 404)
            return response.json().get("result", "unknown")
        except requests.RequestException as e:
            print(f"An error occurred while fetching status: {e}")
            return "error"

    def wait_for_completion(self):
        # Polls the server for status updates using exponential backoff until it receives 'completed' or 'error', or until max retries are reached.

        delay = self.initial_delay
        for attempt in range(self.max_retries):
            status = self.get_status()
            print(f"Attempt {attempt + 1}: Status = {status}")

            if status in ["completed", "error"]:
                return status  # Stop polling if we reach a terminal state

            time.sleep(delay)
            delay *= 2  # Exponential backoff

        print("Max retries reached. Final status unknown.")
        return "unknown"


if __name__ == "__main__":
    client = VideoTranslationClient()
    final_status = client.wait_for_completion()
    print(f"Final job status: {final_status}")
