# Merge Images to PDF (Python)

A Python project for merging multiple images into a single PDF file. This tool is designed to simplify the process of consolidating images into a single, compact file format.

---

## 🚀 Features
- Merge multiple images (JPEG, PNG, etc.) into a single PDF.
- Supports basic image resizing to fit within the PDF pages.
- Easy-to-use modular structure.

## ⚙️ Requirements

- Python 3.8+
- Install dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

## 🔧 Installation

To use this project, follow these steps:

1. **Clone the Repository**
    
    Clone this repository to your local machine:  
    
    ```bash
    git clone https://github.com/marwan-ahmed-23/Merge-Images-to-PDF-python.git
    cd Merge-Images-to-PDF-python
    ```

2. **Create a Virtual Environment (Optional)**

    It is recommended to use a virtual environment for Python projects:
    
   ```bash
    python -m venv venv
    source venv/bin/activate        # On macOS/Linux
    venv\Scripts\activate           # On Windows
   ```

3. **Install Dependencies**

    Install the required Python libraries using pip:
    
   ```bash
    pip install -r requirements.txt
   ```

4. **Run Examples**

    Test the functionality by running the example script:
    
   ```bash
    python examples/example.py
   ```


>### Notes:
> Ensure the file `requirements.txt` contains the dependencies: `fpdf` `pillow`

## Example

```bash
from src.merge_images_to_pdf import merge_images_to_pdf

images = ["image1.jpg", "image2.png", "image3.jpeg"]
output_path = "output.pdf"

merge_images_to_pdf(images, output_path)
print(f"PDF saved at {output_path}")
```

## 📂 Directory Structure
```plaintext
Merge-Images-to-PDF-python/
├── examples/
│   └── example.py
├── src/
│   └── merge_images_to_pdf.py
├── LICENSE
├── README.md
└── .gitignore
```

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to enhance functionality or add features.

## 🌟 Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub. Your support means the world to us!
