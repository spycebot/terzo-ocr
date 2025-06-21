#! python3

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os



def fetch_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                    help="type of preprocessing to be done: thresh or blur")
    return vars(ap.parse_args())

def load_image():
    # Load the example image and convert it to grayscale
    return cv2.imread(args["image"])

def set_grayscale():
    # Convert loaded image to grayscale
    gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    # Check to see if we should apply thresholding to preprocess the image
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif args["preprocess"] == "blur":
        gray = cv2.medianBlur(gray, 3)
    return gray

def write_grayscale():
    # Write the grayscale image to disk as a temporary file so we can apply OCR to it
    _filename = "{}.png".format(os.getpid())
    cv2.imwrite(_filename, gray_scale)
    return _filename

def output_text(_filename):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(_filename))
    '''try:
    except:
        print("An error occurred in pytesseract.image_to_string")
    finally:
        print("Finally for pytesseract.image_to_string")'''

    try:
        print(text)
        os.remove(_filename)
    except:
        print("An error occurred in removing", str(_filename))
    finally:
        print("That is all she wrote.")

def show_output_images():
    # cv.imshow("Image", image)
    pass

if __name__ == "__main__":
    print("Hello", "World", sep=", ", end="!\n")
    args = fetch_arguments()
    print("Image:", args["image"])
    print("Preprocess:", args["preprocess"])
    target_image = load_image()
    gray_scale = set_grayscale()
    filename = write_grayscale()
    output_text(filename)
    show_output_images()