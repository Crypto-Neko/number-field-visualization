from sage.all import *
from compute_invariants import *
from visualization import *

def main(n=-1, im=-1):
    if n == -1 or im == -1:
        n = input("Enter the number of fields to compare: ")
        while not (n.isinstance(int)) and not (n > 0):
            n = input("Input not accepted. Enter 0 for real and 1 for imaginary: ")
        im = input("Enter 0 for real and 1 for imaginary: ")
        while not (im in [0, 1]):
            im = input("Input not accepted. Enter 0 for real and 1 for imaginary: ")
    if im == 0:
        invariants = real_quad(n)
    elif im == 1:
        invariants = imag_quad(n)
        
    visualize(invariants, im)

#### MAIN FUNCTION CODE ####
if __name__ == "__main__":
    main()
