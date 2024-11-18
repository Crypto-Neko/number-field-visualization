from sage.all import *
from compute_invariants import *
from visualization import *

def main(n=-1):
    if n == -1:
        n = input("Enter the number of fields to compare: ")
        while not (n.isinstance(int)) and not (n > 0):
            n = input("Input not accepted. Enter 0 for real and 1 for imaginary: ")

    invariants = compute_invariants(n)        
    plot_invariants(invariants)

#### MAIN FUNCTION CODE ####
if __name__ == "__main__":
    main()
