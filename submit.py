import json
import os
from matrix import update_seat_matrix
from dataclasses import asdict
from movie import Show
from json.decoder import JSONDecodeError
from tkinter import Button, Frame, BitmapImage, Label, PhotoImage
from movie import Show
import pyqrcode
import PIL
from PIL import Image, ImageTk

def submit(show:Show, username:str, frame:Frame):
    update_seat_matrix(show)
    
    with open('selected_seats.json', 'r') as file:
        seats = json.load(file)
        save_tickets_to_user(show, username, seats)

    _empty()
    info = json.dumps({
        'name': username,
        'show': asdict(show),
        'seats': seats

    })
    info = "foo"
    generate_qr_code(info)
    img  = PhotoImage(file='./ticket.png')
    print(img)
    # qr = pyqrcode.create(info)
    # qr_xbm = qr.xbm(scale=5)
    # img = BitmapImage(data=qr_xbm)
    # img.config(background='blue')
    img_lbl = Label(frame, image=img, bg='red')
    img_lbl.pack()
    Label(frame, text=info, wraplength=300).pack()

    Button(frame, text="Exit", command=exit).pack()
    frame.tkraise()

def generate_qr_code(info):
    qr = pyqrcode.create(info)
    fname = ""
    qr.png('ticket.png', scale=8)
    # return fname
def _empty() -> None:
    # empty the file for next use
    with open('selected_seats.json', 'w') as file:
        file.write("[]")

def save_tickets_to_user(show:Show, username:str, seats:list) -> None:
    print(show.name, username, seats)
    user = {
        'name': username,
        'history': [
            {
                'show': asdict(show),
                'seats': seats
            }
        ]
    }
    data = get_user_data()
    if user['name'] not in data:
        data[user['name']] = user
    else:
        data[user['name']]['history'].append(user['history'][0])
    with open('users.json', 'w+') as file:
        json.dump(data, file, indent=4)

def get_user_data() -> dict:
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        with open('users.json', 'w') as file:
            file.write('{}')
        data = {}
    return data
