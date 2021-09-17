import os
import sys

import cv2

def read_image(image_path, show = True):
    # complete the function
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
    