from tkinter import *
import json
from seats import Seat, Show

root=Tk()
top=Toplevel()
top.title('LOGIN')
root.title('MOVIE MANIA SEAT LAYOUT')

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

show = Show(
    name = "Avatar",
    director = 'James Cameron',
    imdb_rating = 7.8,
    timing = '11:00PM',
    screen_no = 4,
    no_of_rows = 5,
    no_of_columns = 5,
    file_name = 'avatar.json'
)

def get_matrix(show:Show):
    with open(show.file_name, 'r') as file:
        matrix = json.load(file)
    # matrix = [[0]*show.no_of_columns for _ in range(show.no_of_rows)]
    return matrix
def update_seat_matrix(show:Show):
    matrix = get_matrix(show)
    with open(show.file_name, 'w') as output:
        with open('selected_seats.txt', 'r') as input:
            for seat_str in input.readlines():
                row, column = int(seat_str[0]), int(seat_str[1])
                matrix[row][column] = 1
        json.dump(matrix, output)

matrix = get_matrix(show)
for row in range(show.no_of_rows):
    for column in range(show.no_of_columns):

        seat = Seat(root, row, column, matrix[row][column])
        seat.grid(row=row, column=column)

def submit():
    update_seat_matrix(show)
    
    print(username.get(), "booked the following seats:-")
    with open('selected_seats.txt', 'r') as file:
        print(file.readlines())

    # empty the file for next use
    with open('selected_seats.txt', 'w') as file:
        file.write("")

submit_button = Button(root, text="Submit", command=submit,font =('calibri', 10, 'bold'),bd='5')
submit_button.grid(column=5, row=0)

root.mainloop()
