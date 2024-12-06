import os
from src.merge_images_to_pdf import MergeImagesToPdf

# List of image paths to merge
image_paths = [
    "example1.jpg",  # Replace with the full path to the first image
    "example2.png",  # Replace with the full path to the second image
    "example3.jpeg"  # Replace with the full path to the third image
]

# Output path for the resulting PDF file
output_pdf_path = "output/merged_images.pdf" 

# Ensure the output directory exists, create it if it doesn't
os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

# Create the merger object and merge the images into a PDF
merger = MergeImagesToPdf(image_paths, output_pdf_path)
merger.merge_images()
