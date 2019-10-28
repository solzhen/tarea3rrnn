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
heat_map_gens = np.zeros((10, 10))
