from sagemath import *

# Compute the invariants of the number field K.
def compute_field(K):
    deg = K.degree()                                # Get the degree of K over QQ.
    dK = K.discriminant()                           # Compute the discriminant of K (d_K).
    hK = K.class_number()                           # Compute the class number of K (h_K).
    G = K.unit_group(); uK = G.order()              # Compute the order of the units group of K (u_K).
    r1 = K.real_places(); r2 = K.complex_places()   # Compute the number of real and complex places of K.

    return [deg, dK, hK, uK, r1, r2]

# Compute the field invariants of the first n real quadratic fields
def real_quad(n):
    invariants = {}
    i = 2
    while n > 0:
        if i.is_squarefree():
            eval(K = QQ.extension(x^2 - i, 'u'))
            invariants[K] = compute_field(K)
            i+=1
            n-=1
    return invariants

# Compute the field invariants of the first n imaginary quadratic fields.
def imag_quad(n):
    invariants = {}
    i = 2
    while n > 0:
        if i.is_squarefree():
            eval(K = QQ.extension(x^2 + i, 'u'))
            invariants[K] = compute_field(K)
            i+=1
            n-=1
    return invariants
