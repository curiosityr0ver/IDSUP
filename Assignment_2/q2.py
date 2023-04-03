from typing import List
from typing import Callable
Matrix = List[List[float]]
Vector = List[float]
def make_matrix(num_rows:int,num_cols:int,
entry_fn:Callable[[int,int],float])-> Matrix:
    return[[entry_fn(i,j)
    for j in range(num_cols)]
    for i in range(num_rows)]
    
def identity_matrix(n:int)->Matrix:
    return make_matrix(n,n,lambda i,j:1 if i==j else 0)
res=identity_matrix(3)
print(res)

def matrix1(n:int)->Matrix:
    return make_matrix(n,n,lambda i,j:i+j)
res2=matrix1(4)
print(res2)

def get_row(M,r):  
    return M[r]
res3=get_row(matrix1(4),1)
print(res3)

def get_col(M,j):
    return [M[r][j] for r in range(len(M))]
res4=get_col(matrix1(4),1)
print(res4)