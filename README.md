# Tarea 3

## Pregunta 1: A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

Se importan distintas librerias para la realizacio en general del programa. En especial la libreria pandas, para asi poder leer el documento .csv y sus datos. Para esta parte entonces se procede a sumar los valores de las columnas Y y los valores de las filas X para poder encontrar su total. Se crean dos listas diferentes para asi almacenar las sumas de cada columna y fila como un vector de X y de Y, tanto de manera horizontal para las X y de manera vertical para las Y. EN las siguientes graficas se ve el comportamiento de estos datos ya sumados.

<img src="Figure_1.png">
<img src="Figure_2.png">

Siguientemente ya con estas figuras podemos encontrar una curva de ajuste. En este caso debido a la composicion podemos ajustar las dos graficas a una gaussina. Encontramos los parametros para los valores en X y en Y. Los cuales dan como resultado en X [mu=10.0120696 ,sigma=3.19804209 ]

Observando las curvas se sabe que tiene que ajustarse a una curva gaussiana. Por lo que se calculan los parámetros y se obtiene un valor de mu=9.90484381 y sigma= 3.29944287 para la curva de mejor ajuste de acuerdo a la distribución en "X". Se obtiene un valor de mu=15.0794609 y sigma=6.02693775 para la curva de mejor ajuste de acuerdo a la distribución en "Y". Ambos ajustes de curva se ven en la siguiente gráfica:



