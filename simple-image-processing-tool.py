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
        filtered_img = img.filter(filter_class)
        return filtered_img
    except AttributeError:
        print(f"Error: Invalid filter type '{filter_type}'.")
    except Exception as e:
        print("Error: Unable to apply filter.")
        print(str(e))  # Print the actual error message for debugging purposes
    return None

def resize_image(img, width, height):
    try:
        resized_img = img.resize((width, height))
        return resized_img
    except Exception as e:
        print("Error: Unable to resize image.")
        return None

def edit_image(img, text, position, color="black"):
    try:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text(position, text, fill=color, font=font)
        return img
    except Exception as e:
