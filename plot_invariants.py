from sage.all import *
import matplotlib.pyplot as plt
import numpy as np

# Produce plots comparing the invariants of each field
def plot_invariants(invariants):
    # Define lists for each invariant to be plotted
    d_list = []
    dK_list = []
    hK_list = []
    fu_list = []
    rK_list = []
    mb_list = []
    
    # Populate the lists with the invariants from the invariants dict
    for K in invariants.keys():
        d_list.append(invariants[K][0])
        dK_list.append(invariants[K][1])
        hK_list.append(invariants[K][2])
        fu_list.append(log(invariants[K][3].abs()))
        rK_list.append(invariants[K][4])
        mb_list.append(invariants[K][5])

    # Use a NumPy array to filter outliers
    d_array = np.array(d_list)
    dK_array = np.array(dK_list)
    hK_array = np.array(hK_list)
    fu_array = np.array(fu_list)
    rK_array = np.array(rK_list)
    mb_array = np.array(mb_list)

    
    # Compute the 90th percentile of the data
    upper_bound = np.percentile(fu_array, 99.9)

    # Use a mask to filter the outliers for better visualization
    # mask = fu_array <= upper_bound
    mask = fu_array <= 100*upper_bound
    filtered_d_list = d_array[mask]
    filtered_dK_list = dK_array[mask]
    filtered_hK_list = hK_array[mask]
    filtered_fu_list = fu_array[mask]
    filtered_rK_list = rK_array[mask]
    filtered_mb_list = mb_array[mask]

    # Plot the invariants wrt abs(alpha)
    # Note: Not plotting d_K because it is trivial to compute and analyze
    # plt.plot(filtered_d_list, filtered_dK_list, marker='o', linestyle='-', label='d_K')
    plt.plot(filtered_d_list, filtered_hK_list, marker='*', linestyle='-', label='h_K')
    plt.plot(filtered_d_list, filtered_fu_list, marker='+', linestyle='-', label='log(abs(fu))')
    plt.plot(filtered_d_list, filtered_rK_list, marker=',', linestyle='-', label='R_K')
    plt.plot(filtered_d_list, filtered_mb_list, marker='s', linestyle='-', label='MB')

    plt.xlabel('Value of d (K = Q(sqrt(d)))')
    plt.ylabel('Magnitude of value')
    plt.title('Field Invariants wrt d, where K = Q(sqrt(d))')
    plt.legend()
    plt.grid(True)
    plt.savefig("invariants_vs_d.png")
    plt.show()
