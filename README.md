# VisionAid: Real-Time Object Detection Web Application

## 🚀 Project Overview
VisionAid is a web-based object detection application that uses YOLOv5 to perform real-time object recognition through your webcam. The application provides instant identification and confidence scores for detected objects.

## 🔧 Technologies Used
- **Backend**: Flask (Python)
- **Object Detection**: YOLOv5 (ultralytics)
- **Frontend**: HTML5, JavaScript
- **Computer Vision**: OpenCV, Torch

## ✨ Features
- Real-time webcam object detection
- Instant object identification
- Confidence score for each detected object
- Simple, intuitive web interface

## 📦 Prerequisites
- Python 3.8+
- Webcam-enabled device

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/VisionAid.git
cd VisionAid
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

## 🖥️ How It Works
1. The application accesses your webcam
2. Captures video frames in real-time
3. Processes each frame using YOLOv5 object detection
4. Displays detected objects with confidence scores

## 🔍 Supported Object Classes
The application can detect a wide range of objects using the YOLOv5n pre-trained model, including:
- People
- Vehicles
- Animals
- Everyday objects
- And many more!

## 📸 Screenshots

<img src="\Images\1.png" width="300" height="150" />

<img src="\Images\2.png" width="300" height="150" />


## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License.

## 🙏 Acknowledgments
- [Ultralytics](https://github.com/ultralytics/yolov5) for YOLOv5
- [Flask](https://flask.palletsprojects.com/) Web Framework