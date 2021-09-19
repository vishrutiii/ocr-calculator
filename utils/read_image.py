import os
import sys

import cv2
import PIL
from PIL import Image
import numpy as np
def read_image(image_path, show = True, module : str = "" ):
    # complete the function
    if module == "opencv":
        image = cv2.imread(image_path)
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image
        except : 
            return image
        finally :
            if show:
                cv2.imshow("Image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        image = Image.open(image_path)
        if show:
            image.show()
        return np.array(image)