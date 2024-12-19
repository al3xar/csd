import math
import bs
import sys
import threading
import math


def calcular_gamma(bs_dic, gamma ,alpha2mn,n, p,mn, result, lock, idx, hilos, verbose=False):
  for q in range(idx, mn, hilos):
    with lock:
      if result['found']:
        return
    if gamma in bs_dic:
      j = bs_dic[gamma]
      k = q * n + j
      with lock:
        result['found'] = True
        result['k'] = k
      return
    gamma = (gamma * pow(alpha2mn,hilos,p)) % p
    if (verbose):
      print(f"gamma: {gamma}")


def gs_calc(bs_dic, p, alpha,beta,n,hilos=6, verbose=False):
  result = {'found': False, 'k': None}
  threads = []
  lock = threading.Lock()
  mn = p-1-n
  alpha2mn = pow(alpha,mn,p)
  for i in range(hilos):
    gamma = (beta * pow(alpha2mn, i, p)) % p
    hilo = threading.Thread(target=calcular_gamma, args=(bs_dic, gamma,alpha2mn, n, p, mn, result, lock, i, hilos, verbose))
    threads.append(hilo)
    hilo.start()

  for hilo in threads:
    hilo.join()

  if result['found']:
      k = result['k']
      print(f"K encontrado: {k}")
      beta_prima = pow(alpha,k,p)
      print(f"Verificación: {beta_prima} es igual a {beta}")
  else:
      print("No se encontró K en el rango especificado.")
  return result['k']

def main():
  #tomar los argumentos por consola de p, alpha y beta
  if len(sys.argv) < 4:
    sys.exit("Faltan argumentos")
  p = int(sys.argv[1])
  alpha = int(sys.argv[2])
  beta = int(sys.argv[3])
  print("Generando bs...")
  bs_dic = bs.bs_calc(p, alpha, 16)  # Construir la tabla de baby steps
  # example bs: {1: 0, 3: 1, 9: 2, 27: 3, 81: 4, 243: 5, 729: 6, 2187: 7, 6561: 8, 4337: 9, 5338: 10,
  print("bs generado")
  n = math.ceil(math.sqrt(p))
  gs_calc(bs_dic, p, alpha, beta, n,16)

if __name__ == "__main__":
    main()

