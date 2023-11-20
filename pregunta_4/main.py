# Jennifer Gámez 16-10396
# Pregunta 4: main.py, donde se hace uso de las Implementación  de las subrutinas

from sub_f import F_recursiva, F_recursiva_cola, F_iterativa
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

# Función para medir el tiempo de ejecución de una función con valores aleatorios

def main():
    # Constantes
    X = 3
    Y = 9
    Z = 6
    # m = 15 # Cantidad de valores a iterar

    # Definición de las variables globales alpha y beta basadas en las constantes X, Y, Z
    alpha = ((X + Y) % 5) + 3
    beta = ((Y + Z) % 5) + 3

    # Genera valores aleatorios para n
    # valores_n = [random.randint(50, 100) for _ in range(m)]
    valores_n = [15]

    # Lista para almacenar los tiempos de ejecución
    tiempos_recursiva = []
    tiempos_recursiva_cola = []
    tiempos_iterativa = []

    # Lista para almacenar los resultado de ejecución
    resultados_recursiva = []
    resultados_recursiva_cola = []
    resultados_iterativa = []

    for n in valores_n:

        # FUNCIÓN RECURSIVA
        inicio = time.time()
        result_recursiva = F_recursiva(alpha, beta, n)
        fin = time.time()
        t = fin - inicio
        tiempos_recursiva.append(t)
        resultados_recursiva.append(result_recursiva)

        # FUNCIÓN RECURSIVA DE COLA
        inicio = time.time()
        result_recursiva_cola = F_recursiva_cola(alpha, beta, n, [i for i in range(alpha*beta)])
        fin = time.time()
        t = fin - inicio
        tiempos_recursiva_cola.append(t)
        resultados_recursiva_cola.append(result_recursiva_cola)

        # FUNCIÓN ITERATIVA
        inicio = time.time()
        result_iterativa = F_iterativa(alpha, beta, n)
        fin = time.time()
        t = fin - inicio
        tiempos_iterativa.append(t)
        resultados_iterativa.append(result_iterativa)

    # Construyendo data
    data = {
    'F_recursiva': tiempos_recursiva,
    'F_recursiva_cola': tiempos_recursiva_cola,
    'F_iterativa': tiempos_iterativa
    }

    data_resultados = {
    'F_recursiva': resultados_recursiva,
    'F_recursiva_cola': resultados_recursiva_cola,
    'F_iterativa': resultados_iterativa
    }

    # Crear un DataFrame con los datos del tiempo
    df = pd.DataFrame(data, index=valores_n)
    
    print("Tiempo de Ejecución de las Función F")
    # Imprimir la tabla en la terminal
    print(tabulate(df, headers='keys', tablefmt='grid'))

    # Crear un DataFrame con los datos de resultados
    dr = pd.DataFrame(data_resultados, index=valores_n)

    print("\t\tResultados de Ejecución de las Función F")
    # Imprimir la tabla en la terminal
    print(tabulate(dr, headers='keys', tablefmt='grid'))

    # Graficar el tiempo de ejecución
    # plt.plot(tiempos_recursiva, label='F_recursiva')
    # plt.plot(tiempos_recursiva_cola, label='F_recursiva_cola')
    # plt.plot(tiempos_iterativa, label='F_iterativa')
    # plt.xlabel('Iteración')
    # plt.ylabel('Tiempo de ejecución')
    # plt.legend()
    # plt.show()

    # Graficar el tiempo de ejecución comparacion de f_recursiva_cola y f_iterativa
    # plt.plot(tiempos_recursiva_cola, label='F_recursiva_cola')
    # plt.plot(tiempos_iterativa, label='F_iterativa')
    # plt.xlabel('Iteración')
    # plt.ylabel('Tiempo de ejecución')
    # plt.legend()
    # plt.grid(True)  # Agregar cuadrícula al gráfico
    # plt.show()



if '__main__' == __name__:
    main()