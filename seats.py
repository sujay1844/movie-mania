import json
from json.decoder import JSONDecodeError
from tkinter import Button, Frame, Tk
from dataclasses import dataclass

@dataclass
class Show:
    name: str
    director: str
    imdb_rating: float
    timing: str

    screen_no: int
    no_of_rows: int
    no_of_columns: int

    file_name: str

class Seat(Button):

    def __init__(self, root:Tk | Frame, row:int, column:int, status:int) -> None:
        self.row = row
        self.column = column
        self.status = status
        self.text = chr(row+65) + str(column)

        padding = 10

        Button.__init__(
            self,
            root,
            text=self.text,
            font=('calibri', 10, 'bold'),
            bd='5',
            bg='grey' if status else '#FF3399',
            fg='#FFF',
            command=self.book,
            padx=padding, pady=padding,
        )

    def book(self) -> None:
        # If the seat is booked, ignore the button click
        if self.status: return

        # Since list of booked seats is common to all buttons, storing it in a file is better than a variable
        try:
            with open('selected_seats.json', 'r') as file:
                selected_seats = json.load(file)
        except (JSONDecodeError, FileNotFoundError):
            selected_seats = []

        coords = [self.row, self.column]
        if coords in selected_seats:
            selected_seats.remove(coords)
            self.configure(bg='#333')
        else:
            selected_seats.append(coords)
            self.configure(bg='green')

        with open('selected_seats.json', 'w') as file:
            json.dump(selected_seats, file)

