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
        self.forward()
        self.paint(screen)

    def turn(self, screen):
        # Récupération des couleurs voisines

        # Calcul de la distance aux couleurs voisines

        # Choix de la couleur la plus proche
        # Calcul de la direction
        # Mise à jour de la direction
        self.direction += random.choice([-1, 1])
        self.direction %= 8

    def paint(self, screen):
        # Dessine la fourmi
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        # laisse une trace au bord de la fourmi
        pygame.draw.circle(screen, self.color, (self.x + self.size * self.direction_table[self.direction][1], self.y + self.direction_table[self.direction][0]), self.size // 2)

    def forward(self):
        speed = 10  # Ajustez la vitesse selon vos besoins
        self.x += self.direction_table[self.direction][0] * speed
        self.y += self.direction_table[self.direction][1] * speed

    def erase(self, screen, bg_color):
        pygame.draw.circle(screen, bg_color, (self.x, self.y), self.size)
