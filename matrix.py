import json
import os
from tkinter import CENTER, Frame, Label
from seats import Seat
from movie import Show

def get_matrix(show:Show) -> list:

    if not os.path.exists(show.file_name):
        create_matrix_file(show)

    with open(show.file_name, 'r') as file:
        matrix = json.load(file)
    return matrix

def update_seat_matrix(show:Show) -> None:
    matrix = get_matrix(show)
    with open(show.file_name, 'w') as output:
        with open('selected_seats.json', 'r') as input:
            for seat in json.load(input):
                row, column = seat
                matrix[row][column] = 1
        json.dump(matrix, output)

def create_matrix_file(show:Show) -> None:

    # Delete if already exists
    if os.path.exists(show.file_name):
        os.remove(show.file_name)

    matrix = [[0]*show.no_of_columns for _ in range(show.no_of_rows)]

    with open(show.file_name, 'w') as output:
        json.dump(matrix, output)

def create_button_matrix(frame:Frame, show:Show) -> Frame:

    sub_frame = Frame(frame)
    button_frame = Frame(sub_frame)
    matrix = get_matrix(show)
    for row in range(show.no_of_rows):
        for column in range(show.no_of_columns):

            seat = Seat(button_frame, row, column, matrix[row][column])
            seat.grid(row=row, column=column)
    button_frame.grid(row=0, column=1)
    sub_frame.place(anchor=CENTER, relx=.5, rely=.5)
    return sub_frame
