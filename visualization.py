from sage.all import *
import matplotlib.pyplot as plt

# Produce plots comparing the invariants of each field.
def visualize(invariants, im):
    alpha_abs_list = []
    dK_list = []
    hK_list = []
    uK_list = []
    
    for K in invariants.keys():
        alpha = K.absolute_generator(); alpha_abs_list.append(alpha.abs())
        dK_list.append(invariants[K][0])
        hK_list.append(invariants[K][1])
        uK_list.append(invariants[K][2])

    plt.plot(alpha_abs_list, dK_list, marker='o')
    plt.xlabel('Absolute Value of Alpha (K = Q(alpha))')
    plt.ylabel('Value of dK')
    plt.title('dK vs the Absolute Values of alpha (K = Q(alpha))')
    plt.savegif("abs_alpha_vs_dK.png")

    plt.plot(alpha_abs_list, hK_list, marker='o')
    plt.xlabel('Absolute Value of Alpha (K = Q(alpha))')
    plt.ylabel('Value of hK')
    plt.title('hK vs the Absolute Values of alpha (K = Q(alpha))')
    plt.savegif("abs_alpha_vs_hK.png")

    plt.plot(alpha_abs_list, dK_list, marker='o')
    plt.xlabel('Value of dK')
    plt.ylabel('Value of hK')
    plt.title('hK vs dK')
    plt.savegif("dK_vs_hK.png")
