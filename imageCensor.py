# Image Censor Application

# Assignment 1 - Image Enhancement in Spatial Domain
# 1. Blacken part of the image
# 2. Darken part of the image
# 3. Brighten pat of the image

import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


class ImageCensor:
    def __init__(self,root):
        self.root = root
        self.menu()

    #---GUI---#
    def menu(self):
        #---Setup---#
        self.root.title("Image Censor Application")
        self.root.iconbitmap("assets/photo-editor.ico")
        self.root.resizable(False, False)
        self.root.geometry("430x600+100+100")
        #---End Of Setup---#

        #---Title Frame---#
        self.title_frame = LabelFrame(self.root)
        self.title_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.title_lbl = Label(self.title_frame, text="Image Censor Application", font=("Arial", 24), bg="#fff", width=20)
        self.title_lbl.pack()
        #---End Of Title Frame---#

        #---Tool Frame---#
        self.tool_frame = LabelFrame(self.root)
        self.tool_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky=W)

        #Open an image
        self.empty_lbl = Label(self.tool_frame, text=" ").grid(row=1, column=0, pady=2)
        self.img_lbl = Label(self.tool_frame, text="1. Choose An Image To Censor:", font=("Arial", 16))
        self.img_lbl.grid(row=2, column=0, columnspan=2, padx=20, sticky=W)
        self.img_button = Button(self.tool_frame, text='Open File...', command=self.open, bg="#808080", fg="#fff", font=("Arial", 12), width=15)
        self.img_button.grid(row=3, column=0, columnspan=2, padx=20, ipadx=5, ipady=5, sticky=W)

        #Censor type
        self.empty_lbl = Label(self.tool_frame, text=" ").grid(row=4, column=0, pady=2)
        self.type_lbl = Label(self.tool_frame, text="2. Choose Type Of Censor:", font=("Arial", 16))
        self.type_lbl.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky=W)
        self.blacken_button = Button(self.tool_frame, text='Blacken Effects', command=self.blacken, bg="#808080", fg="#fff", font=("Arial", 12), width=15)
        self.blacken_button.grid(row=6, column=0, padx=20, ipadx=5, ipady=5, sticky=W)
        self.darken_button = Button(self.tool_frame, text='Darken Effects', command=self.darken, bg="#808080", fg="#fff", font=("Arial", 12), width=15)
        self.darken_button.grid(row=7, column=0, padx=20, pady=5, ipadx=5, ipady=5, sticky=W)
        self.lighten_button = Button(self.tool_frame, text='Lighten Effects', command=self.lighten, bg="#808080", fg="#fff", font=("Arial", 12), width=15)
        self.lighten_button.grid(row=7, column=1, pady=5, ipadx=5, ipady=5, sticky=W)
        self.type_lbl = Label(self.tool_frame, text="Lighten/Darken (%) :", font=("Arial", 12))
        self.type_lbl.grid(row=8, column=0, padx=20, sticky=SW)
        self.slide = Scale(self.tool_frame, from_=0, to=100, orient=HORIZONTAL, length=150)
        self.slide.grid(row=8, column=1, ipadx=5, sticky=SW)
        self.slide.set(50)

        #Select ROI
        self.empty_lbl = Label(self.tool_frame, text=" ").grid(row=9, column=0, pady=2)
        self.type_lbl = Label(self.tool_frame, text="3. Select a Region Of Interest (ROI)", font=("Arial", 16))
        self.type_lbl.grid(row=10, column=0, columnspan=2, padx=20, pady=5, sticky=W)
        self.type_lbl = Label(self.tool_frame, text="      - Apply by pressing SPACE or ENTER button", font=("Arial", 12))
        self.type_lbl.grid(row=11, column=0, columnspan=2, padx=20, sticky=W)
        self.type_lbl = Label(self.tool_frame, text="      - Cancel by pressing C button", font=("Arial", 12))
        self.type_lbl.grid(row=12, column=0, columnspan=2, padx=20, sticky=W)

        #Action buttons
        self.save_button = Button(self.tool_frame, text='Save As...', command=self.save, bg="#808080", fg="#fff", font=("Arial", 12), width=15)
        self.save_button.grid(row=19, column=0, padx=20, pady=20, ipadx=5, ipady=5, sticky=W)
        self.clear_button = Button(self.tool_frame, text='Reset To Original', command=self.clear, bg="#808080", fg="#fff", font=("Arial", 12), width=15)
        self.clear_button.grid(row=19, column=1, pady=20, ipadx=5, ipady=5, sticky=W)
        #---End Of Tool Frame---#
    #---End Of GUI---#

    #---Functions---#
    # raw_img    : the uploaded original image
    # img        : the image to apply changes
    # temp_img   : temporary image
    # copy_img   : copy of raw image

    def open(self):
        self.filename = filedialog.askopenfilename(
            initialdir = "./img",
            title = "Choose An Image",
            filetypes=(
                ("JPG files", "*.jpg"), 
                ("PNG files", "*.png"),
                ("TIF files", "*.tif"), 
                ("All files", "*.*")
            )
        )
        self.raw_img = cv.imread(self.filename)
        self.copy_img = self.raw_img.copy()
        self.img = self.raw_img
        cv.destroyAllWindows()
        cv.imshow('Image', self.img)
        cv.moveWindow("Image", 550, 250)

    def blacken(self):
        cv.destroyAllWindows()
        (x,y,z) = self.img.shape
        self.rectangle = 255*np.ones((x,y,z), dtype="uint8")
        self.roi = cv.selectROI(self.img)
        self.rectangle[int(self.roi[1]):int(self.roi[1]+self.roi[3]), 
                       int(self.roi[0]):int(self.roi[0]+self.roi[2])] = 0
        self.temp_img = cv.bitwise_and(self.rectangle, self.img)
        self.img = self.temp_img
        cv.destroyAllWindows()
        cv.imshow("Image", self.img)
        cv.moveWindow("Image", 550, 250)

    def darken(self):
        cv.destroyAllWindows()
        (x,y,z) = self.img.shape
        self.rectangle = 255*np.ones((x,y,z), dtype="uint8")
        self.roi = cv.selectROI(self.img)
        self.rectangle[int(self.roi[1]):int(self.roi[1]+self.roi[3]), 
                       int(self.roi[0]):int(self.roi[0]+self.roi[2])] = 0
        
        #subtraction truncate arithmetic
        for i in range(0,x):
            for j in range(0,y):
                for k in range(0,z):
                    if self.rectangle[i,j,k] != 255: #ignore not ROI
                        total = self.img[i,j,k] - (self.slide.get() / 100 * 255) #percentage = x/100 *255
                        if (total < 0):
                            self.img[i,j,k]= 0
                        else:
                            self.img[i,j,k] = total

        cv.destroyAllWindows()
        cv.imshow("Image", self.img)
        cv.moveWindow("Image", 550, 250)

    def lighten(self):
        cv.destroyAllWindows()
        (x,y,z) = self.img.shape
        self.rectangle = 255*np.ones((x,y,z), dtype="uint8")
        self.roi = cv.selectROI(self.img)
        self.rectangle[int(self.roi[1]):int(self.roi[1]+self.roi[3]), 
                       int(self.roi[0]):int(self.roi[0]+self.roi[2])] = 0
        
        #addition truncate arithmetic
        for i in range(0,x):
            for j in range(0,y):
                for k in range(0,z):
                    if self.rectangle[i,j,k] != 255: #ignore not ROI
                        total = self.img[i,j,k] + (self.slide.get() / 100 * 255) #percentage = x/100 *255
                        if (total > 255):
                            self.img[i,j,k] = 255
                        else:
                            self.img[i,j,k] = total

        cv.destroyAllWindows()
        cv.imshow("Image", self.img)
        cv.moveWindow("Image", 550, 250)

    def save(self):
        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type

        save_as_image = self.img
        cv.imwrite(filename, save_as_image)
        self.filename = filename

    def clear(self):
        self.img = self.copy_img
        cv.destroyAllWindows()
        cv.imshow("Image", self.img)
        cv.moveWindow("Image", 550, 250)
    #---End Of Functions---#

#---End Of Class---#

mainWindow = Tk()
ImageCensor(mainWindow)
mainWindow.mainloop()