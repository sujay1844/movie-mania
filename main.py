from tkinter import Tk, Toplevel, Button, Label, StringVar, Entry, Frame
from matrix import create_button_matrix
from movie import Show, create_show
from submit import submit

root=Tk()
root.title('MOVIE MANIA')
root.state('zoomed')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

page1=Frame(root)
page2=Frame(root)
page3=Frame(root)
page4=Frame(root)

for frame in (page1 , page2 , page3 , page4):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()


show_frame(page1)

#=========page1==========

label_user=Label(page1,text="USERNAME").place(x=40,y=60)
username=StringVar()
username_box=Entry(page1,textvariable=username,font=('Times', 12,'bold'), highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').place(x=110,y=60)
label_pass=Label(page1,text="PASSWORD").place(x=40,y=100)
password=StringVar()
password_box=Entry(page1,textvariable=password,show='*', highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').place(x=110,y=100)

login_button=Button(page1,text="Login",command=lambda: show_frame(page2), font =('calibri', 10, 'bold'),bd='5').place(x=40,y=130)
cancel_button=Button(page1,text="Cancel",command=root.destroy, font =('calibri', 10, 'bold'),bd='5').place(x=90,y=130)


#=========page2============

pag2_label = Label(page2,text="WELCOME TO MOVIE MANIA", font=('Arial', 30, 'bold'))
pag2_label.place(x=50,y=100)

pag2_nxt_button=Button(page2, text="NEXT", font=('Arial' ,15, 'bold') , command=lambda: show_frame(page3))
pag2_nxt_button.place(x=200,y=400)

pag2_bk_button=Button(page2, text="BACK", font=('Arial' ,15, 'bold') , command=lambda: show_frame(page1))
pag2_bk_button.place(x=200,y=600)

#========page3============

pag3_label = Label(page3,text="SEAT LAYOUT", font=('Arial', 30, 'bold'))
pag3_label.grid(row=0,columnspan=5)


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

create_button_matrix(page3, show)

def seat_layout():
    submit_button = Button(
        root,
        text="Submit",
        command=lambda: submit(show, username.get()),
        font=('calibri', 10, 'bold'),
        bd='5'
    )
    submit_button.grid(column=5, row=0)

seat_layout(page4)   

root.mainloop()
