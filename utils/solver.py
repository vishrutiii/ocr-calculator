import os
import sys
import time
import math
from cv2 import TermCriteria_COUNT
import pandas as pd
import numpy as np

filepath = "A:\\Pending Projects\\OCR Calculator\\ocr-calculator\\Data\\fun.txt"

df = pd.read_table(filepath, sep=", ")
input_fun = np.array(df['Input'])
output_fun = np.array(df['Output'])


def output(input_text : str = ""):
    """
    It will take input as a string and return the output of the given input mathematics problem
    """
    if input_text in input_fun:
        return output_fun[np.where(input_fun == input_text)]
    
    else :
        raise ValueError("Required Input Function Not Found")
