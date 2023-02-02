from tkinter import Frame, Label, PhotoImage, Tk

root = Tk()
frame = Frame(root)
img = PhotoImage(file='ticket.png')
img_lbl = Label(frame, image=img, bg='red')
img_lbl.pack()
Label(frame, text='hi', bg='green').pack()
frame.pack()
root.mainloop()
