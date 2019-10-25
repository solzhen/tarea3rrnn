# tarea3rrnn
# Tarea 3 Algoritmo Genetico

Cristóbal Fuentes

# Ejercicios

## Encontrar Número

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

![Figure 1](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_1.png)

El siguiente gráfico muestra el tiempo de ejecución que demoró
el programa en ejecutar los procesos de validación, selección y reproducción
por generación. Note como el tiempo aumenta en cada generación debido a que el crossover
tiende a aumentar la profundidad de los árboles.

![Figure 1](https://github.com/solzhen/tarea2rrnn/blob/master/figs/Figure_2.png)


## Resultados