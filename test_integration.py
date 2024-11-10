import subprocess
import time
from client import VideoTranslationClient


def start_server():
    return subprocess.Popen(["python", "server.py"])


def test_client():
    client = VideoTranslationClient("http://127.0.0.1:5000")
    final_status = client.get_status()
    print("Test completed with status:", final_status)


if __name__ == "__main__":
    server_process = start_server()
    time.sleep(2)  # Give the server time to start

    try:
        test_client()
    finally:
        server_process.terminate()  # Ensure server is terminated after test
