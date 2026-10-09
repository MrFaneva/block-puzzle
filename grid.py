from settings import ROWS, COLS

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    def is_valid(self, piece):
        for x, y in piece.cells():
            if x < 0 or x >= COLS or y >= ROWS:
                return False
            if y >= 0 and self.grid[y][x]:
                return False
        return True

    def lock_piece(self, piece):
        # sécurité supplémentaire : ne jamais écrire hors grille
        for x, y in piece.cells():
            if 0 <= y < ROWS and 0 <= x < COLS:
                self.grid[y][x] = piece.color

    def clear_lines(self):
        new_grid = [row for row in self.grid if 0 in row]
        cleared = ROWS - len(new_grid)
        for _ in range(cleared):
            new_grid.insert(0, [0] * COLS)
        self.grid = new_grid
        return cleared
