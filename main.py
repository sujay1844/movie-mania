from PIL import ImageTk , Image
from tkinter import CENTER, LEFT, NE, NW, RIGHT, Tk, Button, Label, StringVar, Entry, Frame
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
    frame.configure(bg='#333')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

#=========page1==========
page1.configure(bg='#333333')

welcome_label = Label(page1, text="WELCOME  TO  MOVIE  MANIA", bg='#333333', fg="#FF3399", font=("Cooper Black", 35)).place(anchor=CENTER, relx=.5, rely=.1)

username=StringVar()
password=StringVar()

page1_centre_frame = Frame(page1, bg="#333")
page1_centre_frame.place(anchor=CENTER, relx=.5, rely=.5)

label_user=Label(page1_centre_frame,text="Username:", bg='#333', fg="#FFF", font=("Arial", 16), padx=10, pady=10).grid(row=0, column=0)
username_box=Entry(page1_centre_frame,textvariable=username,font=('Times', 12,'bold'), highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').grid(row=0, column=1)
label_pass=Label(page1_centre_frame,text="Password:",bg='#333', fg="#FFF", font=("Arial", 16), padx=10, pady=20).grid(row=1, column=0)
password_box=Entry(page1_centre_frame,textvariable=password,show='*', font=('Times', 12,'bold'),highlightcolor = 'green', highlightbackground='brown', bg='#FFEFE7').grid(row=1, column=1)

login_button=Button(page1_centre_frame,text="Login",command=lambda: show_frame(page2), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').grid(row=2, column=0)
cancel_button=Button(page1_centre_frame,text="Cancel",command=root.destroy,bg="#FF3399", fg="#FFFFFF",font =("Arial", 16),bd='5').grid(row=2, column=1)


#=========page2============
pag3_label = Label(page3,text="SEAT LAYOUT", font=('Cooper Black', 35), bg='#333', fg='#FF3399')
pag3_label.place(anchor=CENTER, relx=.5, rely=.1)
page3_back_button_frame = Frame(page3, padx=15, pady=15, bg='#333')
page3_back_button_frame.pack(anchor=NW, side=LEFT)
pag2_bk_button1=Button(page3_back_button_frame,text='Back', command=lambda: show_frame(page4),bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').pack()
page3_next_button_frame = Frame(page3, padx=15, pady=15, bg='#333')
page3_next_button_frame.pack(anchor=NE, side=RIGHT)
pag3_nxt_button=Button(page3_next_button_frame,text='Next', command=lambda: show_frame(page4), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').pack()

def seat_layout(show:Show, frame:Frame):
    submit_button = Button(
        frame,
        text="Submit",
        command=lambda: submit(show, username.get(), page4),
        font=('calibri', 10, 'bold'),
        bd='5',
        bg='#FF3399',
        fg='#FFF'
    )
    submit_button.grid(row=1, column=1)
    details = Frame(frame, padx=100, bg='#333')

    text = f"""
    Name: {show.name}
    Director: {show.director}
    IMDb Rating: {show.imdb_rating}
    Time: {show.timing}
    Screen No: {show.screen_no}
    """

    lbl = Label(details,text=text, font=('calibri', 20, 'normal'), justify='left', bg='#333', fg='#FFF')
    lbl.grid(row=0, column=0)
    details.grid(row=0, column=0, rowspan=2)


def book_now(show:Show):
    sub_frame = create_button_matrix(page3, show)
    seat_layout(show, sub_frame)   
    show_frame(page3)

page2.configure(bg='#333333')
pag2_label = Label(page2,text="SELECT YOUR MOVIE", bg='#333333', fg="#FF3399", font=("Cooper Black", 35)).place(anchor=CENTER, relx=.5, rely=.1)

page2_centre_frame = Frame(page2, bg='#333')
page2_centre_frame.place(anchor=CENTER, relx=.5, rely=.5)
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
avatar_frame = Frame(page2_centre_frame, bg="#333", padx=40)
avatar_frame.grid(row=0, column=0)
avatar_img=ImageTk.PhotoImage(Image.open("avatar.png"))
avatar_lbl=Label(avatar_frame,image=avatar_img, pady=20)
avatar_lbl.pack()
avatar_book_btn=Button(avatar_frame,text="Book Now",command=lambda: book_now(show_avatar), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').pack()

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
pathaan_frame = Frame(page2_centre_frame, bg="#333", padx=40)
pathaan_frame.grid(row=0, column=1)
pathaan_img=ImageTk.PhotoImage(Image.open("pathaan.png"))
pathaan_lbl=Label(pathaan_frame,image=pathaan_img)
pathaan_lbl.pack()
pathaan_book_btn=Button(pathaan_frame,text="Book Now",command=lambda: book_now(show_pathaan), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').pack()

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
varisu_frame = Frame(page2_centre_frame, bg='#333', padx=40)
varisu_frame.grid(row=0, column=2)
varisu_img=ImageTk.PhotoImage(Image.open("varisu.png"))
varisu_lbl=Label(varisu_frame,image=varisu_img)
varisu_lbl.pack()
varisu_book_btn=Button(varisu_frame,text="Book Now",command=lambda: book_now(show_varisu), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').pack()

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
kantara_frame = Frame(page2_centre_frame, bg='#333', padx=40)
kantara_frame.grid(row=0, column=3)
kantara_img=ImageTk.PhotoImage(Image.open("kantara.png"))
kantara_lbl=Label(kantara_frame,image=kantara_img)
kantara_lbl.pack()
kantara_book_btn=Button(kantara_frame,text="Book Now",command=lambda: book_now(show_kantara), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5').pack()

page2_nxt_button_frame = Frame(page2, padx=15, pady=15, bg='#333')
page2_nxt_button_frame.pack(anchor=NE, side=RIGHT)
pag2_nxt_button=Button(page2_nxt_button_frame,text='Next', command=lambda: show_frame(page3) , bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5', padx=10, pady=10).pack()

page2_back_button_frame = Frame(page2, padx=15, pady=15, bg='#333')
page2_back_button_frame.pack(anchor=NW, side=LEFT)
pag2_bk_button=Button(page2_back_button_frame,text='Back', command=lambda: show_frame(page3), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),bd='5', padx=10, pady=10).pack()

#==========page4===========

page4.configure(bg='#333333')
# pag4_label = Label(page4,text='Hey Sri', bg='#333333', fg="#FF3399", font=("Arial Black", 35)).place(x=50,y=100)
# thanku_label = Label(page4,text='Thank you for booking , Here are your details', bg='#333333', fg="#FF3399", font=("Arial Black", 25)).place(x=400,y=200)
#
# pg4_label1=Label(page4,text='Name : Sri', bg='#333333', fg="#FF3399", font=("Arial Black", 20)).place(x=450,y=300)


root.mainloop()
