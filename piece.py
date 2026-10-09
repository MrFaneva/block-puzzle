import random
from colors import *

SHAPES = [
    ([[1, 1, 1, 1]], CYAN),
    ([[1, 1], [1, 1]], YELLOW),
    ([[0, 1, 0], [1, 1, 1]], PURPLE),
    ([[1, 0, 0], [1, 1, 1]], BLUE),
    ([[0, 0, 1], [1, 1, 1]], ORANGE),
    ([[0, 1, 1], [1, 1, 0]], GREEN),
    ([[1, 1, 0], [0, 1, 1]], RED),
]

class Piece:
    def __init__(self):
        self.shape, self.color = random.choice(SHAPES)
        self.x = 3
        self.y = -2

    def cells(self):
        return [
            (self.x + x, self.y + y)
            for y, row in enumerate(self.shape)
            for x, cell in enumerate(row)
            if cell
        ]

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
