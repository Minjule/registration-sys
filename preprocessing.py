import os
from glob import glob
import cv2
from PIL import Image

import cv2
import numpy as np

def resize_with_padding(image, target_size):
    old_size = image.shape[:2]
    ratio = min(target_size[0] / old_size[0], target_size[1] / old_size[1])
    new_size = tuple([int(x * ratio) for x in old_size])

    resized_image = cv2.resize(image, (new_size[1], new_size[0]), interpolation=cv2.INTER_AREA)

    delta_w = target_size[1] - new_size[1]
    delta_h = target_size[0] - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    padded_image = cv2.copyMakeBorder(resized_image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    return padded_image


def resizing(input_dir, output_dir, target_size=(224, 224), image_extensions=(".jpg", ".png")):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.lower().endswith(image_extensions):
            try:
                filepath = os.path.join(input_dir, file)
                image = cv2.imread(filepath)
                resized_image = resize_with_padding(image, target_size)
                cv2.imwrite(os.path.join(output_dir, os.path.basename(filepath)), resized_image)
            except Exception as e:
                print(f"Error processing file {file}: {e}")


if __name__ == "__main__":
    directory = "C:\\Users\\Acer\\Documents\\GitHub\\registration-sys\\junk" 
    resizing(directory, directory)