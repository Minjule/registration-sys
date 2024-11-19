import os
import shutil
from sklearn.model_selection import train_test_split

dataset_path = "C:\\Users\\Acer\\Desktop\\academy\\ocular desease recognition\\archive\\datasets"
output_path = "C:\\Users\\Acer\\Desktop\\academy\\ocular desease recognition\\splitted"

train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

os.makedirs(output_path, exist_ok=True)

split_dirs = ["train", "val", "test"]
for split_dir in split_dirs:
    os.makedirs(os.path.join(output_path, split_dir), exist_ok=True)

for class_name in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_name)
    if not os.path.isdir(class_path): 
        continue

    images = os.listdir(class_path)

    train_images, temp_images = train_test_split(images, test_size=(1 - train_ratio), random_state=42)
    val_images, test_images = train_test_split(temp_images, test_size=(test_ratio / (val_ratio + test_ratio)), random_state=42)

    for split, split_images in zip(split_dirs, [train_images, val_images, test_images]):
        split_class_dir = os.path.join(output_path, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)
        for image in split_images:
            src_path = os.path.join(class_path, image)
            dst_path = os.path.join(split_class_dir, image)
            shutil.copy(src_path, dst_path)

print("Dataset split completed!")

