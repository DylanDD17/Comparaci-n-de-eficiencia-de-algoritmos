# Comparación de eficiencia de algoritmos

El propósito de esta tarea es probar y comparar dos maneras de calcular el factorial de un número:

- **Recursiva**
- **Iterativa**

La idea es medir cuánto tardan y cuánta memoria usan, y ver las diferencias entre ambas.  
El programa se realizó en **C** y también en **Python** para comparar.

---

## Cómo funciona

### Método Recursivo
- La función se llama a sí misma hasta llegar a 1.
- Puede gastar más memoria porque se guardan muchas llamadas en la pila.

### Método Iterativo
- Usa un bucle (`for`) para multiplicar desde 1 hasta *n*.
- Es más eficiente con la memoria y normalmente más rápido para valores grandes.

---

## Medición de tiempo y memoria

**Tiempo:**
- En **C** se utilizó `clock()` para medir los segundos que tarda.
- En **Python** se utilizó `time.time()`.

**Memoria:**
- En **C** se utilizó `GetProcessMemoryInfo()` para saber cuánta memoria está usando el programa.
- En **Python** se utilizó `memory_profiler`.

---

## Resultados:

Los resultados obtenidos muestran que

<img width="997" height="491" alt="image" src="https://github.com/user-attachments/assets/e43c6678-0211-4f48-8144-08f1709e3c94" />

- La versión **recursiva** usa más memoria.
- La versión **iterativa** es más estable y rápida en la mayoría de los casos.
- Para números muy grandes, la recursiva puede romperse por el límite de llamadas.
