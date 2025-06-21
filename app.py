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
    ap.add_argument("-o", "--output", type=str, default="file",
                    help="output destination: file or console")
    ap.add_argument("-s", "--suppress", type=bool, default=False,
                    help="suppress the display of image files after OCR operation")
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
    elif args["output"] == "blur":
        gray = cv2.medianBlur(gray, 3)
    return gray

def write_grayscale():
    # Write the grayscale image to disk as a temporary file so we can apply OCR to it
    _filename = "{}.png".format(os.getpid())
    cv2.imwrite(_filename, gray_scale)
    return _filename

def output_text(_filename):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = "OCR operation has not been performed"
    try:
        text = pytesseract.image_to_string(Image.open(_filename))
    except pytesseract.pytesseract.TesseractNotFoundError:
        print("PyTesseract has not been found. The executable may not have been installed")
    except:
        print("An error occurred in pytesseract.image_to_string")
    finally:
        print("Finally after pytesseract.image_to_string")

    # Write text to file or console
    if args["output"] == 'file':
        try:
            with open("{}.txt".format(os.getpid()), "a") as f:
                f.write(text)
        except:
            print("An error occurred writing output file")
        finally:
            print("Finally after writing outfile to disk")
    elif args['output'] == 'console':
        print(text)
    else:
        print("Unsupported output option selected:", str(args["output"]))

    # Remove intermediate text file
    try:
        os.remove(_filename)
    except:
        print("An error occurred in removing", str(_filename))
    finally:
        print("Finally after removing", str(_filename))

def show_output_images(_image, _gray):
    if args["suppress"] == False:
        cv2.imshow("Image", _image)
        cv2.imshow("Output", _gray)
    # print("Press any key to exit. ")
    # NG in PyCharm Terminal
    # cv2.waitKey(0)

if __name__ == "__main__":
    print("Hello", "World", sep=", ", end="!\n")
    args = fetch_arguments()
    print("Image:", args["image"])
    print("Preprocess:", args["preprocess"])
    target_image = load_image()
    gray_scale = set_grayscale()
    filename = write_grayscale()
    output_text(filename)
    show_output_images(target_image, gray_scale)