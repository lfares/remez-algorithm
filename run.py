from Remez import *
# import sys
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# func = sys.argv[1]
# a = sys.argv[2]
# b = sys.argv[3]
# degree = sys.argv[4]

x = symbols('x')
func = cos(x)
a = 0
b = 1
degree = 2

remez = Remez(func, a, b, degree)

chebyshev_nodes = remez.find_chebyshev_nodes()
print("Chebyshev nodes: ", chebyshev_nodes)
E = symbols('x')
b_vector, E = remez.enforce_oscillation_criteria(chebyshev_nodes, E)
print("B vector (from b0 to bn): ", b_vector)
print("Error E: ", E)
polynomial = remez.form_polynomial(b_vector)
print("First polynomial: ", np.poly1d(polynomial))

t = np.linspace(0, 2*math.pi, 400)
y1 = polynomial(t)
y2 = np.cos(t)
plt.plot(t, y1, 'b')
plt.plot(t, y2, 'r')
plt.show()