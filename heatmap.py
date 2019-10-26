import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion
from ffuncion.fitnessfunctions import IgualdadValorFormulaYProfundidadSinRepeticion
from structs.ast import *


def generate_pop(n, depth, ast):
    return [ast(depth) for _ in range(n)]


allowed_functions = [AddNode, SubNode, MultNode, DivNode]
allowed_terminals = [1,2,3,5,7,11,13,17,19,23]
meta = 65346
ci = IteracionesCondicion(100)
ast = AST(allowed_functions, allowed_terminals)
heat_map_max = np.zeros((10, 10))
heat_map_depth = np.zeros((10, 10))
heat_map_time = np.zeros((10, 10))

for i in range(10):
    for j in range(10):
        ff = IgualdadValorFormulaYProfundidadSinRepeticion(meta, 10**(i+1), (j+1)*10)
        ag = AlgoritmoGenetico(50, ff, ast, 0.2, ci, 3, generate_pop)
        res = ag.run(out=False)
        winner_val = ag.poblacion[np.argmax(ag.puntajes)]
        heat_map_max[i][j] = winner_val.eval()
        heat_map_depth[i][j] = winner_val.depth(0)
        heat_map_time[i][j] = res[-1][-1]
        print(".", end='')
    print()


def heatplot(heat_map, cm):
    a0 = plt.subplot(111)
    im0 = a0.imshow(heat_map, cmap=cm,
                    interpolation='bilinear', extent=[0, 9, 0, 9],
                    )
    divider0 = make_axes_locatable(a0)
    cax0 = divider0.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im0, cax=cax0)
    plt.show()


heatplot(heat_map_max, 'hot')
heatplot(heat_map_time, 'plasma')
heatplot(heat_map_depth, 'gnuplot')