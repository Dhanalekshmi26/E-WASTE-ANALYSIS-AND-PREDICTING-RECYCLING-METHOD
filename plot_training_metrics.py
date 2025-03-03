import matplotlib.pyplot as plt

# Manually extracted values from your training logs
epochs = list(range(1, 11))  # Adjust according to how many epochs were completed

# Training and validation accuracy
train_acc = [0.4621, 0.6437, 0.7011, 0.7160, 0.7405, 0.7468, 0.7638, 0.7720, 0.7786, 0.7894]
val_acc = [0.7070, 0.8010, 0.8551, 0.8471, 0.8615, 0.8615, 0.8599, 0.8758, 0.9029, 0.8997]

# Training and validation loss
train_loss = [1.8287, 1.1298, 0.9720, 0.9249, 0.8513, 0.8136, 0.7474, 0.7411, 0.7026, 0.6796]
val_loss = [0.9260, 0.6501, 0.5035, 0.5305, 0.4538, 0.4297, 0.4593, 0.4107, 0.3674, 0.3692]

# Plot Accuracy
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(epochs, train_acc, 'bo-', label='Training Accuracy')
plt.plot(epochs, val_acc, 'r^-', label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

# Plot Loss
plt.subplot(1, 2, 2)
plt.plot(epochs, train_loss, 'bo-', label='Training Loss')
plt.plot(epochs, val_loss, 'r^-', label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()

plt.tight_layout()
plt.show()
