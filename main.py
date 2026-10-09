import pygame
from game import Game
from settings import *
from colors import *
from player import Player

pygame.init()

# Variables de base
players = 1
game = None
state = "menu"

# Fenêtre initiale
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Puzzle / Tetris")
font = pygame.font.SysFont("Arial", 28)
clock = pygame.time.Clock()

running = True

while running:
    dt = clock.tick(FPS)  # dt en ms

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MENU
        if state == "menu" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                players = 1
            elif event.key == pygame.K_2:
                players = 2
            elif event.key == pygame.K_RETURN:
                players = min(players, len(Player.KEYS))
                screen = pygame.display.set_mode((WIDTH * players, HEIGHT))
                game = Game(players)
                state = "game"

        # GAME
        elif state == "game" and event.type == pygame.KEYDOWN:
            # Rotation et actions ponctuelles
            for p in game.players:
                p.handle_input(event)

            # Pause
            if event.key == pygame.K_p:
                game.toggle_pause()

    # GAME : déplacements continus avec vitesse limitée
    if state == "game":
        keys_pressed = pygame.key.get_pressed()
        for p in game.players:
            p.handle_held_keys(keys_pressed, dt)

    # Dessin
    screen.fill(BLACK)

    if state == "menu":
        screen.blit(font.render("1 = Solo | 2 = Multijoueur", True, WHITE), (40, 220))
        screen.blit(font.render("ENTER pour jouer", True, WHITE), (40, 260))

    elif state == "game":
        game.update(dt)
        game.draw(screen)

        if game.paused:
            pause_text = font.render("PAUSE", True, RED)
            screen.blit(
                pause_text,
                (screen.get_width() // 2 - pause_text.get_width() // 2,
                 HEIGHT // 2 - pause_text.get_height() // 2)
            )

    pygame.display.flip()

pygame.quit()
