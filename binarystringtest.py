from algoritmo.auxfun import heterogenetic_pop, ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IgualdadCondicion, IteracionesCondicion, CombinarCondiciones
from ffuncion.fitnessfunctions import IgualdadNumericString
from gfuncion.generators import binary_gen
from structs.arboles import *
from structs.ast import *


meta = "001010101101010110101110"
c1 = IgualdadCondicion(len(meta))
c2 = IteracionesCondicion(100)
ci = CombinarCondiciones(c1, c2)
ff = IgualdadNumericString(meta)
ag = AlgoritmoGenetico(100, ff, binary_gen, 0.1, ci, len(meta), heterogenetic_pop)

ez_plot(ag.run())
