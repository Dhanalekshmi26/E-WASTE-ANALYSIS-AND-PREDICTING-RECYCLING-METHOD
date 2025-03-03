import os
import json
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Define paths dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_class_path = os.path.join(BASE_DIR, "class_labels.json")
json_recycle_path = os.path.join(BASE_DIR, "recycling_info.json")
model_path = os.path.join(BASE_DIR, "ewaste_mobilenetv2.h5")

# Load JSON files
with open(json_class_path, "r", encoding="utf-8") as file:
    class_labels = json.load(file)

with open(json_recycle_path, "r", encoding="utf-8") as file:
    recycling_info = json.load(file)

# Load trained CNN model
model = load_model(model_path)

def load_and_preprocess_image(image_path):
    """ Load and preprocess image for model prediction """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return None
    image = cv2.resize(image, (224, 224))
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def detect_device(image_path):
    """ Detect the electronic device from image """
    image = load_and_preprocess_image(image_path)
    if image is None:
        return None
    predictions = model.predict(image)
    class_idx = np.argmax(predictions)

    # Convert index to string to match JSON keys
    class_idx_str = str(class_idx)

    if class_idx_str not in class_labels:
        print("Error: Predicted class index out of range!")
        return None

    detected_device = class_labels[class_idx_str]
    return detected_device

def process_image(image_path):
    """ Process image to detect the device and fetch recycling details """
    detected_device = detect_device(image_path)
    if detected_device is None:
        print("No device detected.")
        return
    
    print(f"✅ Detected Device: {detected_device}")

    # Fetch recycling info
    if detected_device in recycling_info:
        internal_components = recycling_info[detected_device].get("internal_components", [])
        recycling_methods = recycling_info[detected_device].get("recycling_methods", {})

        print("\n🔍 Internal Components:")
        for component in internal_components:
            print(f"- {component}: {recycling_methods.get(component, ' No recycling method available')}")
    else:
        print(" No data available for this device.")

if __name__ == "__main__":
    test_images_folder = os.path.join(BASE_DIR, "test_images")
    
    if not os.path.exists(test_images_folder):
        print("'test_images/' folder not found!")
    else:
        test_images = [f for f in os.listdir(test_images_folder) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

        if not test_images:
            print("No test images found in 'test_images/' folder!")
        else:
            for img in test_images:
                image_path = os.path.join(test_images_folder, img)
                print(f"\n Processing image: {image_path}")
                process_image(image_path)
