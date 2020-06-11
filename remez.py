import math

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
    
    # def enforce_oscillation_criteria(self):



# func = e**x
# a = 0
# b = 1
# n = 1


