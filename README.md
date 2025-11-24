# TASK 7 

# Image Resizer Tool
A Python-based batch image resizer and converter for automating image processing tasks. This tool utilizes Pillow and the os module for reading, resizing, and exporting images from a designated folder.

# Features
Resize multiple images in bulk by specifying custom width and height.

Automatically reads all images from the input folder.

Supports popular image formats (JPEG, PNG, etc., as provided).

Saves resized images to a chosen output directory.

Handles input errors and defaults gracefully to common dimensions.

# Folder Structure
image-resizer/ (Main project folder)

resizer.py (Main script)

requirements.txt (Package dependencies)

input/ (Place all source images here)

output/ (Resized images are saved here)

# Setup Instructions
Clone or download the repository to your local machine.

Install dependencies by running:
pip install -r requirements.txt
or directly install Pillow:
pip install Pillow

. Add your images to the input folder.

Usage Guide
Run the script using:
python resizer.py

Enter desired width (px) and height (px) when prompted.

If you provide an invalid input, the tool will default to 800x600 pixels.

The script processes all images found in the input folder.

Progress and status messages will be displayed in the terminal.

When finished, check the output folder for your resized images.
