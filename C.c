#include <stdio.h>
#include <time.h>
#include <windows.h>
#include <psapi.h>

// funciones
unsigned long long facto_r(unsigned int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * facto_r(n - 1);
}


unsigned long long facto_i(unsigned int n) {
    unsigned long long resultado = 1;
    for (unsigned int i = 1; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}


// funcion para medir memoria
double memoria_usada_MB() {
    PROCESS_MEMORY_COUNTERS pmc;
    GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc));
    return pmc.WorkingSetSize / (1024.0 * 1024.0);
}


// funcion para medir tiempo
double medir_tiempo(unsigned long long (*func)(unsigned int), unsigned int n) {
    clock_t inicio = clock();
    func(n);
    clock_t fin = clock();
    return (double)(fin - inicio) / CLOCKS_PER_SEC;
}


// main
int main() {
    unsigned int valores[] = {10, 100, 300, 500, 800};
    int num_valores = sizeof(valores) / sizeof(valores[0]);

    FILE *f = fopen("resultados.csv", "w");
    if (!f) {
        printf("Error al abrir resultados.csv\n");
        return 1;
    }

    fprintf(f, "n,Tiempo Recursivo (s),Memoria Recursiva (MB),Tiempo Iterativo (s),Memoria Iterativa (MB)\n");

    for (int i = 0; i < num_valores; i++) {
        unsigned int n = valores[i];

        // medir recursivo
        double mem_inicio_r = memoria_usada_MB();
        double tiempo_r = medir_tiempo(facto_r, n);
        double mem_final_r = memoria_usada_MB();
        double mem_r = mem_final_r - mem_inicio_r;

        // medir iterativo
        double mem_inicio_i = memoria_usada_MB();
        double tiempo_i = medir_tiempo(facto_i, n);
        double mem_final_i = memoria_usada_MB();
        double mem_i = mem_final_i - mem_inicio_i;

        printf("n=%u -> Recursivo: %.8f s, %.4f MB | Iterativo: %.8f s, %.4f MB\n",
               n, tiempo_r, mem_r, tiempo_i, mem_i);

        fprintf(f, "%u,%.8f,%.4f,%.8f,%.4f\n", n, tiempo_r, mem_r, tiempo_i, mem_i);
    }

    fclose(f);
    printf("\nDatos guardados en resultados.csv\n");
    return 0;
}