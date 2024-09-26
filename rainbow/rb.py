import hashlib
import random
import ast

def reverse(hash: str) -> str:
    hash_value = ''.join(bin(int(char, 16))[2:].zfill(4) for char in hash)
    first_5_bits = int(hash_value[:15], 2)
    length = 4 + (first_5_bits % 6)
    remaining_bits = int(hash_value, 2)
    password = str(remaining_bits).zfill(10)[:length]
    
    # print(f"Hash: {hash}")
    # print(f"First 5 bits: {first_5_bits}")
    # print(f"Length: {length}")
    # print(f"Remaining bits: {remaining_bits}")    
    # print(f"Reverse: {password}")
    return password

def hash(data:str, num_bits=40):
  full = hashlib.sha1(data.encode()).hexdigest()
  hexa_words = num_bits // 4
  return full[:hexa_words]

def gen_table(width: int, deep: int) -> dict:
    table ={}
    while len(table) < deep:
      passwd = str(random.randrange(9999999))
      p = passwd
      for j in range(width):
          p = reverse(hash(p))
      table[hash(p)] = passwd
    print("Table generated", len(table))
    return table

passwd = "67325"
h = hash(passwd)
print(f"Password: {passwd}")
print(f"Hash of password {h}")

width= 1000
deep = 10000
try :
    raise Exception("Table not found")
    f_table = open('table.txt').read()
    table = ast.literal_eval(f_table)
except:
    print("Table not found, generating...")
    table = gen_table(width, deep)
    f_table = open('table.txt', 'w')
    f_table.write(str(table))
    f_table.close()
    
collision = False
hi= h
for i in range (width):
  if (hi in table):
    print("Collision!")
    collision = True
    break;
  hi = hash(reverse(hi))

if not collision:
  raise Exception("Collision no encontrada")

pwd = table[hi]
print(f"initial pwd:{pwd}")
while hash(pwd) != h:
  pwd = reverse(hash(pwd))

print(hi)
print(pwd)

print(f"Password original: {passwd}")
print(f"Hash del Password original: {hash(passwd)}")

print(f"Password encontrado: {pwd}")
print(f"Hash del Password encontrado: {hash(pwd)}")







