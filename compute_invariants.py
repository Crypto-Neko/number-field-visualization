from sage.all import *

# Compute the invariants of the number field K.
def compute_field(K):
    dK = K.discriminant()                           # Compute the discriminant of K (d_K)
    hK = K.class_number()                           # Compute the class number of K (h_K)
    fu = K.units()[0]                               # Compute the fundamental unit of K
    rK = K.regulator()                              # Compute the regulator of K (R_K)
    
    print([dK, hK, fu, rK])
    return [dK, hK, fu, rK]

# Compute the field invariants of the first n real quadratic fields
def compute_invariants(n):
    invariants = {}
    i = 2
    while n > 0:
        if is_squarefree(i):
            x = polygen(ZZ, 'x')
            K = NumberField(x**Integer(2) - i, names=('u',))
            invariants[K] = compute_field(K)
            n-=1
        i+=1
    return invariants
