from Remez import *
# import sys
import matplotlib.pyplot as plt
import os

# func = sys.argv[1]
# a = sys.argv[2]
# b = sys.argv[3]
# degree = sys.argv[4]

x = symbols('x')
func = sin(x)
a = 0
b = 2*math.pi

for i in range(3,8,2):
    degree = i
    remez = Remez(func, a, b, degree)

    chebyshev_nodes = remez.find_chebyshev_nodes()
    print("Chebyshev nodes: ", chebyshev_nodes)
    E = symbols('x')
    b_vector, E = remez.enforce_oscillation_criteria(chebyshev_nodes, E)
    print("B vector (from b0 to bn): ", b_vector)
    print("Error E: ", E)
    polynomial = remez.form_polynomial(b_vector)
    print("First polynomial: ")
    print(np.poly1d(polynomial))

    if not os.path.isdir('output'):
        os.mkdir('output')
    output_path = 'output/remez_result{}.png'.format(degree)
    title = 'Remez algorithm result for degree {}'.format(degree)

    t = np.linspace(0, 2*math.pi, 400)
    y1 = polynomial(t)
    y2 = np.sin(t)
    plt.plot(t, y1, 'b', label='remez_algorithm')
    plt.plot(t, y2, 'r', label='actual_function')
    plt.legend()
    plt.title(title)
    plt.savefig(output_path)
    plt.show()
