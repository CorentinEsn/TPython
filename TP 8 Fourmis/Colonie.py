import threading

import pygame

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
        ant_threadpool = []*self.numberAnts
        for ant in self.ants:
            pygame.draw.circle(screen, ant.color, (ant.x, ant.y), ant.size)
            ant_threadpool.append(threading.Thread(target=ant.move(screen)))

        for thread in ant_threadpool:
            thread.start()

        for thread in ant_threadpool:
            thread.join()

        for ant in self.ants:
            pygame.draw.circle(screen, (255,0,0), (ant.x, ant.y), ant.size)