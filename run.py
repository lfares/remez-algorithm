from Remez import *
# import sys
import matplotlib.pyplot as plt
import os

# func = sys.argv[1]
# a = sys.argv[2]
# b = sys.argv[3]
# degree = sys.argv[4]

# Check for output path to put graphs
if not os.path.isdir('output'):
    os.mkdir('output')
output_path = 'output/'

# Define values
func = sin(x)
func_derivative = cos(x)
a = 0
b = 2*math.pi
degree = 4
i = 0
loop = True

# Initiate remez funcs and pass throught them
remez = Remez(func, a, b, degree)

while loop == True:
    #######   START STEP 1  ########
    if i == 0:
        chebyshev_nodes = remez.find_chebyshev_nodes()
    else:
        chebyshev_nodes = remez.get_new_chebyshev_nodes(y_error, t_error, roots)
    print("Chebyshev nodes: ", chebyshev_nodes)

    E = symbols('x')
    b_vector, E = remez.solve_system(chebyshev_nodes, E)
    print("B vector (from b0 to bn): ", b_vector)
    print("Error E: ", E)

    polynomial = remez.form_polynomial(b_vector)
    print("Polynomial for interaction {}: ".format(i))
    print(np.poly1d(polynomial))

    # Plot error function
    roots = []
    t_error = np.linspace(0, 2*math.pi, 1000)
    y_error = np.sin(t_error) - polynomial(t_error)
    plt.plot(t_error, y_error, 'b')
    plt.title('Função erro para iteração {}'.format(i))
    plt.xlabel('x')
    plt.ylabel('e(x) = f(x) - p(x)')
    plt.savefig(output_path+'error_function_{}.png'.format(i))
    plt.show()

    # Plot graphs
    t = np.linspace(0, 2*math.pi, 400)
    y1 = polynomial(t)
    y2 = np.sin(t)
    plt.plot(t, y1, 'b', label='aproximação de remez')
    plt.plot(t, y2, 'r', label='função real')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Resultado do algoritmo de Remezes para iteração {}'.format(i))
    plt.savefig(output_path+'remez_result_{}.png'.format(i))
    plt.show()

    # Get E_min and E_max to test end of iteration
    E_min = min(y_error)
    E_max = max(y_error)
    print("E min: ", E_min)
    print("E_max: ", E_max)
    if math.isclose(abs(E_max), abs(E_min), rel_tol=0.001):
        loop = False 

    #######   START STEP 2  ########
    roots = remez.get_error_func_roots(y_error, t_error)
    print("Error function roots: ", roots)

    i += 1

    
