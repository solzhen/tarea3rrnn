class IgualdadNumericString:
    def __init__(self, meta):
        self.meta = meta

    def aplicar(self, cromosoma):
        return sum(str(cromosoma[i]) == self.meta[i] for i in range(len(self.meta)))

class IgualdadString:
    def __init__(self, meta):
        self.meta = meta

    def aplicar(self, cromosoma):
        return sum(chr(cromosoma[i]) == self.meta[i] for i in range(len(self.meta)))

class KnapsackValue:
    def __init__(self, pesos, valores, limite):
        self.pesos = pesos
        self.valores = valores
        self.limite = limite

    def aplicar(self, cromosoma):
        peso_total = sum(self.pesos[i] * cromosoma[i] for i in range(len(cromosoma)))
        if peso_total > self.limite:
            return 0
        else:
            return sum(self.valores[i] * cromosoma[i] for i in range(len(cromosoma)))

class IgualdadValorFormula:
    def __init__(self, meta):
        self.meta = meta

    def aplicar(self, nodo):
        formula_val = nodo.eval()
        delta = abs(self.meta - formula_val)
        return max(self.meta - delta, 0)


class IgualdadValorFormulaYProfundidad:
    def __init__(self, meta, vdw=1000, ddw=10):
        self.meta = meta
        self.vdw = vdw
        self.ddw = ddw

    def aplicar(self, nodo):
        formula_val = nodo.eval()
        delta = abs(self.meta - formula_val)*100/self.vdw
        score1 = 100 - delta
        gamma = nodo.depth(0) - 1
        score2 = (100 - gamma*100/self.ddw)
        return max(score1 + score2, -200)