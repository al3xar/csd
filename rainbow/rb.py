import hashlib
import string

domain = string.ascii_lowercase + string.ascii_uppercase + string.digits

def hash(data,num_bits=40):
  full = hashlib.sha1(data.encode()).hexdigest()
  hexa_words = num_bits // 4
  return full[:hexa_words]

def reverse(hash:str, num_bits=40):
  block_size=4
  bin_hash= bin(int(hash,16))[2:]
  num_blocks = [bin_hash[i:i+block_size] for i in range(0, len(bin_hash), block_size)]
  digits = [str(int(block, 2) % 10) for block in num_blocks]
  result = "".join(digits)
  return result

passwd="1234"
h = hash(passwd)
print(f"Contraseña: {passwd}")
print(f"Hash de {passwd} es {hash(passwd)}")
print(f"El reverso del {h} es {reverse(h)}")

width = 100
deep = 100

rainbow_table = {}

for i in range(deep):
  line_password = str(i)
  line_hash=""
  for j in range(width):
    line_hash = hash(reverse(hash(line_password)))
  rainbow_table[line_hash] = line_password

# print(rainbow_table)
print("Tabla generada")

collision = False
hi= h
for i in range (width):
  if (hi in rainbow_table):
    print("Collision!")
    collision = True
    break;
  hi = hash(reverse(hi))

if not collision:
  raise Exception("Collision no encontrada")

pwd = rainbow_table[hi]
print(f"initial pwd:{pwd}")
while hash(pwd) != h:
  pwd = reverse(hash(pwd))

print(hi)
print(pwd)
