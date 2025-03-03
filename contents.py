import tensorflow as tf
import json

# Load trained model
model_path = "ewaste_mobilenetv2.h5"  # Make sure the model file is in the same directory
model = tf.keras.models.load_model(model_path)

# Check if class labels were stored separately
class_labels_file = "class_labels.json"  # Update if the filename is different
try:
    with open(class_labels_file, "r") as f:
        class_labels = json.load(f)
except FileNotFoundError:
    print("⚠️ Class labels file not found! Extracting from training process instead...")
    # If labels were not saved separately, try to infer them
    class_labels = [f"Class_{i}" for i in range(model.output_shape[-1])]

# Print detected classes
print("\n🔍 **Contents Available in the Model:**")
print(f"Contents: {class_labels}")  # Print in required format
