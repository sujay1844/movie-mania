from PIL import ImageTk , Image
from tkinter import CENTER, Tk, Button, Label, StringVar, Entry, Frame
from matrix import create_button_matrix
from movie import Show
from submit import submit

root=Tk()
root.title('MOVIE MANIA')
# root.state('zoomed')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

page1=Frame(root)
page2=Frame(root)
page3=Frame(root)
page4=Frame(root)

for frame in (page1 , page2 , page3, page4):
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
pag3_label = Label(page3,text="SEAT LAYOUT", font=('Arial', 30, 'bold'))
pag3_label.place(anchor=CENTER, relx=.5, rely=.1)
def seat_layout(show:Show, frame:Frame):
    submit_button = Button(
        frame,
        text="Submit",
        command=lambda: submit(show, username.get(), page4),
        font=('calibri', 10, 'bold'),
        bd='5'
    )
    submit_button.grid(row=1, column=1)
    details = Frame(frame, padx=100)

    text = f"""
    Name: {show.name}
    Director: {show.director}
    IMDb Rating: {show.imdb_rating}
    Time: {show.timing}
    Screen No: {show.screen_no}
    """

    lbl = Label(details,text=text, font=('calibri', 20, 'normal'))
    lbl.grid(row=0, column=0)
    details.grid(row=0, column=0, rowspan=2)


def book_now(show:Show):
    sub_frame = create_button_matrix(page3, show)
    seat_layout(show, sub_frame)   
    show_frame(page3)

page2.configure(bg='#333333')
pag2_label = Label(page2,text="SELECT YOUR MOVIE", bg='#333333', fg="#FF3399", font=("Cooper Black", 35)).place(x=500,y=100)

show_avatar = Show(
    name='Avatar',
    director='James Cameron',
    imdb_rating=7.8,
    timing='11:00PM',
    screen_no=4,
    no_of_rows=5,
    no_of_columns=5,
    file_name='avatar.json'
)
avatar_img=ImageTk.PhotoImage(Image.open("avatar1.png"))
avatar_lbl=Label(page2,image=avatar_img)
avatar_lbl.place(x=50,y=200)
avatar_book_btn=Button(page2,text="Book Now",command=lambda: book_now(show_avatar), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=100,y=550)

show_pathaan = Show(
    name='Pathaan',
    director='Siddarth Anand',
    imdb_rating=7.5,
    timing='4:00PM',
    screen_no=3,
    no_of_rows=6,
    no_of_columns=5,
    file_name='pathaan.json'
)
pathaan_img=ImageTk.PhotoImage(Image.open("pathaan1.png"))
pathaan_lbl=Label(page2,image=pathaan_img)
pathaan_lbl.place(x=450,y=200)
pathaan_book_btn=Button(page2,text="Book Now",command=lambda: book_now(show_pathaan), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=500,y=550)

show_varisu = Show(
    name='Varisu',
    director='Vamshi Paidipally',
    imdb_rating=6.8,
    timing='7:00PM',
    screen_no=4,
    no_of_rows=5,
    no_of_columns=7,
    file_name='varisu.json'
)
varisu_img=ImageTk.PhotoImage(Image.open("varisu1.png"))
varisu_lbl=Label(page2,image=varisu_img)
varisu_lbl.place(x=850,y=200)
varisu_book_btn=Button(page2,text="Book Now",command=lambda: book_now(show_varisu), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=900,y=550)

show_kantara = Show(
    name='Kantara',
    director='Rishab Shetty',
    imdb_rating=8.4,
    timing='1:00PM',
    screen_no=1,
    no_of_rows=4,
    no_of_columns=6,
    file_name='kantara.json'
)
kantara_img=ImageTk.PhotoImage(Image.open("kantara1.png"))
kantara_lbl=Label(page2,image=kantara_img)
kantara_lbl.place(x=1250,y=200)
kantara_book_btn=Button(page2,text="Book Now",command=lambda: book_now(show_kantara), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=1300,y=550)

next_button=Image.open("nextbtn.png")
resize_next_button=next_button.resize((50,50))
next_btn=ImageTk.PhotoImage(resize_next_button)
pag2_nxt_button=Button(page2,text='Next', command=lambda: show_frame(page3) , bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=1400,y=50)

back_button=Image.open("backbtn.png")
resize_back_button=back_button.resize((50,50))
back_btn=ImageTk.PhotoImage(resize_back_button)
pag2_bk_button=Button(page2,text='back', command=lambda: show_frame(page3), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=50,y=50)



#========page3============


next_button1=Image.open("nextbtn.png")
resize_next_button1=next_button1.resize((50,50))
next_btn1=ImageTk.PhotoImage(resize_next_button1)
pag2_nxt_button1=Button(page3,text='Next', command=lambda: show_frame(page4), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=1400,y=50)

back_button1=Image.open("backbtn.png")
resize_back_button1=back_button1.resize((50,50))
back_btn1=ImageTk.PhotoImage(resize_back_button1)
pag2_bk_button1=Button(page3,text='Back', command=lambda: show_frame(page4),bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').place(x=50,y=50)

#==========page4===========

page4.configure(bg='#333333')
pag4_label = Label(page4,text='Hey Sri', bg='#333333', fg="#FF3399", font=("Arial Black", 35)).place(x=50,y=100)
thanku_label = Label(page4,text='Thank you for booking , Here are your details', bg='#333333', fg="#FF3399", font=("Arial Black", 25)).place(x=400,y=200)

pg4_label1=Label(page4,text='Name : Sri', bg='#333333', fg="#FF3399", font=("Arial Black", 20)).place(x=450,y=300)


root.mainloop()
