from src.merge_images_to_pdf import merge_images_to_pdf

# Example images to merge
images = ["example1.jpg", "example2.png", "example3.jpeg"]

# Output PDF path
output_pdf = "merged_output.pdf"

# Merge images into a PDF
merge_images_to_pdf(images, output_pdf)

print(f"PDF successfully created: {output_pdf}")
