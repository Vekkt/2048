from tkinter import Tk, Canvas, mainloop
from render import *

def main():
    root = Tk()
    board = Game(root)
    board.pack()
    mainloop()

if __name__ == '__main__':
   main()