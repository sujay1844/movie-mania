from tkinter import Tk, Button, Entry, StringVar
import json

root = Tk()

with open('matrix.json') as file:
    matrix = json.load(file)

username = StringVar()
username_box = Entry(root, textvariable=username)
username_box.grid(row=0, column=0)

booked_seats = []
def create_button(row, column):
    btn = Button(root, text=chr(row+65)+str(column))
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

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(column=1, row=0)

root.mainloop()
