import sys
import random
import threading

import pygame
from fourmis import Fourmi
from Colonie import Colonie

# Initialisation de Pygame
pygame.init()

# Paramètres de la plateforme
width, height = 500, 500
bg_color = (255, 255, 255)  # Couleur de fond

# Paramètres des fourmis
ant_size = 5

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


# Fonction principale
def main():
    # Création de la fenêtre
    screen = pygame.display.set_mode((width, height))
    screen.fill(bg_color)
    pygame.display.set_caption("Plateforme 2D pour les Fourmis")

    ants = []
    nb_colonies = 4
    taille_colonie = 1
    colonies = []
    nb_colonies = 5
    taille_colonie = 10
    for i in range(nb_colonies):
        random.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for j in range(taille_colonie):
            ant = Fourmi(screen, random.color)
            ants.append(ant)
        colonies.append(Colonie(screen, random.color, taille_colonie))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_SPACE:
                pygame.pause()


        # Déplacement des fourmis
        for colonie in colonies:
            colonie.move(screen)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images
        pygame.time.Clock().tick(200)


if __name__ == "__main__":
    main()

