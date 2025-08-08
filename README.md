# Comparaci-n-de-eficiencia-de-algoritmos

El proporsito de esta tarea es probar y comparar dos maneras de calcular el factorial de un número:

Recursiva

Iterativa

La idea es medir cuánto tardan y cuánta memoria usan, y ver las diferencias entre ambas.
El programa se realizo en C y también en Python para comparar.

Cómo funciona:
Método Recursivo
La función se llama a sí misma hasta llegar a 1.
Puede gastar más memoria porque se guardan muchas llamadas en la pila.

Método Iterativo
Usa un bucle (for) para multiplicar desde 1 hasta n.
Es más eficiente con la memoria y normalmente más rápido para valores grandes.

Medicion tiempo y memoria
Tiempo:

En C usé clock() para medir los segundos que tarda.

En Python usé time.time().

Memoria:

En C usé GetProcessMemoryInfo() para saber cuánta memoria está usando el programa.

En Python usé memory_profiler.


RESULTADOS
Los resultados que obtuve muestran que:

La versión recursiva usa más memoria.

La versión iterativa es más estable y rápida en la mayoría de los casos.

Para números muy grandes, la recursiva puede llegar a romperse por límite de llamadas.
