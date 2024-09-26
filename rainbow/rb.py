import hashlib
import random
import ast

def reverse(hash: str) -> str:
    hash_value = ''.join(bin(int(char, 16))[2:].zfill(4) for char in hash)
    first_5_bits = int(hash_value[:15], 2)
    length = 6 + (first_5_bits % 14)
    remaining_bits = int(hash_value, 2)
    password = str(remaining_bits).zfill(10)[:length]
    return password

def hash(data:str, num_bits=40):
  full = hashlib.sha1(data.encode()).hexdigest()
  hexa_words = num_bits // 4
  return full[:hexa_words]

def gen_table(width: int, deep: int) -> dict:
    table ={}
    while len(table) < deep:
        repeated = False
        passwd = str(random.randint(99999,99999999999999999999))
        p = passwd
        for j in range(width):
            h = hash(p)
            if h in table:
                repeated = True
                break
            p = reverse(h)
        if repeated: 
            continue
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
        # throw exception
        raise Exception("Password not found")

def find_original_hash(table, hi):
    pwd = table[hi]
    hp = hash(pwd)
    while h != hp:
        if hp == hi:
            print(f"Linea incorrecta, seguimos buscando...")
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
    print(f"Original passwd: {passwd} ➜")
    print(f"Original hash: {hp} ➜")
    while hp != hi:
        pp = reverse(hp)
        hp= hash(pp)
        print(f"reverse ➜ {pp}")
        print(f"hash ➜ {hp}")



width= 1000
deep = 1000000
passwd = "321321321"
h = hash(passwd)

print(f"Password: {passwd}")
print(f"Hash of password {h}")

try :
    # raise Exception("Table not found")
    f_table = open('table.txt').read()
    table = ast.literal_eval(f_table)
except:
    print("Table not found, generating...")
    table = gen_table(width, deep)
    f_table = open('table.txt', 'w')
    f_table.write(str(table))
    f_table.close()
    


search_collision(table,width)





print(f"Password line: {pwd}")

print("SEARCH TRACE")

    
print(j)
print(f"The password is: {pwd}")
print(f"The hash of the generated password is: {hp}")






