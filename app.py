from flask import Flask, render_template, request, jsonify, url_for
import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'  # Store images here
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load class labels
with open('class_labels.json', 'r') as f:
    CLASS_LABELS = json.load(f)

# Load recycling information
with open('recycling_info.json', 'r') as f:
    RECYCLING_DATA = json.load(f)

# Load CNN model
MODEL_PATH = 'ewaste_mobilenetv2.h5'  # Update with the correct path
model = load_model(MODEL_PATH)

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # 🔍 Run CNN model for actual detection
        detected_label = detect_device(filepath)

        # Fetch recycling info safely
        device_info = RECYCLING_DATA.get(detected_label, {})
        internal_components = device_info.get("internal_components", [])
        recycling_methods = device_info.get("recycling_methods", {})

        return jsonify({
            'filename': filename,
            'detected_device': detected_label,
            'internal_components': internal_components,
            'recycling_methods': recycling_methods,
            'image_url': url_for('static', filename=f'uploads/{filename}')
        })

def detect_device(image_path):
    """
    Process the image and run it through the CNN model to detect the device.
    """
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust size as per model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize
    
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])  # Get class with highest probability
    
    # Map index to class label
    detected_label = CLASS_LABELS.get(str(predicted_class_index), "Unknown Device")
    return detected_label

if __name__ == '__main__':
    app.run(debug=True)
