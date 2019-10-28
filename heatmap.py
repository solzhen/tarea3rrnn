import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from algoritmo.auxfun import generate_pop
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion, CombinarCondiciones, IgualdadCondicion
from ffuncion.fitnessfunctions import IgualdadValorFormulaYProfundidadSinRepeticion, VarCheckIgualdad
from structs.ast import *


allowed_functions = [AddNode, SubNode, MultNode, DivNode]
allowed_terminals = [1, 2, 3, 5, 7, 11, 13, 'x', 'x', 'x', 'x', 'x', 'x']

meta = AddNode(
    SubNode(
        MultNode(
            MultNode(
                TerminalVariableNode('x'),
                TerminalVariableNode('x')
            ),
            TerminalVariableNode('x')
        )
        ,
        TerminalNode(10)
    ),
    MultNode(
        TerminalVariableNode('x'),
        TerminalNode(2)
    )
)

ci = CombinarCondiciones(IteracionesCondicion(250), IgualdadCondicion(100))
ff = VarCheckIgualdad(meta)
ast = AST(allowed_functions, allowed_terminals)
heat_map_generation = np.zeros((11, 11))

mutation_rates = [0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
pop_sizes = [0, 5, 10, 25, 50, 100, 150, 200, 300, 400, 500, 1000]

for i in range(11):
    for j in range(11):
        pop_size = pop_sizes[i + 1]
        mut_rate = mutation_rates[j + 1]
        ag = AlgoritmoGenetico(pop_size, ff, ast, mut_rate, ci, 3, generate_pop)
        ret = ag.run(out=False)
        gen = len(ret)
        heat_map_generation[i][j] = gen
        print('.', end='')
    print()

print(heat_map_generation)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

plt.imshow(heat_map_generation, cmap='plasma', origin='upper')
plt.xlabel('Tasa de mutación')
plt.ylabel('Población')
plt.colorbar()

ax.set_xticklabels(mutation_rates)
ax.set_yticklabels(pop_sizes)

plt.show()
