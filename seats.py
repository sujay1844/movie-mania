from tkinter import Button
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

    def __init__(self, root, row, column, status):
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
            bg='red' if status else 'white',
            command=self.book,
            padx=padding, pady=padding,
        )

    def book(self):
        # If the seat is booked, ignore the button click
        if self.status: return

        self.configure(bg='green')

        # Since list of booked seats is common to all buttons, storing it in a file is better than a variable
        with open('selected_seats.txt', 'a') as file:
            file.write( str(self.row) + str(self.column) + '\n' )
