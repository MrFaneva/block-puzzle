import pygame
from player import Player
from settings import *
from colors import *

class Game:
    def __init__(self, players):
        max_players = len(Player.KEYS)
        self.players = [Player(i) for i in range(min(players, max_players))]
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def update(self, dt):
        if not self.paused:
            for p in self.players:
                p.update(dt)

    def draw(self, screen):
        for p in self.players:
            p.draw(screen)

        # Barres verticales entre joueurs
        for i in range(1, len(self.players)):
            x = i * WIDTH
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 3)
