from Remez import *
import sys

func = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]
degree = sys.argv[4]

remez = Remez(func, a, b, degree)

chebyshev_nodes = remez.find_chebyshev_nodes()
E = int
b_vector, E = remez.enforce_oscillation_criteria(chebyshev_nodes, E)
polynomial = remez.form_polynomial(b_vector)

