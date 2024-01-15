import sys
import random
import pygame
from fourmis import Fourmi

# Initialisation de Pygame
pygame.init()

# Paramètres de la plateforme
width, height = 1920, 1080
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
    nb_colonies = 2
    taille_colonie = 70
    for i in range(nb_colonies):
        random.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(taille_colonie):
            ant = Fourmi(screen, random.color)
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
            if ant.x < 0 :
                ant.x = width
            if ant.x > width :
                ant.x = 0
            if ant.y < 0 :
                ant.y = height
            if ant.y > height:
                ant.y = 0


        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter la fréquence d'images
        pygame.time.Clock().tick(30)


if __name__ == "__main__":
    main()

