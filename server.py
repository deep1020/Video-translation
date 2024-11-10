from flask import Flask, jsonify, send_from_directory
import random
import time
import threading

app = Flask(__name__)
status = "pending"
delay = 10  # configurable delay for simulation

def simulate_processing():
    global status
    time.sleep(delay)  # Wait for the configured delay
    status = random.choice(["completed", "error"])  # Randomly set final status

@app.route('/')
def home():
    return "Welcome to the Video Translation Status API! Use the '/status' endpoint to check the job status."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"result": status})

if __name__ == "__main__":
    # Start the background process to change status
    threading.Thread(target=simulate_processing).start()
    app.run(debug=True, port=5000)
