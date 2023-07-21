from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def open_image(file_path):
    try:
        img = Image.open(file_path)
        return img
    except Exception as e:
        print("Error: Unable to open image.")
        return None

def apply_filter(img, filter_type):
    try:
        # Convert the filter_type string to the corresponding ImageFilter class
        filter_class = getattr(ImageFilter, filter_type.upper())
