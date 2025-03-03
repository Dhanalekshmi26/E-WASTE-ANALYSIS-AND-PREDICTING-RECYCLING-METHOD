import os
import json

# Set your dataset path (update this to match your training folder)
dataset_path = "dataset/DATASET/modified-dataset/train"  # Example: "dataset/train"

# Extract class names from dataset folders
class_labels = sorted(os.listdir(dataset_path))  # Sort ensures labels match training order

# Save labels for future use
with open("class_labels.json", "w") as f:
    json.dump(class_labels, f)

print("\n✅ **Extracted Class Labels:**")
print(f"Contents: {class_labels}")
