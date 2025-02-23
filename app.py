from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import torch
import os
from PIL import Image
import io

app = Flask(__name__)

# Load the YOLO model using CPU
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', device='cpu')  # Force CPU usage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    # Get the image from the request
    file = request.files['image'].read()
    img = Image.open(io.BytesIO(file))

    # Perform detection
    results = model(img)

    # Extract detections
    detections = results.pandas().xyxy[0]  # Get results as a DataFrame
    detected_objects = detections[['name', 'confidence']].to_dict(orient='records')  # Convert to list of dicts

    return jsonify(detected_objects)

if __name__ == '__main__':
    app.run(debug=True)
