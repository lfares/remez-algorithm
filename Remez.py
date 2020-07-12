import math
import mpmath
import numpy as np 
from scipy import linalg
from sympy.abc import x
from sympy import *

class Remez():
    # For a given func in an interval [a,b] and a degree n of interpolating polynomial 
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n

    def find_chebyshev_nodes(self):
        chebyshev_nodes = []
        end_iteration = self.n + 2 # 0 to n+1 -> n+2 points
        for i in range(end_iteration):
            x = 0.5*(self.a+self.b) + 0.5*(self.b-self.a)*np.cos(((2*i-1)/(2*self.n))*math.pi)
            chebyshev_nodes.append(x)
        
        return chebyshev_nodes
    
    def enforce_oscillation_criteria(self, chebyshev_nodes, E):
        end_iteration = self.n + 2
        matrix_a = [[1] for i in range(end_iteration)]
        matrix_b = []
        for i in range(end_iteration):
            for j in range(1, self.n+1):
                matrix_a[i].append((chebyshev_nodes[i]-self.a) ** j)
            if i%2 == 0:   
                matrix_a[i].append(1)
            else:
                matrix_a[i].append(-1)
            matrix_b.append(self.solve_func(chebyshev_nodes[i]))
   
        matrix_a = np.array(matrix_a).astype(float)
        print(matrix_a)
        matrix_b = np.array(matrix_b).astype(float)
        print(matrix_a)
        print(matrix_b)
        result = linalg.solve(matrix_a, matrix_b)

        return list(result[:(self.n+1)]), result[self.n+1]

    def solve_func(self, x_value):
        result = self.func.subs(x, x_value)
        return result
        
    def form_polynomial(self, b_vector):
        b_vector.reverse() # get vector as [b_n, b_n-1 ... b_0]
        p = np.poly1d(b_vector, variable='x')
        return p
    
    def get_error_func_roots(self, y, t):
        roots = []
        for i in range(1, (len(y)-1)):
            if ((y[i-1] > 0 and y[i+1] < 0) or (y[i-1] < 0 and y[i+1] > 0)) and i%2 == 0:
                roots.append(t[i])
        
        return roots

    def get_new_chebyshev_nodes(self, y, t, roots):
        new_chebyshev_nodes = []
        max_abs_value = abs(y[0])
        max_abs_value_index = 0
        final_index = 0
        for root in roots: 
            for i in range(final_index, len(y)):
                if max_abs_value < abs(y[i]):
                    max_abs_value = abs(y[i])
                    max_abs_value_index = i
                if t[i] == root:
                    new_chebyshev_nodes.append(t[max_abs_value_index])
                    final_index = i
                    max_abs_value = abs(y[i])
                    max_abs_value_index = i
                    break
        
        for i in range(final_index, len(y)):
            if max_abs_value < abs(y[i]):
                max_abs_value_index = i
        new_chebyshev_nodes.append(t[max_abs_value_index])

        return new_chebyshev_nodes
        


