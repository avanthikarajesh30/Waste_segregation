

♻️ Intelligent Waste Segregation System (YOLOv8)

Real-time object detection system for automated waste classification using YOLOv8 and custom-trained computer vision models.

⸻

📌 Overview

This project implements a real-time waste segregation system using YOLOv8 for object detection. The model classifies waste into multiple categories (e.g., plastic, paper, metal, glass, organic) to support smart recycling and sustainability initiatives.

The system was trained on a hybrid dataset combining TrashNet and custom-labeled images in COCO format and optimized for deployment-ready performance.

⸻

🎯 Problem Statement

Manual waste segregation is inefficient and prone to human error. This project aims to:
	•	Automate waste classification using deep learning
	•	Improve recycling accuracy
	•	Enable edge-deployable real-time inference
	•	Support scalable smart-city sustainability systems

⸻

🏗 System Architecture

Pipeline Overview:
	1.	Dataset Collection (TrashNet + Custom Images)
	2.	Annotation in COCO Format
	3.	Data Augmentation
	4.	YOLOv8 Training
	5.	Model Evaluation (mAP metrics)
	6.	Real-Time Inference Deployment

⸻

📊 Dataset
	•	Total Images: 6,000+
	•	Source: TrashNet + Custom annotated images
	•	Format: COCO bounding box annotations
	•	Classes: 6 waste categories
	•	Split: Train / Validation / Test

Data Augmentation Techniques
	•	Mosaic augmentation
	•	Random rotation
	•	Scaling
	•	Color jitter
	•	Horizontal flipping

⸻

🤖 Model Details
	•	Model: YOLOv8 (Ultralytics)
	•	Framework: PyTorch
	•	Training: Custom hyperparameter tuning
	•	Loss Functions: Box loss, Objectness loss, Classification loss

Hyperparameters Tuned:
	•	Learning rate
	•	Batch size
	•	IoU threshold
	•	Confidence threshold

⸻

📈 Results

Metric	Score
mAP@0.5	92%
mAP@0.5:0.95	84%
Inference Latency	45ms (optimized)

Improvements:
	•	Reduced inference latency from 120ms → 45ms via quantization
	•	Improved generalization with advanced augmentation
	•	Optimized batch processing for edge deployment

⸻

⚙️ Tech Stack
	•	Python
	•	PyTorch
	•	YOLOv8 (Ultralytics)
	•	OpenCV
	•	COCO Dataset Format
	•	Docker (for deployment)

⸻

📁 Project Structure

waste-segregation/
│
├── runs/detect/
├── weights/
├── train.py
├── main.py
├── app.py
├── data.yaml
├── args.yaml
├── settings.py
├── requirements.txt
├── packages.txt
├── results.csv
├── yolov8n.pt
└── README.md


⸻

🚀 Installation

1️⃣ Clone Repository

git clone https://github.com/avanthikarajesh30/<repo-name>.git
cd <repo-name>

2️⃣ Install Dependencies

pip install -r requirements.txt


⸻

🏋️ Training

python train.py

Or using YOLO CLI:

yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640


⸻

🔎 Inference

python main.py

Or:

yolo detect predict model=best.pt source=0

(Use source=0 for webcam)

⸻

📦 Deployment
	•	Model quantized for lower latency
	•	Docker-ready environment
	•	Supports edge-device deployment

⸻

🌍 Applications
	•	Smart bins
	•	Recycling facilities
	•	Industrial waste sorting
	•	Smart city sustainability systems
	•	Edge AI hardware deployment

⸻

🔮 Future Improvements
	•	Deploy on Jetson Nano / Edge TPU
	•	Add real-time dashboard analytics
	•	Integrate IoT-based bin sensors
	•	Expand dataset to 20K+ images
	•	Add multi-object tracking

⸻

👩‍💻 Author

Avanthika Rajesh
MS Computer Engineering – Virginia Tech
AI/ML | Computer Vision | Edge AI | Systems Engineering

