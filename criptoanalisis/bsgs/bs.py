import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import math

def calcular_bs_parcial(alpha, p, n, idx, hilos):
    """Calcula una parte de `bs` directamente."""
    parcial = {}
    for i in range(idx, n, hilos):  # Dividimos el trabajo entre procesos
        valor = pow(alpha, i, p)
        parcial[valor] = i  # Construimos el diccionario directamente
    return parcial

def bs_calc(p, alpha, hilos=6):
    n = math.ceil(math.sqrt(p))
    resultado = {}  # Diccionario final

    with ProcessPoolExecutor(max_workers=hilos) as executor:
        futures = [executor.submit(calcular_bs_parcial, alpha, p, n, idx, hilos) for idx in range(hilos)]
        for future in as_completed(futures):
            parcial = future.result()
            resultado.update(parcial)  # Combina los resultados
    return resultado

def main():
    p = 157943476947589
    alpha = 18
    print(f"Para p: {p}")
    print(f"alpha: {alpha}")
    start_time = time.time()
    bs = bs_calc(p, alpha, 16)
    end_time = time.time() - start_time
    print(f"length: {len(bs)}")
    print(f"Execution time: {end_time}")


if __name__ == "__main__":
    main()

