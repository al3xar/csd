import math
import time
from sympy import gcd, isprime
from egcd import egcd
from read_file import read_retos
import matplotlib.pyplot as plt
import pandas as pd


#t=47

def f(x:int,a:int,b:int,p:int,o,alpha,beta):
  xm = x % 3
  ai = a
  bi = b
  if (xm == 0):
    xi = pow(x,2,p)
    ai = 2*a % (p-1)
    bi = 2*b % (p-1)
  elif (xm == 1):
    bi = (b+1) % (p-1)
    xi = (beta*x) % p
  elif (xm == 2):
    xi = (alpha*x) % p
    ai = (a+1) % (p-1)
  else:
    raise ValueError("Error en f(x,a,b,p,o)")
  return xi,ai,bi

def pollard_rho(alpha,beta,p,o):
  a = b = aa = bb = 0
  i = x = xx = 1
  counter = 0
  while i < p:
    x, a, b = f(x,a,b,p,o,alpha,beta);
    # print (f"i = {i}, x = {x}, a = {a}, b = {b}")
    xx, aa, bb = f(xx,aa,bb,p,o,alpha,beta); xx, aa, bb = f(xx,aa,bb,p,o,alpha,beta);
    #print (f"i = {i}, xx = {xx}, aa = {aa}, bb = {bb}")
    if x == xx:
      if(gcd(b-bb,o) != 1):
        # print("No se puede calcular k, porque el mcd de b-bb y o no es 1")
        counter += 1
      else:
        g, j, y = egcd(b - bb, o)
        e = j % o
        k = (((aa - a) * e) % o)
        print("Encontrada k = ", k)
        return k, counter
    i += 1
  raise ValueError("No se ha encontrado k")


def create_graphs(time_marks: list):
  df = pd.DataFrame(time_marks, columns=["time"])
  df['reto'] = [f"Reto {i+1}" for i in range(len(time_marks))]  # Nombres de retos
  plt.figure(figsize=(10, 6))
  plt.bar(df['reto'], df['time'], color='blue', alpha=0.7, edgecolor='black')
  plt.title("Tiempos por Reto")
  plt.xlabel("Tallas")
  plt.ylabel("Tiempo (s)")
  plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje X
  plt.grid(axis='y', linestyle='--', alpha=0.6)
  plt.tight_layout()  # Ajustar para que las etiquetas no se corten
  plt.savefig('./resultados/bsgs.png')  # Guardamos la gráfica como 'bsgs.png'
  print("Gráfico guardado como 'bsgs.png'.")
  # Guardar los datos en un archivo CSV
  df.to_csv('./resultados/bsgs.csv', index=False)
  print("Datos guardados como 'bsgs.csv'.")


if __name__ == '__main__':
  retos = read_retos()
  time_marks = {}
  for i in range(0,len(retos)):
    reto = retos[i]
    if reto[0] not in time_marks:
      time_marks[reto[0]] = []
    if not isprime(reto[4]):
      #print(f"El orden {reto[4]} no es primo, se salta el reto")
      continue
    print("--------------------------------------------------")
    print(f"Reto {i}: {reto}")
    p = reto[1]
    alpha = reto[2]
    beta = reto[3]
    o = reto[4]
    # p = 971
    # o = 97
    # alpha =4
    # beta = 364

    try:
      t_start = time.time()
      k, counter  = pollard_rho(alpha,beta,p,o);
      time_marks[reto[0]].append(time.time() - t_start)
    except ValueError as e:
      print(e)
      continue
    print("counter = ",counter)
    if (beta == pow(alpha,k,p)):
      print(f"¡Éxito! Beta original: {beta} es igual a {pow(alpha,k,p)}")
    # else:
    #   raise ValueError("Error en el cálculo de k")

  # Calcula la media de cada una de las listas de time_marks y guardalo en una lista si no está vacía
  marks = [sum(time_marks[key]) / len(time_marks[key]) for key in time_marks if time_marks[key]]
  create_graphs(marks)
