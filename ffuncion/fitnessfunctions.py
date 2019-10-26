from structs.arboles import TerminalNode


MAX_SCORE = 100000


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
        try:
            formula_val = nodo.eval()
        except ZeroDivisionError:
            return -MAX_SCORE
        delta = abs(self.meta - formula_val) * MAX_SCORE / self.vdw
        score1 = MAX_SCORE - delta
        gamma = nodo.depth(0) - 1
        score2 = (MAX_SCORE - gamma * MAX_SCORE / self.ddw)
        return max(score1 + score2, -MAX_SCORE)


class IgualdadValorFormulaYProfundidadSinRepeticion(IgualdadValorFormulaYProfundidad):
    def aplicar(self, nodo):
        values = []
        for node in nodo.serialize():
            if isinstance(node, TerminalNode):
                if node.value in values:
                    return -2*MAX_SCORE
                else:
                    values.append(node.value)
        try:
            formula_val = nodo.eval()
        except ZeroDivisionError:
            return -MAX_SCORE
        delta = abs(self.meta - formula_val)*MAX_SCORE / self.vdw
        score1 = MAX_SCORE - delta
        gamma = nodo.depth(0) - 1
        score2 = (MAX_SCORE - gamma*MAX_SCORE / self.ddw)
        return max(score1 + score2, -MAX_SCORE)


class VarCheckIgualdad(IgualdadValorFormulaYProfundidad):
    def aplicar(self, nodo):
        MAX_SCORE = 1000
        total_score = 0
        for v in range(-100, 100, 1):
            nodo.set_val('x', v)
            self.meta.set_val('x', v)
            val1 = nodo.eval()
            val2 = self.meta.eval()
            delta = abs(val1 - val2) * MAX_SCORE / self.vdw
            score1 = MAX_SCORE - delta
            gamma = nodo.depth(0) - 1
            score2 = (MAX_SCORE - gamma * MAX_SCORE / self.ddw)
            total_score += score1 + score2
        return max(total_score, -10*MAX_SCORE)

class VarCheckIgualdad(IgualdadValorFormulaYProfundidad):
    def aplicar(self, nodo):
        MAX_SCORE = 1000
        total_score = 0
        for v in range(-100, 100, 1):
            nodo.set_val('x', v)
            self.meta.set_val('x', v)
            try:
                val1 = nodo.eval()
            except ZeroDivisionError:
                return -10 * MAX_SCORE
            val2 = self.meta.eval()
            delta = abs(val1 - val2) * MAX_SCORE / self.vdw
            score1 = MAX_SCORE - delta
            gamma = nodo.depth(0) - 1
            score2 = (MAX_SCORE - gamma * MAX_SCORE / self.ddw)
            total_score += score1 + score2
        return max(total_score, -10*MAX_SCORE)