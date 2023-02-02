from tkinter import *
import json
from seats import Seat, Show
from PIL import ImageTk , Image

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
page1.configure(bg='#333333')

welcome_label = Label(page1, text="WELCOME  TO  MOVIE  MANIA", bg='#333333', fg="#FF3399", font=("Cooper Black", 35)).place(x=400,y=100)

label_user=Label(page1,text="USERNAME", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).place(x=600,y=250)
username=StringVar()
username_box=Entry(page1,textvariable=username,font=('Times', 12,'bold'), highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').place(x=750,y=250)
label_pass=Label(page1,text="PASSWORD",bg='#333333', fg="#FFFFFF", font=("Arial", 16)).place(x=600,y=300)
password=StringVar()
password_box=Entry(page1,textvariable=password,show='*', font=('Times', 12,'bold'),highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').place(x=750,y=300)

login_button=Button(page1,text="Login",command=lambda: show_frame(page2), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=650,y=400)
cancel_button=Button(page1,text="Cancel",command=root.destroy,bg="#FF3399", fg="#FFFFFF",font =("Arial", 16),bd='5').place(x=800,y=400)


#=========page2============

page2.configure(bg='#333333')

pag2_label = Label(page2,text="SELECT YOUR MOVIE", bg='#333333', fg="#FF3399", font=("Cooper Black", 35)).place(x=500,y=100)


avatar=ImageTk.PhotoImage( Image.open("avatar1.png"))
avatar_movie=Label(page2,image=avatar)
avatar_movie.place(x=50,y=200)
avatar_book_btn=Button(page2,text="Book Now",command=lambda: show_frame(page3), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=100,y=550)

pathaan=ImageTk.PhotoImage(Image.open("pathaan1.png"))
pathaan_movie=Label(page2,image=pathaan)
pathaan_movie.place(x=450,y=200)
pathaan_book_btn=Button(page2,text="Book Now",command=lambda: show_frame(page3), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=500,y=550)

varisu=ImageTk.PhotoImage(Image.open("varisu1.png"))
varisu_movie=Label(page2,image=varisu)
varisu_movie.place(x=850,y=200)
varisu_book_btn=Button(page2,text="Book Now",command=lambda: show_frame(page3), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=900,y=550)

kantara=ImageTk.PhotoImage(Image.open("kantara1.png"))
kantara_movie=Label(page2,image=kantara)
kantara_movie.place(x=1250,y=200)
kantara_book_btn=Button(page2,text="Book Now",command=lambda: show_frame(page3), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=1300,y=550)

pag2_nxt_button=Button(page2, text="NEXT",  bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5', command=lambda: show_frame(page3)).place(x=1400,y=700)
pag2_bk_button=Button(page2, text="BACK",  bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5', command=lambda: show_frame(page1)).place(x=50,y=700)


#========page3============

pag3_label = Label(page3,text="SEAT LAYOUT", font=('Arial', 30, 'bold'))
pag3_label.grid(row=0,columnspan=5)


show_avatar = Show(
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

def seat_layout():
    for row in range(show.no_of_rows):
        for column in range(show.no_of_columns):

            seat = Seat(page3, row, column, matrix[row][column])
            seat.grid(row=row+1, column=column)

    def submit():
        update_seat_matrix(show)
    
        print(username.get(), "booked the following seats:-")
        with open('selected_seats.txt', 'r') as file:
             print(file.readlines())

         # empty the file for next use
        with open('selected_seats.txt', 'w') as file:
             file.write("")
 
    submit_button = Button(page3, text="Submit", command=submit,font =('calibri', 10, 'bold'),bd='5')
    submit_button.grid(column=5, row=0)

seat_layout()   

root.mainloop()
