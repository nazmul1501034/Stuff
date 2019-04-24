import math

def vector_add(u,v):
    return [u_1+v_1 for u_1,v_1 in zip(u,v)]

def vector_subtract(u,v):
    return [u_1-v_1 for u_1,v_1 in zip(u,v)]

def vector_dot(u,v):
    return sum(u_1*v_1 for u_1,v_1 in zip(u,v))

def scaler_multiply(c,u):
    return [c*u_1 for u_1 in u]

def squre_modulus(u):
    return vector_dot(u,u)

def vector_modulus(u):
    return math.sqrt(squre_modulus(u))

def distance(u,v):
    return vector_modulus(vector_subtract(u,v))
