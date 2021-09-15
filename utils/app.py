# import necessary files
import os
import sys
import time

import PIL
import cv2
import datetime
import tkinter.messagebox as msgs

from tkinter import *
from typing import Sized
from tkinter.filedialog import askopenfilename

from PIL import ImageTk
from time import time
from datetime import datetime


import warnings
warnings.filterwarnings('ignore')

# path where all images will be stored
path_of_image = "A:\Pending Projects\OCR Calculator\ocr-calculator\Images"
class App:
    def __init__(self, root, title, video_source = 0):
        self.i = 1
        self.root = root # init the root
        self.root.title(title) # get the title of the window
        self.root.geometry("600x800") # define the dimesions of the window
        self.root.minsize(600,800) # config the min dimesnions of the window
        self.root.maxsize(600,800) # config the max dimesions of the window
        self.canvas_width = 400 # width of the canvas window
        self.canvas_height = 300 # height of the canvas window
        self.video_source = video_source # select which video source, web cam, or any other camera source
        self.cameraOpen = False
        self.image_ = None

        # display the title of the program in the window
        self.title_window = Label(text = "OCR Calculator", font = "comicsansms 20 bold")
        self.title_window.pack(fill = Y,padx = 20, pady = 20)

        #create a canvas where we can display our images
        self.tkinter_canvas = Canvas(self.root, width = self.canvas_width, height = self.canvas_height, bg="white")
        self.tkinter_canvas.pack()

        # creating a frame where we will display our buttons, for functionality
        self.frame = Frame(self.root) # init the frame, it is like the div in html, where we will defining our button
        self.frame.pack(side=TOP)

        self.select_button = Button(self.frame, borderwidth=7, bg="black", fg="white", text="Select From Computer", font="comicsansms 13", command=self.openImage) # created a select button which will select the image from our local machine
        self.select_button.pack(side=LEFT,anchor='ne', pady=20, padx=35)

        self.snapshot = Button(self.frame, borderwidth=7, bg="black", fg="white", text="SnapShot", font="comicsansms 13", command=self.takeSnap) # snapshot is the button that is used to capture the images from the web camera
        self.snapshot.pack(side = BOTTOM, anchor='ne', padx=35)

        self.webcam_button = Button(self.frame, borderwidth=7, bg="black", fg="white", text="Open WebCam", font="comicsansms 13", command=self.openCamera) # webcam button is used to open the web camera of the local machine
        self.webcam_button.pack(side=LEFT,anchor='ne', pady=20,padx=35)

        # now we will initialize our output button which will show the output of our given input image
        self.output_frame = Frame(self.root)
        self.output_frame.pack()

        # output button that will pop up a message box with input and output
        self.output_button = Button(self.output_frame, borderwidth=7, bg="black", fg="white", text="GET OUTPUT", font="comicsansms 13", pady=20, padx=20, command=self.showOutput)
        self.output_button.pack(fill = X, pady = 60)

        # make the delay var, to refresh the page
        self.delay = 10

        # init the main loop of the program, to run the program
        self.root.mainloop()
        
    # funtion to open the image
    def openImage(self):
        # to refresh the page, to avoid overlapping
        if self.cameraOpen:
            self.closeCamera()
        
        global file
        file = askopenfilename(defaultextension=".png", filetypes=[("All Files", "."), ("PNG Image","*.png")])
        if file == "":
            file = None
        else:
            title = os.path.basename(file) + "- OCR-Calculator"
            root.title(title)
            img_ = PIL.Image.open(file)
            img_ = img_.resize((self.canvas_width, self.canvas_height))
            img = ImageTk.PhotoImage(image = img_)
            image_ = Label(image=img)
            self.image_ = image_
            self.image_.image = img
            self.image_.place(x=97,y=78)

    # show output function it will show the output of the given input
    def showOutput(self):
        try:
            msgs.showinfo("Output", "The Input : {} and The Output is : {}".format(1,2))
        except:
            msgs.showwarning("Error", "The program can't be executed.")

    def openCamera(self):
        if self.image_ is not None:
            self.image_.config(image=None)
            self.image_.image = None

        if self.cameraOpen:
            self.closeCamera()

        
        video = cv2.VideoCapture(self.video_source)
        self.cameraOpen = True
        self.video = video
        def show_frame():
            ret, frame = video.read()
            cv2image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(cv2image)
            img = img.resize((self.canvas_width, self.canvas_height))
            imgtk = ImageTk.PhotoImage(image = img)
            v = Label(image=imgtk)
            v.image = imgtk
            v.place(x=97,y=78)
            v.after(self.delay, show_frame)

        show_frame()

    def closeCamera(self):
        self.video.release()
        cv2.destroyAllWindows()

    # function to take snapshot of the image
    def takeSnap(self):
        ret, frame_ = get_frame(self.video)
        if ret:
            curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            filename = path_of_image + "\image_{}.jpg".format(str(curr_datetime))
            a = cv2.imwrite(filename,frame_)
            cv2.imshow("maths_",frame_)
            print("File saved ")
            
            

def get_frame(video):
    if video.isOpened():
        ret, frame = video.read()
        if ret:
            return (ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        else:
            return (ret, None)
    else:
        return (False, None)



if __name__ == "__main__":
    root = Tk() # init the root 
    title = "OCR-Calculator" # title of the porgram
    App(root, title) # run the app