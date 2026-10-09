import pygame

pygame.mixer.init()

SOUNDS = {
    "move": pygame.mixer.Sound("assets/sounds/move.wav"),
    "rotate": pygame.mixer.Sound("assets/sounds/rotate.wav"),
    "clear": pygame.mixer.Sound("assets/sounds/clear.wav"),
    "gameover": pygame.mixer.Sound("assets/sounds/gameover.wav"),
}

def play(name):
    if name in SOUNDS:
        SOUNDS[name].play()
