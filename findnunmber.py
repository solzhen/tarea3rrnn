from algoritmo.auxfun import ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IgualdadCondicion, IteracionesCondicion, CombinarCondiciones
from ffuncion.fitnessfunctions import IgualdadValorFormula
from structs.ast import *


allowed_functions = [AddNode, SubNode, MaxNode, MultNode]
allowed_terminals = [25, 7, 8, 100, 4, 2]

meta = 65346
c1 = IgualdadCondicion(meta)
c2 = IteracionesCondicion(50)
ci = CombinarCondiciones(c1, c2)

ff = IgualdadValorFormula(meta)

ast = AST(allowed_functions, allowed_terminals)

def generate_pop(n, depth, ast):
	return [ast(depth) for _ in range(n)]

ag = AlgoritmoGenetico(100, ff, ast, 0.3, ci, 4, generate_pop)

res = ag.run()

ez_plot(res)
