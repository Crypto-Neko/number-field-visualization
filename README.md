# Quadratic Field Analaysis

### Overview

The purpose of this project is to systematically study the properties of real and complex number fields and record them in a JSON file. I wrote the code while I was taking a graduate course in algebraic number theory and I was interested in seeing what patterns there might be in the invariants, specifically in the size of the regulator. The results have been interesting, and upon showing them to my professor, I was able to gain some insight into what was going on.

### Explanation of Files

1. **`main.py`**: This is the main file, which allows the user to enter the number of fields to compute, and runs plot_invariants from `plot_invariants.py` if the number entered is less than 10000. Resulting data is converted to a JSON file and saved to a file.
2. **`computer_invariants.py`**: Computes the values of d, the discriminant, class number, fundamental unit, regulator, and Minkowski bound of a number field.
3. **`plot_invariants.py`**: Plots the values of d, the discriminant, class number, fundamental unit, regulator, and Minkowski bound of a number field. Stores plots to file.
4. **`track_fu_spikes.py`**: This module is meant to track fields where the size of the fundamental unit increases greatly between two fields. It plots the log of the spikes and saves the plot to a file.
5. **`first_100k_real_fields.json`**: The data from the first 100k real quadratic fields, i.e. Q(sqrt(d)) for the first 100k squarefree integers d.
6. **`first_100k_imaginary_fields.json`**: The data from the first 100k imaginary quadratic fields, i.e. Q(sqrt(-d)) for the first 100k squarefree integers d.
7. **`invariants_data.json`**: The output of the program when `main.py` is run.


