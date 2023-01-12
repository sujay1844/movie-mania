from tkinter import *
import json

root=Tk()
top=Toplevel()
top.title('LOGIN')
root.title('MOVIE MANIA SEAT LAYOUT')


with open ('matrix.json') as file:
    matrix=json.load(file)
       

label_user=Label(top,text="USERNAME").place(x=40,y=60)
username=StringVar()
username_box=Entry(top,textvariable=username,font=('Times', 12,'bold'), highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').place(x=110,y=60)
label_pass=Label(top,text="PASSWORD").place(x=40,y=100)
password=StringVar()
password_box=Entry(top,textvariable=password,show='*', highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').place(x=110,y=100)

login_button=Button(top,text="Login",command=lambda:command1(), font =('calibri', 10, 'bold'),bd='5').place(x=40,y=130)
cancel_button=Button(top,text="Cancel",command=lambda:command2(), font =('calibri', 10, 'bold'),bd='5').place(x=90,y=130)

def command1():
    root.deiconify()
    top.destroy()

def command2():
    top.destroy()
    root.destroy()
    
username1=StringVar()
username1_box=Entry(root,textvariable=username1,font=('Times', 12,'bold'), highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7')
username1_box.grid(columnspan=5)

booked_seats = []
def create_button(row, column):
    btn = Button(root, text=chr(row+65)+str(column),font =('calibri', 10, 'bold'),bd='5')
    btn.configure(padx=10, pady=10)

    if matrix[str(row)][column]:
        btn.configure(bg='red')

    btn.configure(command=lambda button=btn: book(button))
    btn.grid(column=column, row=row+1)
    return btn

def book(button):
    for row in matrix:
        for column in range(len(matrix[row])):
            if button == buttons[int(row)][column]:
                booked_seats.append((row, column))
                matrix[row][column] = 1
    button.config(bg='green')

    
buttons = []
for _ in range(len(matrix)):
    buttons.append([])
for row in matrix:
    for column in range(len(matrix[row])):
        buttons[int(row)].append(create_button(int(row), int(column)))

def submit():
    with open('matrix.json', 'w') as file:
        file.write(json.dumps(matrix, indent=4))
    
    print(username.get(), "booked the following seats")
    print(booked_seats)

submit_button = Button(root, text="Submit", command=submit,font =('calibri', 10, 'bold'),bd='5')
submit_button.grid(column=5, row=0)

root.mainloop()
