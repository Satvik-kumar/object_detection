from flask import Flask, request, jsonify
from your_ml_module import run_object_detection  # Import your object detection function from your ML module

app = Flask(__name__)

@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    # Run your object detection code here
    result = run_object_detection()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
