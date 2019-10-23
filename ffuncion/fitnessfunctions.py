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
