import fourmis
class Colonie:

    def __init__(self, screen, color, numberAnts):
        self.color = color
        self.numberAnts = numberAnts
        self.ants = []
        for _ in range(numberAnts):
            ant = fourmis.Fourmi(screen, color)
            self.ants.append(ant)

    def move(self, screen):
        for ant in self.ants:
            ant.move(screen)
            # Assurez-vous que les fourmis restent dans les limites de l'écran
            if ant.x < 0:
                ant.x = screen.get_width()
            if ant.x > screen.get_width():
                ant.x = 0
            if ant.y < 0:
                ant.y = screen.get_height()
            if ant.y > screen.get_height():
                ant.y = 0
