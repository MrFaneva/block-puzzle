import pygame
from grid import Grid
from piece import Piece
from score import Score
from settings import *
from colors import *

class Player:
    # Touches distinctes pour chaque joueur
    KEYS = [
        {"left": pygame.K_q, "right": pygame.K_d,
         "down": pygame.K_s, "rotate": pygame.K_z},  # Joueur 1
        {"left": pygame.K_LEFT, "right": pygame.K_RIGHT,
         "down": pygame.K_DOWN, "rotate": pygame.K_UP}  # Joueur 2
    ]

    def __init__(self, index):
        self.index = index
        self.grid = Grid()
        self.piece = Piece()
        self.score = Score()
        self.fall_time = 0
        self.offset_x = index * WIDTH
        self.font = pygame.font.SysFont("Arial", 16)

        # Timers pour touches maintenues
        self.horizontal_timer = 0
        self.vertical_timer = 0
        self.key_repeat_delay_h = 100   # ms pour horizontal
        self.key_repeat_delay_v = 50    # ms pour vertical

        # Flag pour indiquer que le sommet est atteint (GAME OVER)
        self.game_over = False

    def speed(self):
        return max(100, 500 - (self.score.level - 1) * 40)

    # Actions ponctuelles (rotation)
    def handle_input(self, event):
        if self.game_over or self.piece is None:
            return  # Plus de pièce → aucun mouvement
        keys = Player.KEYS[self.index]
        if event.key == keys["rotate"]:
            old = self.piece.shape
            self.piece.rotate()
            if not self.grid.is_valid(self.piece):
                self.piece.shape = old

    # Déplacements continus avec vitesse limitée
    def handle_held_keys(self, keys_pressed, dt):
        if self.game_over or self.piece is None:
            return  # Plus de pièce → aucun mouvement

        keys = Player.KEYS[self.index]

        # Timer horizontal
        self.horizontal_timer += dt
        if keys_pressed[keys["left"]] or keys_pressed[keys["right"]]:
            if self.horizontal_timer > self.key_repeat_delay_h:
                if keys_pressed[keys["left"]]:
                    self.piece.x -= 1
                    if not self.grid.is_valid(self.piece):
                        self.piece.x += 1
                if keys_pressed[keys["right"]]:
                    self.piece.x += 1
                    if not self.grid.is_valid(self.piece):
                        self.piece.x -= 1
                self.horizontal_timer = 0

        # Timer vertical
        self.vertical_timer += dt
        if keys_pressed[keys["down"]]:
            if self.vertical_timer > self.key_repeat_delay_v:
                self.piece.y += 1
                if not self.grid.is_valid(self.piece):
                    self.piece.y -= 1
                    self.grid.lock_piece(self.piece)
                    cleared = self.grid.clear_lines()
                    if cleared:
                        self.score.add_lines(cleared)

                    # Nouvelle pièce uniquement si espace disponible
                    new_piece = Piece()
                    if self.grid.is_valid(new_piece):
                        self.piece = new_piece
                    else:
                        self.piece = None
                        self.game_over = True  # bloque le joueur

                self.vertical_timer = 0

    def update(self, dt):
        if self.game_over or self.piece is None:
            return  # joueur bloqué → rien à faire

        self.fall_time += dt
        if self.fall_time > self.speed():
            self.piece.y += 1
            if not self.grid.is_valid(self.piece):
                self.piece.y -= 1
                self.grid.lock_piece(self.piece)
                cleared = self.grid.clear_lines()
                if cleared:
                    self.score.add_lines(cleared)

                # Nouvelle pièce uniquement si espace disponible
                new_piece = Piece()
                if self.grid.is_valid(new_piece):
                    self.piece = new_piece
                else:
                    self.piece = None
                    self.game_over = True  # bloque le joueur

            self.fall_time = 0

    def draw(self, screen):
        # Dessiner la grille avec contours
        for y in range(ROWS):
            for x in range(COLS):
                color = self.grid.grid[y][x]
                if color:
                    rect = pygame.Rect(
                        self.offset_x + x * CELL_SIZE,
                        y * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    pygame.draw.rect(screen, color, rect)       # Remplissage
                    pygame.draw.rect(screen, GRAY, rect, 2)     # Contour 2px

        # Dessiner la pièce active avec contours
        if self.piece is not None:
            for x, y in self.piece.cells():
                if y >= 0:
                    rect = pygame.Rect(
                        self.offset_x + x * CELL_SIZE,
                        y * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    pygame.draw.rect(screen, self.piece.color, rect)  # Remplissage
                    pygame.draw.rect(screen, GRAY, rect, 2)           # Contour 2px
        else:
            if self.game_over:
                # Message GAME OVER pour ce joueur
                screen.blit(
                    self.font.render("GAME OVER", True, RED),
                    (self.offset_x + 5, HEIGHT // 2)
                )

        # Affichage du score et du niveau
        screen.blit(
            self.font.render(f"Score: {self.score.score}", True, WHITE),
            (self.offset_x + 5, 5)
        )
        screen.blit(
            self.font.render(f"Niveau: {self.score.level}", True, WHITE),
            (self.offset_x + 5, 22)
        )
