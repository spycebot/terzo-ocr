# Terzo OCR

18 JUN 2025

## Summary

Terzo OCR is a simple implementation of PyTesseract that has proven itself useful for several years. 
The current implementation is run from the command line; a TkInter or wxPython GUI may follow in the future.
If successful, Terzo OCR will save the text captured from an image file to a text file on disk by default, 
or output the text to the console if you set the --output flag to "console".
The default preprocessing method is threshold, but can be set to blur if you set the --preprocess flag to "blur".

### Dependencies

- Python 3.13
- Pillow-11.2.1
- PyTeserract 0.3.13
- argparse
- os

### Installing PyTesseract

1. Install tesseract using the Windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

    a. Under "Choose Components", choose additional languages

    b. For example, "Math / equation detection module"
 
2. Take note of the tesseract path from the installation. For example: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. Run "pip install pytesseract" in the virtual environment

4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

(https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)