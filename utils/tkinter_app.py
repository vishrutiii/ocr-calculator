from tkinter import *
from typing import Sized
import tkinter.messagebox as msgs
from tkinter.filedialog import askopenfilename
import os
import PIL
from PIL import ImageTk
import cv2

# function to show output
def showOutput():
    msgs.showinfo("Output", "The Input : {} and The Output is : {}".format(1,2)) # complete the function

# function to open image
def openImage():
    global file
    file = askopenfilename(defaultextension=".png", filetypes=[("All Files", "."), ("PNG Image","*.png")])

    if file == "":
        file = None
    else:
        title = os.path.basename(file) + "- OCR-Calculator"
        root.title(title)
        img_ = PIL.Image.open(file)
        img_ = img_.resize((canvas_width, canvas_height))
        img = ImageTk.PhotoImage(image = img_)
        print(type(img_))
        print(img_)
        image_ = Label(image=img)
        image_.image = img
        image_.place(x=97,y=78)



# open the web camera
def openCamera():
    video = cv2.VideoCapture(0)

    def show_frame():
        ret, frame = video.read()
        cv2image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(cv2image)
        img = img.resize((canvas_width, canvas_height))
        imgtk = ImageTk.PhotoImage(image = img)
        v = Label(image=imgtk)
        v.image = imgtk
        v.place(x=97,y=78)
        v.after(10, show_frame)

    show_frame()

    def get_frame():
        if video.isopened():
            ret, frame = video.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            else:
                return (ret, None)
        else:
            return (None, None)


# take the snapshot of that image
def takeSnap():
    pass

root = Tk()
root.geometry("600x800")
root.minsize(600,800)
root.maxsize(600,800)
root.title("OCR-Calculator")

title_window = Label(text = "OCR Calculator", font = "comicsansms 20 bold")
title_window.pack(fill = Y,padx = 20, pady = 20)

canvas_width = 400
canvas_height = 300
tkinter_canvas = Canvas(root, width = canvas_width, height = canvas_height, bg="white")
# tkinter_canvas = Frame(root, width=canvas_width, height=canvas_height)
tkinter_canvas.pack()



webcam_frame = Frame(root)
webcam_frame.pack(side=TOP)
select_button = Button(webcam_frame, borderwidth=7, bg="black", fg="white", text="Select From Computer", font="comicsansms 13", command=openImage)
select_button.pack(side=LEFT,anchor='ne', pady=20, padx=35)
snapshot = Button(webcam_frame, borderwidth=7, bg="black", fg="white", text="SnapShot", font="comicsansms 13", command=takeSnap)
snapshot.pack(side = BOTTOM, anchor='ne', padx=35)

webcam_button = Button(webcam_frame, borderwidth=7, bg="black", fg="white", text="Open WebCam", font="comicsansms 13", command=openCamera)
webcam_button.pack(side=LEFT,anchor='ne', pady=20,padx=35)

input_frame = Frame(root,)
input_frame.pack()
input_text = Button(input_frame, borderwidth=7, bg="black", fg="white", text="GET OUTPUT", font="comicsansms 13", pady=20, padx=20, command=showOutput)
input_text.pack( fill=X ,pady=60)

root.mainloop()