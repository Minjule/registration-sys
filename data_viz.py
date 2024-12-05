import os
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter

def count_images_in_subfolders(directory, image_extensions=(".jpg", ".jpeg", ".png", ".bmp", ".gif")):
    folder_counts = {}
    for item in os.listdir(directory):
        subfolder_path = os.path.join(directory, item)
        if os.path.isdir(subfolder_path):  # Check if it's a folder
            image_count = sum(1 for file in os.listdir(subfolder_path) if file.lower().endswith(image_extensions)
            )
            folder_counts[item] = image_count
    print(folder_counts)
    return folder_counts

def count_extension_type(directory):
    jpg_count, png_count = 0, 0
    image_modes = {"RGB": 0, "BGR":0, "RGBA":0, "L":0, "CMYK":0}
    dimensions_count = Counter()
    for item in os.listdir(directory):
        subfolder_path = os.path.join(directory, item)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file.lower().endswith(".jpg"):
                    jpg_count += 1
                elif (file.lower().endswith(".png")):
                    png_count += 1
                try:
                    filepath = os.path.join(subfolder_path, file)
                    with Image.open(filepath) as img:
                        dimensions = img.size  # (width, height)
                        image_modes[img.mode] += 1
                        dimensions_count[dimensions] += 1
                except Exception as e:
                    print(f"Error processing file {file}: {e}")
    print(f"Dimension count => {dimensions_count}")
    print(f"Image mode count => {image_modes}")
    return jpg_count, png_count

def visualize_image_counts(folder_counts):
    folders = list(folder_counts.keys())
    counts = list(folder_counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.barh(folders, counts, color='skyblue')
    plt.xlabel('Number of Images')
    plt.ylabel('Folders')
    plt.title('Number of Images in Each Folder')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    directory = "C:\\Users\\Acer\\Desktop\\academy\\data_add2" 
    folder_counts = count_images_in_subfolders(directory)
    count = count_extension_type(directory)
    print(f"jpg count = {count[0]}, png count = {count[1]}")
    visualize_image_counts(folder_counts)
