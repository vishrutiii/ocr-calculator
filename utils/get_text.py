import os
import sys
import math
import time
import pytesseract
import PIL
from PIL import Image
from read_image import read_image
import numpy as np


def get_text(filename : str = ""):
    """
    It will take the input filename, and extract the input the maths text from it.
    """
    # image = read_image(filename)
    img = Image.open(filename)
    print(pytesseract.image_to_string(img))
    return img

path = "A:\Pending Projects\OCR Calculator\ocr-calculator\Images\/abc.png"
get_text(path)