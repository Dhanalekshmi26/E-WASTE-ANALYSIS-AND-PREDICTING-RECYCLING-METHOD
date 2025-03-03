import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load the trained model
model = tf.keras.models.load_model("ewaste_mobilenetv2.h5")

# Define test dataset directory
test_dir = "dataset/DATASET/modified-dataset/test"  # Change this to your actual test data folder

# Load test dataset
test_datagen = ImageDataGenerator(rescale=1.0/255)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),  # Change this if your model uses a different input size
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Get class labels
class_labels = list(test_generator.class_indices.keys())

# Predict on test data
y_pred_prob = model.predict(test_generator)
y_pred = np.argmax(y_pred_prob, axis=1)  # Convert probabilities to class indices
y_true = test_generator.classes  # True labels

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Plot confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()


# Print classification report
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=class_labels))
