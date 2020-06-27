# Tarea 3

## Pregunta 1: A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

Se importan distintas librerias para la realizacio en general del programa. En especial la libreria pandas, para asi poder leer el documento .csv y sus datos. Para esta parte entonces se procede a sumar los valores de las columnas Y y los valores de las filas X para poder encontrar su total. Se crean dos listas diferentes para asi almacenar las sumas de cada columna y fila como un vector de X y de Y, tanto de manera horizontal para las X y de manera vertical para las Y. EN las siguientes graficas se ve el comportamiento de estos datos ya sumados.

<img src="Figure_1.png">
<img src="Figure_2.png">

Siguientemente ya con estas figuras podemos encontrar una curva de ajuste. En este caso debido a la composicion podemos ajustar las dos graficas a una gaussina. Encontramos los parametros para los valores en X y en Y. Los cuales dan como resultado en X, [mu=10.0120696 ,sigma=3.19804209 ], para Y dando como resultados [mu=15.01506038 ,sigma=6.04857283 ]. Las curvas de ajuste son las siguientes

<img src="Figure_3.png">
<img src="Figure_4.png">

## Pregunta 2: Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?

Debido al ajuste que le dimos, se usa la funcion gaussiana para este calculo. La funcion gaussiana se ve en la siguiente imagen.

<img src="Gauss.png" width="200">

Ademas de que sabemos que la funcion de densidad conjunta es la siguiente.

<img src="Gauss2.png" width="200">

Por lo que hacemos los calculos para cada funcion de X y Y , luego las multimplicamos y encontramos el resultado final como se ve en la siguiente imagen.

<img src="Gauss3.png" width="400">





