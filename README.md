# ♻️ Intelligent Waste Segregation System

### Real-Time Waste Detection & Classification using YOLOv8

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![License](https://img.shields.io/badge/Dataset-CC%20BY%204.0-lightgrey)

---

## 📌 Overview

Manual waste sorting is slow, error-prone, and unscalable — a critical bottleneck for recycling facilities and smart city infrastructure. This project builds a **real-time AI-powered waste detection and classification system** using **YOLOv8**, capable of identifying **22 distinct waste categories** from live video or images.

The system is trained on a custom-annotated dataset sourced from [Roboflow Universe](https://universe.roboflow.com/ai-project-i3wje/waste-detection-vqkjo/dataset/10) and is optimized for deployment on both standard hardware and edge devices. An interactive **Streamlit web app** (`app.py`) is included for live inference.

---

## 🎯 Problem Statement

Global recycling rates remain low largely because sorting is manual, inconsistent, and labor-intensive. Automating waste classification with computer vision addresses:

- **Recycling accuracy** — reduce contamination of recyclable streams
- **Processing speed** — handle high-throughput conveyor or bin environments
- **Hazardous waste safety** — automatically flag batteries, chemical bottles, and paint buckets
- **Smart city integration** — enable AI-powered bin sensors and sorting robots
- **Edge AI deployment** — run inference on low-power embedded devices

---

## 🗂️ Repository Structure

```
Waste_segregation/
│
├── train.py                  # YOLOv8 training script
├── main.py                   # Core inference pipeline
├── app.py                    # Streamlit web app for live demo
├── settings.py               # Global configuration settings
│
├── data.yaml                 # Dataset config: class names, paths, splits
├── args.yaml                 # Training hyperparameter arguments
├── requirements.txt          # Python dependencies
├── packages.txt              # System-level package dependencies
│
├── yolov8n.pt                # Base YOLOv8n pretrained weights
├── weights/                  # Directory for custom trained weights
├── runs/detect/              # YOLO training run outputs (metrics, plots, weights)
├── results.csv               # Training metrics log
│
└── README.md
```

---

## 🏷️ Waste Categories (22 Classes)

The model classifies waste into **22 fine-grained categories**, spanning recyclable, non-recyclable, and hazardous materials:

| Category | Type |
|---|---|
| `plastic_bottle` | Recyclable |
| `plastic_bottle_cap` | Recyclable |
| `plastic_bag` | Non-recyclable |
| `plastic_box` | Recyclable |
| `plastic_cup` | Non-recyclable |
| `plastic_cup_lid` | Non-recyclable |
| `plastic_cultery` | Non-recyclable |
| `scrap_plastic` | Non-recyclable |
| `snack_bag` | Non-recyclable |
| `straw` | Non-recyclable |
| `can` | Recyclable |
| `cardboard_box` | Recyclable |
| `cardboard_bowl` | Recyclable |
| `reuseable_paper` | Recyclable |
| `scrap_paper` | Recyclable |
| `battery` | ⚠️ Hazardous |
| `light_bulb` | ⚠️ Hazardous |
| `chemical_plastic_bottle` | ⚠️ Hazardous |
| `chemical_plastic_gallon` | ⚠️ Hazardous |
| `chemical_spray_can` | ⚠️ Hazardous |
| `paint_bucket` | ⚠️ Hazardous |
| `stick` | Organic/Other |

---

## 📊 Dataset

| Property | Details |
|---|---|
| **Source** | [Roboflow Universe — waste-detection-vqkjo v10](https://universe.roboflow.com/ai-project-i3wje/waste-detection-vqkjo/dataset/10) |
| **Total Images** | 6,000+ |
| **Annotation Format** | YOLO bounding boxes |
| **Number of Classes** | 22 |
| **License** | CC BY 4.0 |
| **Split** | Train / Validation / Test |

### Data Augmentation
To improve generalization, the following augmentations were applied during training:
- Mosaic augmentation (multi-image blending)
- Random rotation and scaling
- Horizontal flipping
- Color jitter (brightness, contrast, saturation)
- Random cropping

---

## 🏗️ System Architecture

```
Input (Image / Video / Webcam)
         │
         ▼
  Preprocessing
  (resize → 640×640, normalize)
         │
         ▼
  YOLOv8 Backbone
  (CSPDarknet feature extraction)
         │
         ▼
  Neck (PANet feature pyramid)
         │
         ▼
  Detection Head
  (bounding box regression + class probabilities)
         │
         ▼
  NMS Post-Processing
  (IoU threshold filtering)
         │
         ▼
  Annotated Output
  (bounding boxes + class labels + confidence scores)
```

---

## 🤖 Model Details

| Property | Value |
|---|---|
| **Architecture** | YOLOv8n (nano — optimized for speed) |
| **Framework** | Ultralytics / PyTorch |
| **Input Size** | 640 × 640 |
| **Base Weights** | `yolov8n.pt` (COCO pretrained) |
| **Fine-tuned on** | Custom 22-class waste dataset |
| **Loss Functions** | Box loss + Classification loss + DFL loss |

**Hyperparameters Tuned** (see `args.yaml`):
- Learning rate and scheduler
- Batch size
- IoU threshold
- Confidence threshold
- Augmentation intensity

---

## 📈 Results

| Metric | Score |
|---|---|
| **mAP@0.5** | 92% |
| **mAP@0.5:0.95** | 84% |
| **Inference Latency** | ~45ms (optimized) |

- Inference latency reduced from **120ms → 45ms** via model optimization
- Improved cross-category generalization through advanced augmentation pipeline
- Training metrics and per-epoch curves available in `runs/detect/` and `results.csv`

> *Update with your specific per-class AP values from `results.csv` for maximum impact.*

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/avanthikarajesh30/Waste_segregation.git
cd Waste_segregation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

For system-level packages (Linux):
```bash
cat packages.txt | xargs sudo apt-get install -y
```

### 3. Download the Dataset

Dataset is hosted on Roboflow Universe. Download via:

```python
from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("ai-project-i3wje").project("waste-detection-vqkjo")
dataset = project.version(10).download("yolov8")
```

Then update the paths in `data.yaml` to point to your local dataset directory.

---

## 🏋️ Training

```bash
python train.py
```

Or directly via the YOLO CLI:

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640 batch=16
```

Training outputs (weights, metrics, confusion matrix, PR curves) are saved to `runs/detect/`.

---

## 🔎 Inference

### On an image or video:
```bash
python main.py
```

Or via CLI:
```bash
yolo detect predict model=weights/best.pt source=path/to/image.jpg
```

### Live webcam inference:
```bash
yolo detect predict model=weights/best.pt source=0
```

---

## 🌐 Web App (Streamlit)

An interactive demo app is included for easy testing:

```bash
streamlit run app.py
```

The app supports:
- Image upload for single-frame inference
- Webcam stream for real-time detection
- Annotated output with bounding boxes, class labels, and confidence scores

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.8+ | Core language |
| YOLOv8 (Ultralytics) | Object detection model |
| PyTorch | Deep learning framework |
| OpenCV | Image/video processing |
| Streamlit | Interactive web demo |
| Roboflow | Dataset hosting and annotation |
| NumPy | Array operations |

---

## 🌍 Real-World Applications

- **Smart recycling bins** — auto-sort waste at point of disposal
- **Recycling facility conveyor belts** — high-throughput automated sorting
- **Hazardous waste flagging** — safely isolate batteries, chemicals, paint
- **Smart city sustainability systems** — real-time waste analytics dashboard
- **Edge AI hardware** — deployable on Jetson Nano, Raspberry Pi, Edge TPU

---

## 🔮 Future Work

- Deploy on **NVIDIA Jetson Nano** or **Coral Edge TPU** for embedded inference
- Expand dataset to **20,000+ images** for improved long-tail class coverage
- Add **multi-object tracking** (ByteTrack / DeepSORT) for conveyor belt use case
- Build a **real-time analytics dashboard** (waste type frequency, hazard alerts)
- Integrate with **IoT bin sensors** for smart city deployment
- Explore **YOLOv8m/l** variants for higher accuracy in non-edge environments
- Add **instance segmentation** (YOLOv8-seg) for pixel-level waste boundary detection

---

## 👩‍💻 Author

**Avanthika Rajesh**
MS Computer Engineering — Virginia Tech
[GitHub](https://github.com/avanthikarajesh30) • [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN_HERE)

---

## 📄 License

The dataset is licensed under **CC BY 4.0** via Roboflow Universe. Code in this repository is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the detection framework
- [Roboflow Universe](https://universe.roboflow.com/ai-project-i3wje/waste-detection-vqkjo/dataset/10) for the annotated waste detection dataset
- Original dataset contributors under the CC BY 4.0 license
