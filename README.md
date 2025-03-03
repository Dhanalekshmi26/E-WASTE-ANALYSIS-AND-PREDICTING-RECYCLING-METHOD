# E-Waste Analysis and Recycling Method Predictor

## 📌 Project Overview
This project is a Flask web app that helps identify electronic waste and suggests recycling methods. It uses a pretrained AI model (MobileNetV2) to recognize electronic devices in images and provides information about their internal parts and how to recycle them.

## 🚀 Features
- Detects electronic devices in uploaded images.
- Shows internal components of detected devices.
- Suggests proper recycling methods based on stored data.
- Easy-to-use web app where users upload images for analysis.

## Methodology
1. Data Collection

Dataset Source: The dataset consists of images of various electronic devices and their internal components collected from Kaggle and other sources.
Categories: The dataset includes images of electronic waste items such as laptops, keyboards, microwaves, mobile phones, and internal components like resistors, capacitors, and PCBs.
Data Organization: The collected images are stored in structured folders categorized by device type.

2. Data Preprocessing

Image Resizing: All images are resized to a uniform size (e.g., 224x224 or 256x256 pixels) to ensure compatibility with the CNN model.
Normalization: Pixel values are normalized between 0 and 1 to improve model performance.
Data Augmentation: Augmentations such as rotation, flipping, and brightness adjustments are applied to increase dataset variability.

3. Model Selection & Training

Pretrained CNN Model: A pretrained model like MobileNetV2  is used for feature extraction and classification.
Fine-Tuning: The final layers of the model are modified to classify e-waste categories and predict internal components.
Training Process:
Loss Function: Cross-entropy loss is used for classification.
Optimizer: Adam or SGD is used to optimize learning.
Evaluation Metrics: Accuracy, precision, recall, and F1-score are calculated to assess model performance.
Training Environment: The model is trained using TensorFlow/Keras or PyTorch on a GPU-enabled system.

4. Model Evaluation
   
The trained model is evaluated using a test dataset.
A confusion matrix is generated to analyze misclassifications.
The model's performance is fine-tuned by adjusting hyperparameters if necessary.

5. Flask Web Application

User Input: Users can upload an image from the test_images folder.
Detection System:
The CNN model classifies the uploaded image as an electronic device.
The system fetches the corresponding internal components and recycling methods from recycling_info.json.
Output Display:
The detected device, its internal components, and their recommended recycling methods are displayed in the UI.
The system provides technical recycling terms such as "Pyrometallurgical Processing" for PCBs.

6. JSON-Based Recycling Information Storage
   
Data Storage: A JSON file (e_waste_recycling.json) stores mappings between detected devices, their internal components, and recycling methods.
API Endpoint: A Flask API endpoint (/recycling-info?device=<device_name>) returns internal components and recycling methods for a detected device.

7. Deployment & Future Enhancements

Deployment: The system is deployed on a local Flask server.
Future Enhancements:
Expansion of the dataset to include more internal components.
Integration with real-time object detection models.
Implementation of a mobile-friendly UI for broader accessibility.


## 🛠️ Technologies Used
- Python (Programming Language)
- Flask (For the web application)
- MobileNetV2 (AI model for detecting devices)
- JSON (For storing recycling information)
- VS Code (For coding and development)

## 📂 Project Structure
```
E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/
│-- static/
│   ├── data/
│   │   ├── e_waste_recycling.json  # Stores device and recycling details
│-- test_images/  # Sample images for testing
│-- templates/
│   ├── index.html  # Web app interface
│-- model/
│   ├── mobilenetv2_model.h5  # AI model file
│-- app.py  # Main program to run the web app
│-- requirements.txt  # List of necessary software packages
│-- README.md  # Project details
```

## 🔧 How to Use
1. Download the project
   ```sh
   git clone https://github.com/Dhanalekshmi26/E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD.git
   cd E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD
   ```
2. Set up Python environment (optional)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. Install required software
   ```sh
   pip install -r requirements.txt
   ```
4. Run the web app
   ```sh
   python app.py
   ```
5. Open the web app
   - Go to: `http://127.0.0.1:5000/` in your browser.
   - Upload an image of an electronic device.
   - See its components and recycling methods.

## 🔍 How It Works
1. User uploads an image of an electronic device through the web app.
2. MobileNetV2 model processes the image and detects the electronic device.
3. The system fetches internal components of the detected device from `e_waste_recycling.json`.
4. Recycling methods are displayed, explaining how to properly recycle each component.


## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---


