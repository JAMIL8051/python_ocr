import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog


def get_file_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select PDF File",
                                           filetypes=[("PDF files", "*.pdf")])

    if file_path:
        return file_path
    else:
        return None
    
    
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text_content = ""

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content += page.extract_text()

            print(f"PDF '{file_path}' loaded successfully.")
            return text_content

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
android_file_path = get_file_path()

if android_file_path:
    print("Selected file path:", android_file_path)
else:
    print("No file selected.")
# Replace this file path with the location of your PDF file on your computer
#android_file_path = '/storage/emulated/0/Documents/Pydroid3/1000 Commonly Misspelled Words Upper Level.pdf'

extracted_text = extract_text_from_pdf(android_file_path)
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