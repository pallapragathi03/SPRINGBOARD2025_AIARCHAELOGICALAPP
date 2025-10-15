import os
from PIL import Image

def convert_images_to_jpg(input_folder):
    # Output folder
    output_folder = os.path.join(input_folder, "JPG_IMAGES")
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Open image
        try:
            with Image.open(file_path) as img:
                # Convert to RGB (in case of PNG with alpha channel)
                img = img.convert("RGB")

                # Get file name without extension
                base_name = os.path.splitext(filename)[0]

                # New file path with .jpg extension
                new_file_path = os.path.join(output_folder, base_name + ".jpg")

                # Save as JPG
                img.save(new_file_path, "JPEG")
                print(f"Converted: {filename} → {base_name}.jpg")
        except Exception as e:
            print(f"Skipping {filename} (Error: {e})")

    print(f"\n✅ All images converted! Saved in: {output_folder}")


# Example usage
input_folder = r"C:\Users\adith\Documents\Satelite Data\New folder\images"  # Change this path
convert_images_to_jpg(input_folder)