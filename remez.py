import math
import numpy as np 
from scipy import linalg

class Remez():
    # For a given func in an interval [a,b] and a degree n of interpolating polynomial 
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n

    def find_chebyshev_nodes(self):
        chebyshev_nodes = []
        end_iteration = self.n + 1 # 0 to n+1 -> n+2 points
        for i in range(end_iteration):
            x = 0.5*(self.a+self.b) + 0.5*(self.b-self.a)*math.cos(((2*i-1)/(2*self.n))*math.pi)
            chebyshev_nodes.append(x)
        
        return chebyshev_nodes
    
    def enforce_oscillation_criteria(self, chebyshev_nodes, E):
        end_iteration = self.n + 1
        matrix_a = [[1] for i in range(end_iteration)]
        matrix_b = []
        for i in range(end_iteration):
            for j in range(1, self.n):
                matrix_a[i].append(chebyshev_nodes[i] ** j)
            matrix_a[i].append(E * ((-1)**i))
            # matrix_b[i] = solve_func(chebyshev_nodes[i])
        
        matrix_a = np.matrix(matrix_a)
        matrix_b = np.matrix(matrix_b)
        result = linalg.solve(matrix_a, matrix_b)

        return result

    # def solve_func(self, x):
        
    def form_polynomial(self, b_vector):
        b_vector.reverse() # get vector as [b_n, b_n-1 ... b_0]
        p = np.poly1d(b_vector)
        return p



# func = e**x
# a = 0
# b = 1
# n = 1


