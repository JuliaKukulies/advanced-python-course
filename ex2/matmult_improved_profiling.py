# Program to multiply two matrices, improved performance (Exercise 2)

import random

N = 250

@profile
def create_matrix(N):
    # NxN matrix
    X =  [[random.randint(0, 100) for i in range(N)] for j in range(N)]
    return X

@profile
def create_larger_matrix(N):
    # Nx(N+1) matrix
    Y = [[random.randint(0, 100) for i in range(N+1)] for j in range(N)]
    return Y

@profile
def multiply_matrices(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

@profile
def print_matrix(result):
    for r in result:
        print(r)

@profile
def __main__(N):
    X= create_matrix(N)
    Y= create_larger_matrix(N)
    result= multiply_matrices(X,Y)
    print_matrix(result)


# call main program 
__main__(N)






