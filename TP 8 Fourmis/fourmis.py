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
        # explore le voisinage
        # calcul de la distace aux couleurs voisines
        # choix de la couleur la plus proche
        # calcul de la direction
        pass

    def paint(self):
        # si petite fourmi, peint la case
        # si grande fourmi, peint la case et les cases voisines
        pass

    def forward(self):
        # avance d'une case dans la direction
        pass
