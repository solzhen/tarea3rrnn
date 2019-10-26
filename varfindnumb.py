from algoritmo.auxfun import ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion
from ffuncion.fitnessfunctions import VarCheckIgualdad
from structs.ast import *


allowed_functions = [AddNode, SubNode, MultNode]
allowed_terminals = [-10, 2, 3, 4, 10, 'x', 'x', 'x', 'x', 'x']


meta = AddNode(
    SubNode(
        MultNode(
            TerminalVariableNode('x'),
            TerminalVariableNode('x')
        ),
        TerminalNode(6)
    ),
    TerminalVariableNode('x')
)


ci = IteracionesCondicion(500)

ff = VarCheckIgualdad(meta, 1000, 1000)

ast = AST(allowed_functions, allowed_terminals)


def generate_pop(n, depth, ast):
    return [ast(2) for _ in range(n)]


ag = AlgoritmoGenetico(20, ff, ast, 0.4, ci, 2, generate_pop)

res = ag.run()

ez_plot(res)