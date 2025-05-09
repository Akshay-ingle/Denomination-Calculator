from tkinter import *
root=Tk()
root.geometry('400x300')
root.title('main')

def topwin():
    top=Toplevel()
    top.geometry('180x100')
    top.title('toplevel')
    12=Label(top,text='this is toplevel window')
    12.pack()

    top.mainloop()
1=Label(root,text='this is root window')
btn=Button(root,text='click here to open new window',command=topwin)

1.pack()
btn.pack()