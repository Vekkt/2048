from random import choice, randint, random
from cell import *


class Board():

    def __init__(self, can, sample = []):
        self.can = can
        self.grid = []

        for i in range(4):
            self.grid.append([])
            for j in range(4):
                self.grid[i].append(0)

        if not sample:
            self.generateCell()
            self.generateCell()
        else:
            for i in range(4):
                for j in range(4):
                    if sample[i][j] == 0:
                        self.grid[i][j] = 0
                    else:
                        self.grid[i][j] = Cell(self, (i, j), sample[i][j])

        self.moved = False
        self.lost = False

    def freeCells(self):
        freeCells = []
        for i in range(4):
            for j in range(4):
                if self.isFree((i, j)):
                    freeCells.append((i, j))
        return freeCells

    def generateCell(self):
        cells = self.freeCells()

        if cells:
            (i, j) = choice(cells)
            value = 2 if random() < 0.9 else 4
            self.grid[i][j] = Cell(self, (i, j), value)
        else:
            self.lost = True

    def isFree(self, position):
        return self.grid[position[0]][position[1]] == 0

    def inBounds(self, i, j):
        return (0 <= i < 4) and (0 <= j < 4)

    def update(self, direction):
        if not self.freeCells:
            self.lost = True
            return

        if direction == (-1, 0):
            for i in range(4):
                for j in range(4):
                    if not self.isFree((i, j)):
                        self.moveCell(self.grid[i][j], direction)
        elif direction == (1, 0):
            for i in range(3, -1, -1):
                for j in range(4):
                    if not self.isFree((i, j)):
                        self.moveCell(self.grid[i][j], direction)
        elif direction == (0, -1):
            for j in range(4):
                for i in range(4):
                    if not self.isFree((i, j)):
                        self.moveCell(self.grid[i][j], direction)
        else:
            for j in range(3, -1, -1):
                for i in range(4):
                    if not self.isFree((i, j)):
                        self.moveCell(self.grid[i][j], direction)
        
        if self.moved:
            self.generateCell()
            self.moved = False

        return self

    def moveCell(self, cell, direction):
        while cell.canMove(direction, self):
            i, j = cell.pos
            cell.move(direction)
            x, y = cell.pos
            self.grid[x][y] = cell
            self.grid[i][j] = 0

            self.moved = True

        i, j = cell.pos
        x, y = (i + direction[0], j + direction[1])
        if self.inBounds(x, y):
            neighboor = self.grid[x][y]
                
            if neighboor.value == cell.value:
                neighboor.increase()
                self.grid[i][j] = 0
                self.can.delete(cell.rect_id)
                self.can.delete(cell.num_id)

                self.moved = True

    def score(self):
        score = 0
        for i in range(4):
            for j in range(4):
                if not self.isFree((i, j)):
                    score += self.grid[i][j].value
        return score

    def getBoard(self):
        m = []
        for i in range(4):
            m.append([])
            for j in range(4):
                if self.isFree((i, j)):
                    m[i].append(0)
                else:
                    m[i].append(self.grid[i][j].value)
        return m
