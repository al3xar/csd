from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import math
import time

hilos = 6

def calcular_bs_parcial(alpha, p, n, idx):
    """Calcula una parte de `bs` directamente."""
    parcial = {}
    for i in range(idx, n, hilos):  # Dividimos el trabajo entre hilos
        valor = pow(alpha, i, p)
        parcial[valor] = i  # Construimos el diccionario directamente
    return parcial

def bs_calc(p, alpha):
    n = math.ceil(math.sqrt(p))
    resultado = {}  # Diccionario compartido
    lock = threading.Lock()

    def thread_safe_update(parcial):
        with lock:
            resultado.update(parcial)

    with ThreadPoolExecutor(max_workers=hilos) as executor:
        futures = [executor.submit(calcular_bs_parcial, alpha, p, n, idx) for idx in range(hilos)]
        for future in as_completed(futures):
            parcial = future.result()
            thread_safe_update(parcial)

    return resultado