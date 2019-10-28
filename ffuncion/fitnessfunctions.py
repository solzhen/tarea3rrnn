from structs.arboles import TerminalNode


class IgualdadValorFormula:
    def __init__(self, meta):
        self.meta = meta

    def aplicar(self, nodo):
        formula_val = nodo.eval()
        delta = abs(self.meta - formula_val)
        return max(self.meta - delta, 0)


class IgualdadValorFormulaYProfundidad:
    def __init__(self, meta, vdw=10000, ddw=5, depth=5):
        self.meta = meta
        self.vdw = vdw
        self.ddw = ddw
        self.depth = depth

    def aplicar(self, nodo):
        try:
            formula_val = nodo.eval()
        except ZeroDivisionError:
            return 0
        delta = abs(self.meta - formula_val) * 100 / self.vdw
        score1 = max(100 - delta, 0)
        gamma = max(nodo.depth(0) - self.depth, 0)
        score2 = self.ddw / (self.ddw + gamma)
        return score1*score2


class IgualdadValorFormulaYProfundidadSinRepeticion(IgualdadValorFormulaYProfundidad):
    def aplicar(self, nodo):
        values = []
        for node in nodo.serialize():
            if isinstance(node, TerminalNode):
                if node.value in values:
                    return 0
                else:
                    values.append(node.value)
        return super().aplicar(nodo)


class VarCheckIgualdad(IgualdadValorFormulaYProfundidad):
    def __init__(self, meta, vdw=10000, ddw=5, depth=5, names=None):
        if names is None:
            self.names = ['x']
        super().__init__(meta, vdw, ddw, depth)

    def aplicar(self, nodo):
        total_score = 0
        for v in range(-100, 101, 1):
            try:
                nodo.set_val('x', v)
                self.meta.set_val('x', v)
                formula_val = nodo.eval()
                meta = self.meta.eval()
            except ZeroDivisionError:
                return 0
            delta = abs(meta - formula_val) * 100 / self.vdw
            score1 = max(100 - delta, 0)
            gamma = max(nodo.depth(0) - self.depth, 0)
            score2 = self.ddw / (self.ddw + gamma)
            total_score += (score1 * score2)
        return total_score / 201
