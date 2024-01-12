# -*- coding: utf-8 -*-
import pygame
import sys
import random
import math
# -*- coding: utf-8 -*-

class Fourmi:

    def __init__(self, x, y, direction, color, size):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = color
        self.size = size

    def move(self, screen):
        self.turn()
        self.forward()
        self.paint(screen)

    def turn(self):
        # Explore le voisinage
        # Calcul de la distance aux couleurs voisines
        # Choix de la couleur la plus proche
        # Calcul de la direction
        pass

    def paint(self, screen):
        # Si petite fourmi, peint la case
        # Si grande fourmi, peint la case et les cases voisines
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def forward(self):
        # Avance d'une case dans la direction
        speed = 2  # Ajustez la vitesse selon vos besoins
        self.x += int(speed * math.cos(math.radians(self.direction)))
        self.y += int(speed * math.sin(math.radians(self.direction)))


