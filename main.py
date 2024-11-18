from sage.all import *
from compute_invariants import *
from plot_invariants import *

def main(n=-1):
    if n == -1:
        n = int(input("Enter the number of fields to compare: "))
        while not (isinstance(n, int)) and not (n > 0):
            n = int(input("Input not accepted. Enter 0 for real and 1 for imaginary: "))

    invariants = compute_invariants(n)        
    plot_invariants(invariants)

#### MAIN FUNCTION CODE ####
if __name__ == "__main__":
    main()
