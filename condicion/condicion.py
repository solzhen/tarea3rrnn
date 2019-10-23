import numpy as np


class Condicion:
    def __init__(self, meta):
        self.meta = meta
        self.ga = None

    def iniciar(self, ga):
        self.ga = ga

    def es_verdadera(self):
        return True


class IgualdadCondicion(Condicion):
    def es_verdadera(self):
        return np.amax(self.ga.puntajes) >= self.meta


class IteracionesCondicion(Condicion):
    def __init__(self, max_iter):
        super().__init__(max_iter)
        self.iteracion = 0

    def iniciar(self, ga):
        super().iniciar(ga)
        self.iteracion = 0

    def es_verdadera(self):
        self.iteracion += 1
        return self.iteracion >= self.meta


class CombinarCondiciones:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def iniciar(self, ga):
        self.c1.iniciar(ga)
        self.c2.iniciar(ga)

    def es_verdadera(self):
        return self.c1.es_verdadera() or self.c2.es_verdadera()
