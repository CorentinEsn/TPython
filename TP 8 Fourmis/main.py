import sys
import random
import pygame
from fourmis import Fourmi

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

# Fonction principale
def main():
    # Création de la fenêtre
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Plateforme 2D pour les Fourmis")

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
            ant.move(screen)

            # Assurez-vous que les fourmis restent dans les limites de l'écran
            ant.x = max(0, min(ant.x, width - 1))
            ant.y = max(0, min(ant.y, height - 1))

        # Dessiner la plateforme et les fourmis
        screen.fill(bg_color)
        for ant in ants:
            ant.paint(screen)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images
        pygame.time.Clock().tick(30)


if __name__ == "__main__":
    main()

