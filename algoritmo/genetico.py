import numpy as np
import sys


class AlgoritmoGenetico:
    def __init__(self, n, f_f, f_g_g, t_d_m, c_d_t, l_c, f_g_i):
        '''

        :param n: tamaño poblacion
        :param f_f: ffuncion de fitness
        :param f_g_g: ffuncion de generacion de genes
        :param t_d_m: tasa de mutacion
        :param c_d_t: condicion de termino
        :param l_c: largo de cromosoma
        :param f_g_i: ffuncion de generacion de poblacion
        '''
        self.n = n
        self.funcion_fitness = f_f
        self.funcion_gen = f_g_g
        self.tasa_mutacion = t_d_m
        self.condicion = c_d_t
        self.poblacion = None
        self.puntajes = None
        self.padres = None
        self.largo_cromosoma = l_c
        self.funcion_pob = f_g_i
        pass

    def run(self, out=True):
        retorno = []
        self.generar_poblacion()
        self.condicion.iniciar(self)
        i = 0
        while True:
            i += 1
            self.evaluacion()
            maxp, prom, minp = self.meta()
            if out:
                sys.stdout.write("\033[K")
                print("Generation {} Winner: {}".format(i, self.poblacion[np.argmax(self.puntajes)]))
                print("Max Score: {} ; Average Score: {} ; Min Score: {}".format(maxp, prom, minp))
            retorno.append([maxp, prom, minp])
            if self.condicion.es_verdadera():
                break
            self.seleccion()
            self.reproduccion()
        return np.array(retorno)

    def meta(self):
        max_puntaje = np.amax(self.puntajes)
        pt_promedio = np.median(self.puntajes)
        min_puntaje = np.amin(self.puntajes)
        return max_puntaje, pt_promedio, min_puntaje

    def generar_poblacion(self):
        self.poblacion = self.funcion_pob(self.n, self.largo_cromosoma, self.funcion_gen)

    def evaluacion(self):
        self.puntajes = np.array([self.funcion_fitness.aplicar(self.poblacion[i]) for i in range(self.n)])

    def seleccion(self):
        self.padres = np.array([
            self.poblacion[
                max(np.random.randint(self.n, size=5), key=lambda x: self.puntajes[x])
            ] for i in range(self.n)
        ])

    def reproduccion(self):
        ganador = self.poblacion[np.argmax(self.puntajes)]
        self.poblacion = np.array([
            self.mutar(self.crossover(self.padres[i-1], self.padres[i])) for i in range(self.n)
        ])
        self.poblacion[-1] = ganador

    def crossover(self, padre, madre):
        p = np.random.randint(0, self.n)
        r = np.array([
            padre[i] if i < p else madre[i] for i in range(self.largo_cromosoma)
        ])
        return r

    def mutar(self, cromosoma):
        return np.array([
            cromosoma[i] if np.random.rand() > self.tasa_mutacion else self.funcion_gen() for i in range(
                self.largo_cromosoma
            )
        ])
