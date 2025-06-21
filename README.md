# Terzo OCR

18 JUN 2025

## Summary

### Dependencies

Python 3.13
Pillow-11.2.1
argparse
os

### Installing PyTesseract

1. Install tesseract using the Windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
    a. Under "Choose Components", choose additional languages
    b. For example, "Math / equation detection module"
3. Take note of the tesseract path from the installation. For example: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.
3. Run "pip install pytesseract" in the virtual environment
4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

(https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)