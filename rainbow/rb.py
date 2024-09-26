import hashlib
import random
import ast

def reverse(hash: str) -> str:
    return f"{int(hash, 16) % 10000}"

def hash(data:str, num_bits=40):
  full = hashlib.sha1(data.encode()).hexdigest()
  hexa_words = num_bits // 4
  return full[:hexa_words]

def gen_table(width: int, deep: int) -> dict:
    table ={}
    while len(table) < deep:
        passwd = f"{random.randint(0, 9999)}"
        p = passwd
        for _ in range(width):
            h = hash(p)
            p = reverse(h)
        table[h] = passwd
    print("Table generated", len(table))
    return table

def search_collision(table,width):
    hi = h
    found = False
    for i in range(width):
        if hi in table:
            print(f"Colision encontrada en index {i}, buscando hash en linea...")
            trace_collision(table, hi)
            found = find_original_hash(table,hi)
            if found:
                break;
        hi = hash(reverse(hi))
    if not found:
        raise Exception("Password not found")

def find_original_hash(table, hi):
    pwd = table[hi]
    hp = hash(pwd)
    while h != hp:
        if hp == hi:
            print(f"Falso positivo, seguimos buscando...")
            return False
        hp = hash(pwd)
        pwd = reverse(hp)
    print(f"HASH ENCONTRADO: {hp}")
    print(f"CONSTRASEÑA EQUIVALENTE: {pwd}")
    return True

def trace_collision(table, hi):
    hp=h
    print("COLLISION TRACE")
    print(f"Found hash: {hi}")
    print(f"Found password: {table[hi]}")
    while hp != hi:
        pp = reverse(hp)
        hp= hash(pp)
        print(f" reverse: {pp}", end=" ➜ ")
        print(f" hash {hp}", end=" ➜ ")

width= 10
deep = 1000
passwd = "4321"
h = hash(passwd)

print(f"Password: {passwd}")
print(f"Hash of password {h}")

try :
    f_table = open('table.txt').read()
    table = ast.literal_eval(f_table)
except:
    print("Table not found, generating...")
    table = gen_table(width, deep)
    f_table = open('table.txt', 'w')
    f_table.write(str(table))
    f_table.close()
    
search_collision(table,width)
