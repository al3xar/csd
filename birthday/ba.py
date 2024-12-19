import hashlib
import numpy
import time

def split_text(text, num_chunks=40):
  length = len(text)
  chunk_size= length // num_chunks
  remainder  =  length % num_chunks
  chunks = []
  start = 0

  for i in range(num_chunks):
    end = start + chunk_size
    if i == num_chunks - 1:
      end += remainder # Last chunk is bigger
    chunks.append(text[start:end])
    start = end
  return chunks

def hash(data,num_bits=40):
  full = hashlib.sha1(data.encode()).hexdigest()
  hexa_words = num_bits // 4
  return full[:hexa_words]

def transform_text(chunks, binary_index):
  hidden_char = '\x01'
  transformed_text = ""
  reversed_binary = binary_index[::-1]
  for j in range(len(binary_index)):
    chunk = chunks[j]
    if reversed_binary[j] == '1':
      chunk += hidden_char
    transformed_text += chunk
  return transformed_text

def white_diccionary(white_chunks, num_bits=40, t= 20):
  diccionary = {}
  limit = numpy.power(2,t)
  for i in range(limit):
    binary_index = bin(i)[2:].zfill(t);
    transformed_text = transform_text(white_chunks, binary_index)
    hash_value = hash(transformed_text,num_bits)
    diccionary[hash_value] = binary_index;
  return diccionary

def black_collision(white_diccionary, white_chunks, black_chunks, num_bits=40):
  t_start = time.time();
  i = 0
  max_attempts = numpy.power(2,num_bits)
  while i < max_attempts-1:
    binary_index = bin(i)[2:].zfill(num_bits);
    transformed_text = transform_text(black_chunks, binary_index)
    hash_value = hash(transformed_text,num_bits)
    if hash_value in white_diccionary:
      print(f"¡Colisión encontrada después de {i} intentos!")
      print(f"Tiempo en encontrar la colisión: {time.time() - t_start} segundos")
      print(f"White binary 1: {white_diccionary[hash_value]}")
      print(f"Black binary: {binary_index}")
      print(f"Hash: {hash_value}")
      print(f"Black text: {transformed_text}")
      print("White text:")
      print(transform_text(white_chunks,white_diccionary[hash_value]))
      print("Black text:")
      print(transformed_text)
      return white_diccionary[hash_value], binary_index;
    i +=1
  print("No hay colision xd")
  return 0, 0;

num_bits=49
white_text = "Buenas tardes alumnos, la fecha de la entrega de este trabajo se mantiene para el 11 de Noviembre pese a que os hayais pasado la semana quitando barro en vuestras casa y en la de vuestros familiares. Un saludo." # open(white).read()
black_text = "Buenos días pupilos míos, el trabajo se aplazará al 15 de noviembre. Ahora que hemos vuelto a la normalidad, os doy una semana más para que podáis entregar los 2 ejercicios a tiempo. Un fuerte abrazo y ánimo." # open(black).read()
white_chunks = split_text(white_text,num_bits//2)
black_chunks = split_text(black_text,num_bits)
start_time = time.time()
wd = white_diccionary(white_chunks,num_bits,num_bits//2)
print(f"Tiempo en crear el diccionario: {time.time() - start_time} segundos")
b_white, b_black = black_collision(wd, white_chunks,black_chunks,num_bits)

