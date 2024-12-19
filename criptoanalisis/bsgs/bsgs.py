import math
from typing import Tuple
import pandas as pd
import time
import matplotlib.pyplot as plt
import sys
import signal
import read_file

import bs as mybs
import gs as mygs

def bsgs(
  reto: Tuple[int, int, int, int, int], hilos=6, verbose: bool = False):
  p = reto[1]
  alpha = reto[2]
  beta =reto[3]
  if (verbose):
    print(f"Para p: {p}")
    print(f"beta: {beta}")
    print(f"alpha: {alpha}")
  n = math.ceil(math.sqrt(p))
  bs = mybs.bs_calc(p, alpha,hilos)
  k = mygs.gs_calc(bs,p, alpha, beta, n,hilos);
  return k

def bsgs_wrapper(reto,hilos, verbose):
    return bsgs(reto,hilos, verbose)

def create_graphs(time_marks: list):
    df = pd.DataFrame(time_marks, columns=["time"])
    df['reto'] = [f"Reto {i+1}" for i in range(len(time_marks))]  # Nombres de retos
    plt.figure(figsize=(10, 6))
    plt.bar(df['reto'], df['time'], color='blue', alpha=0.7, edgecolor='black')
    plt.title("Tiempos por Reto")
    plt.xlabel("Retos")
    plt.ylabel("Tiempo (s)")
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje X
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()  # Ajustar para que las etiquetas no se corten
    plt.savefig('./resultados/bsgs.png')  # Guardamos la gráfica como 'bsgs.png'
    print("Gráfico guardado como 'bsgs.png'.")
    # Guardar los datos en un archivo CSV
    df.to_csv('./resultados/bsgs.csv', index=False)
    print("Datos guardados como 'bsgs.csv'.")

# Función para manejar la señal de interrupción (Ctrl+C)
def signal_handler(sig, frame):
    print('¡Has presionado Ctrl+C! Guardando datos y generando gráficos...')
    if not time_marks:
        print("No hay datos en 'time_marks' para procesar.")
        sys.exit(0)
    # Guardar los datos recolectados en un DataFrame
    create_graphs(time_marks)

    # Salir del programa
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    retos = read_file.read_retos()
    time_marks = {}
    for i in range(0,len(retos)):
        reto = retos[i]
        if reto[0] not in time_marks:
            time_marks[reto[0]] = []
        print("---------------------------------")
        print(f"Reto {i}: {reto}")
        t_start = time.time()
        k = bsgs_wrapper(reto,1,False)

        result = {
            'tiempo': (time.time() - t_start),
            'talla': reto[0],

        }
        time_marks.append(result)
        print(f"Tiempo de ejecución: {result['tiempo']} segundos")

    marks = [sum(time_marks[key]) / len(time_marks[key]) for key in time_marks if time_marks[key]]

    create_graphs(time_marks)
