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
Utiliza dos puntajes: puntaje por valo y putnaje por profundidad.\
 El puntaje va de 0 a 100, mientras 
mas cercano al valor buscado, más cercano a 100. \
El puntaje por profundidad va de 0 a 1, y es igual a 1 mientras la 
profundidad del árbol sea menor a un hiperparametro definido para la 
función (5 por defecto). Ambos valores se multiplican para dar el valor
final. \
Además, hay dos hiperparámetros que definen que tanto se penaliza en cada
puntaje, por ejemplo, una diferencia de 100 en el valor se puede
modular para que castigue más o menos fuerte utilizando estos hiperparámetros.


Se utilizó una población de 200 individuos, con 200 generaciones
como límite, tasa de mutación de 0.2:

![Figure 3](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_3.png)

El ganador fue la siguiente expressión:

La última generación tuvo el siguiente output:
```javascript
Generation 200 Winner: ((25 * ((100 + 4) * 25)) + (max({4, (100 - 25)}) - ((7 + 8) * (7 - 25))))
Max Score: 99.99846968444893 ; Average Score: 26.244345885857427 ; Min Score: 0.0
Iteration time: 0.4520258903503418 seconds
```

Que da como resultado **65345**

Con la nueva función de fitness
también se redujo el tiempo de ejecución por generación:

![Figure 4](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_4.png)

### 1.3 Sin repetición

Modificada la función fitness para otorgar el puntaje minimo si
se repite algún nodo terminal con un mismo valor.

Con 500 generaciones, población de 200 y una tasa de mutación de 0.5 se tiene:
  
![Figure 5](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_5.png)

Donde el ganador tuvo el siguiente output:

```javascript
Generation 500 Winner: ((4 * 7) * (8 + (100 * (25 - 2))))
Max Score: 98.8951121721299 ; Average Score: 1.6218360725981693 ; Min Score: 0.0
Iteration time: 0.09600543975830078 seconds
```

Que da como resultado **64624**

## 2. Variables

Para añadir variables añadí una subclase a TerminalNode que guarda
un nombre de variable además del valor. El valor puede ser cambiado
utilizando un método (añadido a Node), lo que permite evaluar un 
árbol entero asignando
un valor específico a un nombre de variable. Sobre el nodo principal
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

La función de fitness simplemente setea un valor y evalua. Sumando los 
puntajes para cada valor y dividiendo por la cantidad de valores.

## 3. Symbolic Regression

Se busca una expressión que se parezca a \
 **x * x + x - 6**

Población: 20\
Maxima Generacion: 500\
Tasa de mutación: 0.4\
Terminales permitidas: -10, 2, 3, 4, 10, 'x'\

![Figure 6](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_6.png)

El ganador:

````javascript
Generation 16 Winner: (((4 + -10) + x) + (x * (x + (x - x))))
Max Score: 100.0 ; Average Score: 71.80025610045008 ; Min Score: 11.745486851456997
Iteration time: 0.1240072250366211 seconds
````
En la generación 16.

## 4. División

Siguiendo la sugerencia del enunciado, las excepciones ZeroDivisionError
le dan el puntaje mínimo al árbol.

Población: 20\
Maxima Generacion: 500\
Tasa de mutación: 0.4\
Terminales permitidas: 1, 2, 3, 5, 7, 11, 13, 'x'


![Figure 7](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_7.png)

Con ganador:
````javascript
Generation 114 Winner: ((1 * (x * x)) + ((1 + x) - 7))
Max Score: 100.0 ; Average Score: 58.94085011091728 ; Min Score: 0.0
Iteration time: 0.12700724601745605 seconds
````
En la generación 114.

# Análisis

## Heatmap 
El siguiente heatmap grafica la generación en la que se encontró la 
expresión equivalente a \
**x * x * x + 2 * x - 10**
usando terminales:\
1, 2, 3, 5, 7, 11, 13, 'x' \
Y operaciones +, -, *, /

Con un límite de 250 generaciones, variando la población y tasa de 
mutación de la siguiente forma:

tasas de mutación : 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0\
poblaciones : 5, 10, 25, 50, 100, 150, 200, 300, 400, 500, 1000

El siguiente heatmap grafica la cantidad de generaciones requeridas para
encontrar una expresión equivalente a x * x * x + 2 * x - 10. Si después de 250
no se consiguió encontrar el programa se detiene. Se debe asumir que 
las coordenadas con valor 250 no lograron encontrar la expresión buscada.

![Figure 8](https://github.com/solzhen/tarea3rrnn/blob/master/figs/Figure_8.png)



 
 