# Abre el fichero en modo lectura
from typing import List, Tuple

def read_retos() -> List[Tuple[int, int, int, int, int]]:
  with open('RetosDL3.txt', 'r') as file:
      lines = file.readlines()
  # Cada reto tiene la siguiente estructura:
  #
  # # n, m, alfa, beta, orden
  retos: List[Tuple[int, int, int, int, int]] = []
  for line in lines:
      # if line has a# skip it
      if line.startswith("#"):
          continue
      print(line.strip())
      # Split the line by commas
      n, m, alfa, beta, orden = map(int, line.strip().split(","))
      # guardalo en la lista como si fuera una struct
      retos.append((n, m, alfa, beta, orden))
  return retos

