import lineareg as lin
import numpy as np
import calc_stats as cs

def print_lin(x: np.ndarray,y: np.ndarray):
    a, b = lin.create_lin_model(x, y)
    s_y, s_a, s_b = lin.calc_std(x, y, a, b)
    print("Values of linear Regression (y = a*x + b):")
    print("a = " + str(a))
    print("b = " + str(b))
    print("-------------------------------------------")
    print("Values for a:")
    print("s_a = " + str(s_a))
    print("t * s_a = " + str(cs.return_T(0.95, len(x)-2) * s_a))
    print("(t* s_a) / |a| = " + str(cs.return_T(0.95, len(x)-2) * s_a / np.abs(a)))
    print("\nValues for b:")
    print("s_b = " + str(s_b))
    print("t * s_b = " + str(cs.return_T(0.95, len(x) - 2) * s_b))
    print("(t* s_b) / |b| = " + str(cs.return_T(0.95, len(x) - 2) * s_b / np.abs(b)))
    print("-------------------------------------------")
