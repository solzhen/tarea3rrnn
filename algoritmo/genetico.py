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
        import time
        d = time.time()
        while True:
            i += 1
            self.evaluacion()
            maxp, prom, minp = self.meta()
            elapsed = time.time() - d
            if out:
                sys.stdout.write("\033[K")
                print("Generation {} Winner: {}".format(i, self.poblacion[np.argmax(self.puntajes)]))
                print("Max Score: {} ; Average Score: {} ; Min Score: {}".format(maxp, prom, minp))
                print("Iteration time: {} seconds".format(elapsed))
            d = time.time()
            retorno.append([maxp, prom, minp, elapsed])
            if self.condicion.es_verdadera():
                break
            self.seleccion()
            self.reproduccion()

        return np.array(retorno)

    def meta(self):
        max_puntaje = np.amax(self.puntajes)
        pt_promedio = np.average(self.puntajes)
        min_puntaje = np.amin(self.puntajes)
        return max_puntaje, pt_promedio, min_puntaje

    def generar_poblacion(self):
        self.poblacion = self.funcion_pob(self.n, self.largo_cromosoma, self.funcion_gen)

    def evaluacion(self):
        self.puntajes = np.array([self.funcion_fitness.aplicar(self.poblacion[i]) for i in range(self.n)])

    def seleccion(self):
        self.padres = [
            self.poblacion[
                max(np.random.randint(self.n, size=5), key=lambda x: self.puntajes[x])
            ] for i in range(self.n)
        ]

    def reproduccion(self):
        ganador = self.poblacion[int(np.argmax(self.puntajes))]
        self.poblacion = [
            self.mutar(self.crossover(self.padres[i-1], self.padres[i])) for i in range(self.n)
        ]
        self.poblacion[-1] = ganador

    def crossover(self, padre, madre):
        ## CHANGE
        new_element = padre.copy()
        nodes_1 = new_element.serialize()
        p1 = nodes_1[np.random.randint(0, len(nodes_1))]
        second_element = madre.copy()
        nodes_2 = second_element.serialize()
        p2 = nodes_2[np.random.randint(0, len(nodes_2))]
        p1.replace(p2)
        return new_element

    def mutar(self, cromosoma):
        ## CHANGE
        new_element = cromosoma.copy()
        nodes_1 = new_element.serialize()
        p1 = nodes_1[np.random.randint(0, len(nodes_1))]
        p2 = self.funcion_gen(np.random.randint(0, self.largo_cromosoma))
        p1.replace(p2)
        return new_element
