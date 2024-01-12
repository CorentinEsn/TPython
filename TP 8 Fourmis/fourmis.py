# -*- coding: utf-8 -*-
import pygame
import sys
import random
import math
# -*- coding: utf-8 -*-

# Initialisation de Pygame
pygame.init()

# Paramètres de la plateforme
width, height = 800, 600
bg_color = (0, 0, 0)  # Couleur de fond

# Paramètres des fourmis
ant_size = 5

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Plateforme 2D pour les Fourmis")

class Fourmi:
    def __init__(self, x, y, direction, color, size):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = color
        self.size = size

    def move(self):
        self.turn()
        self.forward()
        self.paint()

    def turn(self):
        # Explore le voisinage
        # Calcul de la distance aux couleurs voisines
        # Choix de la couleur la plus proche
        # Calcul de la direction
        pass

    def paint(self):
        # Si petite fourmi, peint la case
        # Si grande fourmi, peint la case et les cases voisines
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def forward(self):
        # Avance d'une case dans la direction
        speed = 2  # Ajustez la vitesse selon vos besoins
        self.x += int(speed * math.cos(math.radians(self.direction)))
        self.y += int(speed * math.sin(math.radians(self.direction)))

# Fonction principale
def main():
    ants = []

    # Génération initiale de fourmis
    for _ in range(10):
        ant = Fourmi(random.randint(0, width), random.randint(0, height),
                     random.randint(0, 360), red, ant_size)
        ants.append(ant)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Déplacement des fourmis
        for ant in ants:
            ant.move()

            # Assurez-vous que les fourmis restent dans les limites de l'écran
            ant.x = max(0, min(ant.x, width - 1))
            ant.y = max(0, min(ant.y, height - 1))

        # Dessiner la plateforme et les fourmis
        screen.fill(bg_color)
        for ant in ants:
            ant.paint()

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()
