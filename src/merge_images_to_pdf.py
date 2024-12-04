from fpdf import FPDF
from PIL import Image

def merge_images_to_pdf(images, output_path):
    """
    Merge multiple images into a single PDF.

    Args:
        images (list): List of image file paths.
        output_path (str): Path for the output PDF.

    Returns:
        None
    """
    # Create a PDF object
    pdf = FPDF()

    for image_path in images:
        try:
            # Open the image to get its dimensions
            image = Image.open(image_path)
            width, height = image.size

            # Convert pixels to millimeters for FPDF (1 px = 0.264583 mm)
            width_mm = width * 0.264583
            height_mm = height * 0.264583

            # Add a page to the PDF with image dimensions
            pdf.add_page()
            pdf.image(image_path, x=10, y=10, w=190)  # Adjust as needed

        except Exception as e:
            print(f"Error processing {image_path}: {e}")

    # Save the PDF
    try:
        pdf.output(output_path)
        print(f"PDF successfully saved to {output_path}")
    except Exception as e:
        print(f"Failed to save PDF: {e}")
