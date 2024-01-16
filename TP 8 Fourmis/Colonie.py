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
