# Graduation Project: YOLO-based Action Detection and Annotation System

## 📋 Overview

This graduation project implements a machine learning pipeline for action detection using YOLO (You Only Look Once) models. The project includes:
- XML to YOLO format annotation conversion
- Action detection model training and evaluation
- Model testing and inference capabilities
- Comprehensive data processing utilities

## 🎯 Project Objectives

- Convert XML-formatted annotations to YOLO format for efficient model training
- Train YOLO11 models for action/pose detection
- Evaluate model performance and generate results
- Provide tools for inference and validation

## 📁 Directory Structure

```
Graduation-Project/
├── xml_to_yolo.py              # Convert XML annotations to YOLO format
├── train_action.py             # Action detection model training script
├── testt.py                    # Testing and inference script
├── final.yaml                  # YOLO model configuration file
├── results.csv                 # Training results and metrics
├── results.png                 # Visualization of results
├── train_batch0.jpg            # Training batch visualization
├── train_v2.txt                # Training log file
├── best.pt                     # Best trained model weights
├── last.pt                     # Last checkpoint weights
├── yolo11n.pt                  # YOLO11 nano pre-trained weights
├── yolo11n-pose.pt            # YOLO11 nano pose detection pre-trained weights
└── README.md                   # This file
```

## 🔄 Workflow

### Step 1: Data Preparation & Annotation Conversion

**File:** `xml_to_yolo.py`

This script converts XML annotation files (typically from annotation tools like LabelImg) to YOLO format.

**Key Features:**
- Reads XML files with bounding box and class information
- Converts absolute coordinates to normalized YOLO format
- Handles missing image size information by reading from image files
- Supports custom class mapping through configuration

**Usage:**
```bash
python xml_to_yolo.py
```

**YOLO Format:**
```
<class_id> <x_center> <y_center> <width> <height>
```
Where all coordinates are normalized (0-1 range)

### Step 2: Model Training

**File:** `train_action.py`

Trains action detection models using YOLO11 architecture.

**Configuration:** `final.yaml`

**Usage:**
```bash
python train_action.py
```

**Output:**
- `best.pt` - Best performing model weights
- `last.pt` - Last checkpoint weights
- `results.csv` - Training metrics and performance data
- `train_batch0.jpg` - Visualization of training batches

### Step 3: Model Testing & Inference

**File:** `testt.py`

Tests trained models and performs inference on new images.

**Usage:**
```bash
python testt.py
```

## 📊 Model Architecture

This project uses:
- **YOLO11 Nano (yolo11n)** - General object detection
- **YOLO11 Nano Pose (yolo11n-pose)** - Pose and action detection

### Model Specifications
- Input: RGB images
- Output: Bounding boxes with class predictions and confidence scores
- Framework: PyTorch (`.pt` format)

## 📈 Results & Performance

- **Results:** See `results.csv` for detailed metrics
- **Visualization:** `results.png` shows performance graphs
- **Training Progress:** Documented in `train_v2.txt`

## ✅ Requirements

### Python Version
- Python 3.8+

### Key Dependencies
```
torch>=2.0.0
torchvision>=0.15.0
ultralytics>=8.0.0  # YOLO implementation
opencv-python>=4.8.0
numpy>=1.23.0
pandas>=1.5.0
Pillow>=9.0.0
```

## ���� Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/ggjj-hub/Graduation-Project.git
cd Graduation-Project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare Your Data
```bash
# Place XML annotations in annotations/ directory
# Place images in images/ directory
```

### 4. Convert Annotations
```bash
python xml_to_yolo.py
```

### 5. Train Model
```bash
python train_action.py
```

### 6. Test & Evaluate
```bash
python testt.py
```

## 📝 Configuration

Edit `final.yaml` to customize:
- Model architecture
- Training parameters (epochs, batch size, learning rate)
- Data paths
- Augmentation settings
- Validation configuration

Example configuration structure:
```yaml
path: /path/to/dataset
train: images/train
val: images/val
test: images/test

nc: 4  # number of classes
names: ['action1', 'action2', 'action3', 'action4']  # class names
```

## 🔍 Understanding the Code

### `xml_to_yolo.py`
- Parses XML annotation files
- Extracts bounding box coordinates and class information
- Normalizes coordinates to YOLO format
- Handles edge cases (missing sizes, empty annotations)

### `train_action.py`
- Initializes YOLO model
- Loads training configuration
- Implements training loop
- Logs metrics and saves checkpoints

### `testt.py`
- Loads trained model weights
- Runs inference on test images
- Visualizes predictions
- Generates performance metrics

## 📊 Output Files Explanation

- **best.pt**: Best model weights during training (use for inference)
- **last.pt**: Final model checkpoint
- **results.csv**: Detailed training metrics (loss, accuracy, mAP, etc.)
- **results.png**: Training curves and performance visualization
- **train_batch0.jpg**: Sample training batch with annotations
- **train_v2.txt**: Detailed training log

## ⚠️ Important Notes

- Ensure XML files contain `Action` attribute and `bndbox` information
- Image files and XML files must have the same base name (different extensions)
- If XML files lack `size` tags, the script reads dimensions from image files
- Adjust `class_mapping` in `xml_to_yolo.py` to match your annotation attributes
- Ensure sufficient GPU memory for training (recommended: ≥8GB)

## 🛠️ Troubleshooting

### Common Issues

**1. Class mapping mismatch**
- Solution: Update `class_mapping` dictionary in `xml_to_yolo.py`

**2. Image not found errors**
- Solution: Verify image paths in XML match actual files

**3. Out of memory during training**
- Solution: Reduce batch size in `final.yaml` or use gradient accumulation

**4. Model not converging**
- Solution: Adjust learning rate or increase training epochs in `final.yaml`

## 📚 References

- [YOLO Documentation](https://docs.ultralytics.com/)
- [PyTorch Documentation](https://pytorch.org/)
- [Object Detection Basics](https://en.wikipedia.org/wiki/Object_detection)

## 👨‍💻 Project Author

- **Repository**: ggjj-hub/Graduation-Project
- **Repository ID**: 1173290289
- **Language**: 100% Python

## 📄 License

Please add appropriate license information here.

## 📞 Support & Contribution

For issues, questions, or contributions:
1. Open an issue on GitHub
2. Submit pull requests with improvements
3. Share feedback and suggestions

---

**Last Updated**: March 5, 2026
**Language Composition**: Python (100%)
```
