import hashlib
import random
import ast

def reverse(hash: str) -> str:
    hash_value = ''.join(bin(int(char, 16))[2:].zfill(4) for char in hash)
    first_5_bits = int(hash_value[:15], 2)
    length = 6 + (first_5_bits % 14)
    remaining_bits = int(hash_value, 2)
    password = str(remaining_bits).zfill(10)[:length]
    
    # print(f"Hash: {hash}")
    # print(f"First 5 bits: {first_5_bits}")
    # print(f"Length: {length}")
    # print(f"Remaining bits: {remaining_bits}")    
    # print(f"Reverse: {password}")
    return password

def hash(data:str, num_bits=60):
  full = hashlib.sha1(data.encode()).hexdigest()
  hexa_words = num_bits // 4
  return full[:hexa_words]

def gen_table(width: int, deep: int) -> dict:
    table ={}
    while len(table) < deep:
        passwd = str(random.randrange(99999999999999999999))
        p = passwd
        for j in range(width):
            h = hash(p)
            if h in table:
                break
            p = reverse(h)
        table[hash(p)] = passwd
    print("Table generated", len(table))
    return table

passwd = "67325"
h = hash(passwd)
print(f"Password: {passwd}")
print(f"Hash of password {h}")
# print("Reverse of hash:", reverse(hash("1234")))
# print("Reverse of hash:", reverse(hash("12345")))
# print("Reverse of hash:", reverse(hash("123456")))
# print("Reverse of hash:", reverse(hash("1234567")))
# print("Reverse of hash:", reverse(hash("12345678")))
# print("Reverse of hash:", reverse(hash("123456789")))
# print("Reverse of hash:", reverse(hash("1234567890")))
# print("Reverse of hash:", reverse(hash("12345678901")))
# print("Reverse of hash:", reverse(hash("123456789012")))
# print("Reverse of hash:", reverse(hash("1234567890123")))

width= 100
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
    
hi = h
for i in range(width):
    if hi in table:
        print(f"Found hash: {hi}")
        print(f"Found password: {table[hi]}")
        break
    hi = hash(reverse(hi))
    
print(f"Password index: {i}")
if i == width:
    # throw exception
    raise Exception("Password not found")

pwd = table[hi]

print(f"Password line: {pwd}")

for j in range(width):
    if h == hash(pwd):
        print(f"The password is: {pwd}")
        break
    pwd = reverse(hash(pwd))
    
print(f"The password is: {pwd}")
print(f"The hash of the generated password is: {hash(pwd)}")






