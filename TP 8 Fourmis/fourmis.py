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

    def turn(self, screen):
        # Récupération des couleurs des cases voisines
        print("old direction: ", self.direction)
        couleur_voisins = []
        possible_dir = []
        height = screen.get_height()
        width = screen.get_width()

        for i in range(1):
            if i == 0:
                x = (self.x + self.direction_table[self.direction][0] * self.size)
                y = (self.y + self.direction_table[self.direction][1] * self.size)
            else:
                x = (self.x + self.direction_table[self.direction+i][0] * self.size)
                y = (self.y + self.direction_table[self.direction+i][1] * self.size)

            x, y = self.stay_in_bounds(x, y, screen)
            couleur_voisins.append(screen.get_at((x, y)))

        for couleur in couleur_voisins:
            if couleur == self.color:
                possible_dir.append(couleur_voisins.index(couleur))
                break
        #choisit une direction aléatoirement parmis les directions possibles
        if possible_dir != []:
            random.shuffle(possible_dir)
            self.direction = random.choice(possible_dir)
        else:
            self.direction += random.choice([-1, 1])
            self.direction %= 8
        print("new direction: ", self.direction)

    def turn2(self, screen):
        self.direction += random.choice([-1, 1])
        self.direction %= 8

    def paint(self, screen):
        # Dessine la fourmi
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size//2)

    def forward(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        speed = self.size//2  # Ajustez la vitesse selon vos besoins
        x = self.x + (self.direction_table[self.direction][0] * speed)
        y = self.y + (self.direction_table[self.direction][1] * speed)
        x, y = self.stay_in_bounds(x, y, screen)
        self.x = x
        self.y = y



    def erase(self, screen, bg_color):
        pygame.draw.circle(screen, bg_color, (self.x, self.y), self.size)

    def stay_in_bounds(self, x, y, screen):
        width = screen.get_width()
        height = screen.get_height()
        if x <= 0:
            x = width-1
        if x >= width:
            x = 1

        if y <= 0:
            y = height-1
        if y >= height:
            y = 1

        return x, y
