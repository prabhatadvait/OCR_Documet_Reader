# OCR_Document_Reader 📝

## 📖 Overview

The **OCR_Document_Reader** project utilizes Python to extract text from images, enabling the conversion of printed or handwritten documents into machine-readable text. This system leverages advanced Optical Character Recognition (OCR) libraries and tools to efficiently process image data, recognizing and translating characters with high accuracy.

## ⚡ Features

- 🧑‍💻 Extract text from both printed and handwritten documents
- 📷 Support for multiple image formats (JPEG, PNG, TIFF, etc.)
- 🔧 Easy-to-use interface for image-to-text conversion
- 🛠️ Integration with advanced OCR tools like Tesseract
- 🎯 High accuracy in text recognition

## 🧰 Technologies Used

- **Python**: Programming language for the core functionality
- **Tesseract OCR**: Open-source OCR engine for text extraction
- **Pillow**: Python Imaging Library (PIL) for image processing
- **OpenCV**: Library for advanced image manipulation and pre-processing
- **Numpy**: Library for numerical operations in image processing

## 🚀 Installation

To install and set up the project locally, follow these steps:

1. 🔗 Clone the repository:
    ```bash
    git clone https://github.com/prabhatadvait/OCR_Document_Reader.git
    ```

2. 🔽 Navigate into the project directory:
    ```bash
    cd OCR_Document_Reader
    ```

3. 🧑‍💻 Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. 📦 Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. 🔨 Install Tesseract (if not already installed):
    - [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)

## 🏁 Usage

1. 🖼️ Place your image file(s) in the `images/` directory.
2. ▶️ Run the OCR script:
    ```bash
    python ocr_reader.py
    ```

3. 📝 The extracted text will be printed to the console, and can also be saved to a text file.

### Example

```bash
$ python ocr_reader.py
Extracted Text: This is an example of a scanned document.
