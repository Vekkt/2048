from random import randint, choice, random
from tkinter import Canvas
from math import log2
from board import *

bg = "#baada1"
colors = [
    "#ccc1b5", 
    "#eee4da", 
    "#eddfc9",
    "#f0b07d",
    "#f39568",
    "#f47c64",
    "#f35f42",
    "#ecce78",
    "#eccb69",
    "#ecc75a",
    "#ecc44d",
    "#ecc13f"
]

class Cell():

    def __init__(self, board, pos, value):
        self.pos = pos
        self.value = value
        self.board = board
        self.can = board.can

        (x, y) = pos
        self.rect_id = self.can.create_rectangle(
            y * 100 + 8, x * 100 + 8,
            y * 100 + 98, x * 100 + 98,
            fill=colors[int(log2(self.value))],
            outline="")
        self.num_id = self.can.create_text(
            y * 100 + 50, x * 100 + 50,
            text = str(value),
            font="system 30 bold",
            fill="#776e66")

    def getValue(self):
        return self.value

    def increase(self):
        self.value *= 2

        fill = "#f9f6f2" if self.value > 4 else "#776e66"
        self.can.itemconfig(self.num_id, text=str(self.value), fill=fill)
        self.can.itemconfig(self.rect_id, fill=colors[int(log2(self.value))])

    def move(self, direction):
        self.pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])

        self.can.move(self.rect_id, direction[1]*100, direction[0]*100)
        self.can.move(self.num_id, direction[1]*100, direction[0]*100)
    
    def canMove(self, direction, board):
        i, j = (self.pos[0] + direction[0], self.pos[1] + direction[1])
        return (0 <= i < 4) and (0 <= j < 4) and board.isFree((i, j))

