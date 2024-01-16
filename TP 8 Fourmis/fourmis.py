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
        self.paint(screen, self.color)
        self.turn(screen)
        self.forward(screen)
        self.paint(screen, (255, 0, 0))


    def turn(self, screen):
        # Récupération des couleurs des cases voisines
        voisins = []
        weights = []

        for i in range(2):
            if i == 0:
                x = (self.x + self.direction_table[self.direction][0] * self.size)
                y = (self.y + self.direction_table[self.direction][1] * self.size)
                x, y = self.stay_in_bounds(x, y, screen)
                voisins.append([screen.get_at((x, y)), self.direction])
            else:
                x = (self.x + self.direction_table[(self.direction+i)%8][0] * self.size)
                y = (self.y + self.direction_table[(self.direction+i)%8][1] * self.size)
                x, y = self.stay_in_bounds(x, y, screen)
                voisins.append([screen.get_at((x, y)), (self.direction+i)%8])
                x = (self.x + self.direction_table[(self.direction-i)%8][0] * self.size)
                y = (self.y + self.direction_table[(self.direction-i)%8][1] * self.size)
                x, y = self.stay_in_bounds(x, y, screen)
                voisins.append([screen.get_at((x, y)), (self.direction-i)%8])

        #calcul la distance de la couleur de la fourmi avec les couleurs des cases voisines
        for v in voisins:
            # si la couleur du voisins est la même que la couleur de la fourmi, on lui donne un poids de 0
            if v[0] == self.color:
                weights.append(1)
            else : weights.append(1/(math.sqrt((self.color[0] - v[0][0])**2 + (self.color[1] - v[0][1])**2 + (self.color[2] - v[0][2])**2)+1))

        #choisit une direction aléatoirement parmis les voisins
        selected_v = random.choices(voisins, weights)
        self.direction = selected_v[0][1]


    def random_turn(self, screen):
        self.direction += random.choice([-1, 0, 1])
        self.direction %= 8

    def paint(self, screen, color):
        # Dessine la fourmi
        pygame.draw.circle(screen, color, (self.x, self.y), self.size//2)

    def forward(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        speed = self.size//2  # Ajustez la vitesse selon vos besoins
        x = self.x + (self.direction_table[self.direction][0] * speed)
        y = self.y + (self.direction_table[self.direction][1] * speed)
        x, y = self.stay_in_bounds(x, y, screen)
        self.x = x
        self.y = y

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
