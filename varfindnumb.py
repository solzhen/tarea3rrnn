from algoritmo.auxfun import ez_plot, generate_pop
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion, IgualdadCondicion, CombinarCondiciones
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

ci = CombinarCondiciones(IteracionesCondicion(500), IgualdadCondicion(100))

ff = VarCheckIgualdad(meta)

ast = AST(allowed_functions, allowed_terminals)

ag = AlgoritmoGenetico(20, ff, ast, 0.4, ci, 2, generate_pop)

res = ag.run()

ez_plot(res)
