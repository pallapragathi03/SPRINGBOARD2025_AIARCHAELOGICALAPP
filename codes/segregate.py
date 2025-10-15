import os
import shutil

# Paths (update to your setup)
images_folder = r"C:\Users\adith\Documents\train_data\heritage_sites\images"
labels_folder = r"C:\Users\adith\Documents\train_data\heritage_sites\labelslabels"
extras_folder = r"C:\Users\adith\Documents\train_data\heritage_sites\extras"

# Create extras subfolders
extras_images = os.path.join(extras_folder, "images")
extras_labels = os.path.join(extras_folder, "labels")
os.makedirs(extras_images, exist_ok=True)
os.makedirs(extras_labels, exist_ok=True)

# Collect all files
image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
label_files = [f for f in os.listdir(labels_folder) if f.lower().endswith('.txt')]

# Get basenames without extension
image_basenames = {os.path.splitext(f)[0] for f in image_files}
label_basenames = {os.path.splitext(f)[0] for f in label_files}

# Find matches and extras
matching = image_basenames & label_basenames
extra_images = image_basenames - label_basenames
extra_labels = label_basenames - image_basenames

# Move extra images
for f in image_files:
    name, ext = os.path.splitext(f)
    if name in extra_images:
        shutil.move(os.path.join(images_folder, f), os.path.join(extras_images, f))

# Move extra labels
for f in label_files:
    name, ext = os.path.splitext(f)
    if name in extra_labels:
        shutil.move(os.path.join(labels_folder, f), os.path.join(extras_labels, f))

print(f"✅ Kept {len(matching)} image-label pairs.")
print(f"📂 Moved {len(extra_images)} extra images to {extras_images}")
print(f"📂 Moved {len(extra_labels)} extra labels to {extras_labels}")