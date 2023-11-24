import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract


# Get Tesseract executable path from user
def get_tesseract_executable_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select EXE File",
                                           filetypes=[("EXE files", "*.exe")])

    if file_path:
        return file_path
    else:
        return None


def get_file_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select JPG File",
                                           filetypes=[("JPG files", "*.jpg")])

    if file_path:
        return file_path
    else:
        return None

# Replace this path with your Tesseract executable path\
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = get_tesseract_executable_path()

android_file_path = get_file_path()

if android_file_path.lower().endswith('.jpg'):
    text = pytesseract.image_to_string(Image.open(android_file_path))
    print(text)
    extracted_text = text
else:
    print("Please provide a valid JPG file path.")
    
if extracted_text is not None:
    if isinstance(extracted_text, str):
        # Get the directory path and filename without extension
        output_directory = os.path.dirname(android_file_path)
        filename_without_extension = os.path.splitext(os.path.basename(android_file_path))[0]

        # Create the output file path with a specific filename for the text file
        output_file_path = os.path.join(output_directory, f"{filename_without_extension}_extracted.txt")
        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)
        print(f"Text extracted successfully and saved to '{output_file_path}'.")
    else:
        print("Extraction failed. No text content to save.")
else:
    print("Extraction failed. No text content extracted.")
