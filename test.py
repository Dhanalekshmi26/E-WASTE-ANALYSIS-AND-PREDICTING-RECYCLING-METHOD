import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json

# Load trained model
model = tf.keras.models.load_model("ewaste_mobilenetv2.h5")

# Load class labels
with open("class_labels.json", "r") as f:
    class_labels = json.load(f)

print(f"✅ Model Ready! Detectable Items: {class_labels}")

# Function to predict an image
def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Resize to match model input size
    img_array = image.img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)  # Get class index
    confidence = np.max(predictions)  # Confidence score

    # Get actual class name
    class_name = class_labels[predicted_class]

    print(f"\n🖼️ Image: {image_path}")
    print(f"🔍 Predicted: {class_name} (Confidence: {confidence:.2f})")

# Test on an image (replace with actual test image path)
predict_image("test_images/download (10).jpg")
