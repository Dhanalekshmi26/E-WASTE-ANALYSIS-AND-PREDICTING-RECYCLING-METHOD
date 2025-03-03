# E-Waste Analysis and Recycling Method Predictor

## 📌 Project Overview
This project is a Flask web app that helps identify electronic waste and suggests recycling methods. It uses a pretrained AI model (MobileNetV2) to recognize electronic devices in images and provides information about their internal parts and how to recycle them.

## 🚀 Features
- Detects electronic devices in uploaded images.
- Shows internal components of detected devices.
- Suggests proper recycling methods based on stored data.
- Easy-to-use web app where users upload images for analysis.

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


