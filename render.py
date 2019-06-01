from board import *
from cell import *
from tkinter import Canvas

bg = "#baada1"
tile_bg = "#ccc1b5"

class Game(Canvas):

    def __init__(self, root):
        Canvas.__init__(self, width = 400 ,height = 400, bg=bg)
        self.root = root
        self.board = Board(self)

        for i in range(4):
            for j in range(4):
                rect = self.create_rectangle(
                    j*100 + 8, i*100 + 8, 
                    j*100+98, i*100+98, 
                    fill=tile_bg, 
                    outline="")
                self.tag_lower(rect)

        root.bind("<Up>", lambda event: self.step((-1, 0)))
        root.bind("<Down>", lambda event: self.step((1, 0)))
        root.bind("<Left>", lambda event: self.step((0, -1)))
        root.bind("<Right>", lambda event: self.step((0, 1)))

    def step(self, direction):
        if not self.board.lost:
            self.board.update(direction)
            
            if self.board.lost:
                self.create_text(
                    200, 200, 
                    text="Game Over", 
                    font="system 30 bold", 
                    fill="red")

