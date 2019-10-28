from algoritmo.auxfun import ez_plot, generate_pop
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion
from ffuncion.fitnessfunctions import IgualdadValorFormulaYProfundidadSinRepeticion
from structs.ast import *


allowed_functions = [AddNode, SubNode, MaxNode, MultNode]
allowed_terminals = [25, 7, 8, 100, 4, 2]

meta = 65346

ci = IteracionesCondicion(500)

ff = IgualdadValorFormulaYProfundidadSinRepeticion(meta)

ast = AST(allowed_functions, allowed_terminals)

ag = AlgoritmoGenetico(200, ff, ast, 0.5, ci, 2, generate_pop)

res = ag.run()

ez_plot(res)
