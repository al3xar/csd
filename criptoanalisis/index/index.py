


from sympy import isprime, Matrix

# 8, 487, 33, 303, 243

alpha = 33
beta = 303
p = 487
o = 243

# Index Calculus algorithm

def index_calculus(alpha, beta, p, o):
    # Step 1: Find the smooth numbers
    smooth_numbers = []
    for i in range(2, p):
        if isprime(i):
            if pow(alpha, i, p) == beta:
                smooth_numbers.append(i)
    print("Smooth numbers: ", smooth_numbers)
    # Step 2: Find the relations
    relations = []
    for i in range(2, p):
        if isprime(i):
            for number in smooth_numbers:
                if pow(alpha, i, p) == pow(alpha, number, p):
                    relations.append((i, number))
    print("Relations: ", relations)
    # Step 3: Find the matrix
    matrix = []
    for i in range(0, len(relations)):
        row = []
        for j in range(0, len(relations)):
            row.append(pow(alpha, relations[i][0] * relations[j][1], p))
        matrix.append(row)
    print("Matrix: ", matrix)
    # Step 4: Find the null space
    A = Matrix(matrix)
    null_space = A.nullspace()
    print("Null space: ", null_space)
    # Step 5: Find the logarithms
    logarithms = []
    for i in range(0, len(null_space[0])):
        logarithms.append(null_space[0][i] % o)
    print("Logarithms: ", logarithms)
    return logarithms
  
  
  
index_calculus(alpha, beta, p, o)