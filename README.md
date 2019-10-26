# Tarea 3 Programación Genética

### Cristóbal Fuentes

# Resultados Ejercicios

## 1. Encontrar Número

### 1.1 Sin límite de repeticiones

Con el fin de encontrar el número 65346 con 
nodos terminales posibles 25, 7, 8, 100, 4, 2, y 
con operaciones Suma, Resta, Multiplicación y 
Máximo (binarios), se utilizó una población de 100 individios, 
tasa de mutación de 0.3, profundidad máxima al generar árboles
de 5, con una función de fitness que mide la distancia del
valor obtenido al buscado y entrega el valor buscado menos la distancia,
con un límite de generaciones de 50.

El siguiente gráfico muestra la evolución de la función de fitness en función
de la generación.

![Figure 1](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_1.png)

El ganador es una expresión demasiado larga como para ponerla aquí.


El siguiente gráfico muestra el tiempo de ejecución por generación, 
es decir, el tiempo que demoró
el programa en ejecutar los procesos de validación, selección y reproducción
por generación. Note como el tiempo aumenta en cada generación debido a que el crossover
tiende a incrementar la profundidad de los árboles.

![Figure 2](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_2.png)

### 1.2 Fitness

Para solucionar el problema del tiempo de ejecución, 
se reduce el puntaje de los árboles demasiado profundos.
La nueva función de fitness otorga la misma importancia
tanto al valor de la forma como la profundidad. 
Utiliza dos puntajes: mientras 
mas cercano al valor buscado, más cercano a 100 el puntaje por valor,
y mientras más cercano a 1 node de profundidad, más 
cercano el puntaje por profundidad a 100. La suma
de ambos puntajes es el puntaje final.
Se utilizó una población de 200 individuos, con 200 generaciones
como límite, tasa de mutación de 0.2:

![Figure 3](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_3.png)

El ganador fue la siguiente expressión:

**((100 + 4) * (25 * 25))**

Que da como resultado 65000

Con la nueva función de fitness
también se redujo el tiempo de ejecución por generación:

![Figure 4](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_4.png)

### 1.3 Sin repetición

Modificada la función fitness para otorgar el puntaje minimo si
se repite algún nodo terminal con un mismo valor.

Con 500 generaciones, población de 200 y una tasa de mutación de 0.5 se tiene:
  
![Figure 5](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_5.png)

Donde el ganador es la siguiente expresión:

**((4 * (25 - 2)) * (7 * 100))**

Que da como resultado 64400

## 2. Variables

Para añadir variables añadí una subclase a TerminalNode que guarda
un nombre de variable además del valor. El valor puede ser cambiado
utilizando un método (añadido a Node), lo que permite evaluar un árbol entero asignando
un valor específico a un nomrbe de variable. Sobre el nodo principal
se llama set_val con 2 argumentos. El primero indica el nombre de la variable
y el segundo el valor. Luego se puede evaluar como cualquier otro.

```python
class Node:
    ...
    def set_val(self, name, val):
        for node in self.arguments:
            node.set_val(name, val)
...
class TerminalNode(Node):
    ...
    def set_val(self, name, value):
        pass
...
class TerminalVariableNode(TerminalNode):
    def __init__(self, name):
        assert isinstance(name, str)
        self.value = 0
        super(TerminalVariableNode, self).__init__(self.value)
        self.name = name
        
    def __repr__(self):
        return str(self.name)

    def set_val(self, name, value):
        self.value = value if self.name == name else self.value
```

También cambié AST para que al crear el nodo terminal lo hiciese
en función del tipo (si era un string entonces era un terminal
variable).

## 3. Symbolic Regression

Se busca una expressión que se parezca a \
 **x * x + x - 6**

Población: 20\
Maxima Generacion: 500\
Tasa de mutación: 0.4
(nota: Le di menos peso a la penalización
por tamaño en comparación a
una expresión equivalente)

![Figure 6](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_6.png)

El ganador fue la expresión \
**((4 + (x * x)) + (x - 10))** \
Que es equivalente en valor al buscado.

## 4. División

