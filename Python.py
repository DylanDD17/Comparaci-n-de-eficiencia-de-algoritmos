from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import time

# funciones 
def facto_r(n):
    """recursivo"""
    if n == 0 or n == 1:
        return 1
    return n * facto_r(n - 1)

def facto_i(n):
    """iterativo"""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# mediciones 
def medir(func, n):
    """mide tiempo y memoria de ejecución de cada función"""
    inicio_tiempo = time.time()
    mem_usage = memory_usage((func, (n,)), max_iterations=1)
    fin_tiempo = time.time()
    tiempo_total = fin_tiempo - inicio_tiempo
    memoria_max = max(mem_usage) - min(mem_usage)
    return tiempo_total, memoria_max

# cosa de windows
if __name__ == "__main__":
    ns = [10, 100, 300, 600, 900]  # valores de prueba


    # guardar
    tiempos_recursivo = []
    tiempos_iterativo = []
    memoria_recursivo = []
    memoria_iterativo = []

    # bucle de mediciones
    for n in ns:
        t_rec, m_rec = medir(facto_r, n)
        t_it, m_it = medir(facto_i, n)

        tiempos_recursivo.append(t_rec)
        memoria_recursivo.append(m_rec)
        tiempos_iterativo.append(t_it)
        memoria_iterativo.append(m_it)

    # resultados en consola
    print("Tiempos recursivo:", tiempos_recursivo)
    print("Tiempos iterativo:", tiempos_iterativo)
    print("Memoria recursivo:", memoria_recursivo)
    print("Memoria iterativo:", memoria_iterativo)

 
    # graficar tiempos
    plt.figure(figsize=(10,5))

    plt.subplot(1, 2, 1)
    plt.plot(ns, tiempos_recursivo, label="Recursivo", marker="o")
    plt.plot(ns, tiempos_iterativo, label="Iterativo", marker="o")
    plt.xlabel("n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo - Factorial Recursivo vs Iterativo")
    plt.legend()
    plt.grid(True)

    
    # graficar memoria
    plt.subplot(1, 2, 2)
    plt.plot(ns, memoria_recursivo, label="Recursivo", marker="o")
    plt.plot(ns, memoria_iterativo, label="Iterativo", marker="o")
    plt.xlabel("n")
    plt.ylabel("Uso de memoria (MB)")
    plt.title("Memoria - Factorial Recursivo vs Iterativo")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()