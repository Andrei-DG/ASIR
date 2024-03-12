from domain.modelo.Carta import Carta
class Jugador:

    def __init__(self, nombre :str, puntos :int = 0):
        self.nombre = nombre
        self.puntos = puntos
        self.carta = Carta

    def __str__(self):
        return self.nombre + " " + str(self.puntos)