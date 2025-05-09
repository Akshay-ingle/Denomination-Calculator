from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root=Tk()
root.title('denomination counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload=Image.open('app_img.jpg')

upload=upload.resize((300,300))
image=ImageTk.PhotoImage