import os

def rename_files(folder_path, prefix="file", start=1):
    # Get all files in the folder
    files = os.listdir(folder_path)
    files.sort()  # Optional: sort to rename in order
    
    for i, filename in enumerate(files, start=start):
        old_path = os.path.join(folder_path, filename)
        
        # Skip directories
        if os.path.isdir(old_path):
            continue
        
        # Get file extension
        ext = os.path.splitext(filename)[1]
        
        # New name
        new_name = f"{prefix}{i}{ext}"
        new_path = os.path.join(folder_path, new_name)
        
        # Rename
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

# Example usage:
rename_files(r"C:\Users\adith\Documents\train_data\Dataset\cropfarmlands\labels",prefix="cfl_",start=1)