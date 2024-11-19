from sage.all import *
import matplotlib.pyplot as plt
import math

def plot_fu_spikes(invariants):
    d_list = []
    fu_vals = []
    fu_spikes = []
    
    for K in invariants.keys():
        d_list.append((K.absolute_generator())**2)
        fu_vals.append(invariants[K][3].abs())
    
    for i in range(len(fu_vals)-1):
        if fu_vals[i+1] > 10 * fu_vals[i]:
            fu_spikes.append([d_list[i+1], fu_vals[i+1]])

    fu_spikes_d = []
    fu_spikes_fu = []
    for d, fu in fu_spikes:
        fu_spikes_d.append(d)
        fu_spikes_fu.append(math.log(fu))

    plt.plot(fu_spikes_d, fu_spikes_fu, marker='o', linestyle='-', label='fu')
    plt.xlabel('Value of d (K = Q(sqrt(d)))')
    plt.ylabel('Log of the Norm of the Fundamental Unit of K')
    plt.title('Spikes in the Norm of the Fundamental Unit of K wrt d, where K = Q(sqrt(d))')
    plt.legend()
    plt.grid(True)
    plt.savefig("fu_spikes_vs_d.png")
    plt.show()

    return fu_spikes
