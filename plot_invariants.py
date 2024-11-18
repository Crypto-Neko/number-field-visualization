from sage.all import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Produce plots comparing the invariants of each field
def plot_invariants(invariants):
    # Define lists for each invariant to be plotted
    alpha_abs_list = []
    dK_list = []
    hK_list = []
    fu_list = []
    rK_list = []
    
    # Populate the lists with the invariants from the invariants dict
    for K in invariants.keys():
        alpha = K.absolute_generator(); alpha_abs_list.append(alpha.abs())
        dK_list.append(invariants[K][0])
        hK_list.append(invariants[K][1])
        fu_list.append(eval(abs(invariants[K][2])))
        rK_list.append(invariants[K][3])

    # Plot the invariants wrt abs(alpha)
    plt.plot(alpha_abs_list, dK_list, marker='o', linestyle='-', label='d_K')
    plt.plot(alpha_abs_list, hK_list, marker='*', linestyle='-', label='h_K')
    plt.plot(alpha_abs_list, fu_list, marker='+', linestyle='-', label='abs(u)')
    plt.plot(alpha_abs_list, rK_list, marker='s', linestyle='-', label='R_K')

    plt.xlabel('Absolute Value of Alpha (K = Q(alpha))')
    plt.ylabel('Magnitude of value')
    plt.title('Field Invariants wrt abs(alpha), where K = Q(alpha)')
    plt.legend()
    plt.grid(True)
    plt.savegif("abs_alpha_vs_dK.png")
    plt.show()
