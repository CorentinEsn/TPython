# -*- coding: utf-8 -*-
import pygame
import sys
import random
import math


# -*- coding: utf-8 -*-

class Fourmi:
    direction_table = [[0, -1],
                       [1, -1],
                       [1, 0],
                       [1, 1],
                       [0, 1],
                       [-1, 1],
                       [-1, 0],
                       [-1, -1]]

    def __init__(self, screen, color):
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())
        self.direction = random.randint(0, 7)
        self.color = color
        self.size = 5 + 5 * random.randint(0, 1)

    def move(self, screen):
        self.turn(screen)
        self.forward(screen)
        self.paint(screen)

    def turn2(self, screen):
        # Récupération des couleurs des cases voisines
        couleur_voisins = []
        height = screen.get_height()
        width = screen.get_width()
        for i in range(8):
            x = (self.x + self.direction_table[i][0]) % width
            y = (self.y + self.direction_table[i][1]) % height
            couleur_voisins.append(screen.get_at((x, y)))

        for couleur in couleur_voisins:
            if couleur == self.color:
                self.direction = couleur_voisins.index(couleur)
                print("couleur")
                break
        else:
            self.direction += random.choice([-1, 1])
            self.direction %= 8
            print("random")

    def turn(self, screen):
        self.direction += random.choice([-1, 1])
        self.direction %= 8

    def paint(self, screen):
        # Dessine la fourmi
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size//2)

    def forward(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        speed = 5  # Ajustez la vitesse selon vos besoins
        self.x += (self.direction_table[self.direction][0] * speed)
        self.y += (self.direction_table[self.direction][1] * speed)

    def erase(self, screen, bg_color):
        pygame.draw.circle(screen, bg_color, (self.x, self.y), self.size)
