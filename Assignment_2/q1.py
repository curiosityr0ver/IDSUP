from typing import List
import math
Vector = List[float]
def add(v:Vector,w:Vector) -> Vector:
    return [v_i+w_i for v_i ,w_i in zip(v,w)]
v1=[2,3,4,5]
v2=[3,4,5,0]
v3=add(v1,v2)
print(v3)

def sub(v:Vector,w:Vector)-> Vector:
    return [v_i-w_i for v_i ,w_i in zip(v,w)]
v1=[2,3,4,5]
v2=[3,4,5,0]
v4=sub(v1,v2)
print(v4)

def mul(v:Vector,w:Vector)-> Vector:
    return [v_i*w_i for v_i ,w_i in zip(v,w)]
v1=[2,3,4,5]
v2=[3,4,5,0]
v4=mul(v1,v2)
print(v4)
