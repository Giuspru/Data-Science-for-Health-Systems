import numpy as np
import matplotlib.pyplot as plt


#Integration between 0 and 1 of: f(x) =  4*sqrt(1-x^2). It should be pi. 
#generate a random vector x o 10000 elements:
X = np.random.rand(100000)
X_squared = X**2

Y = 4*np.sqrt(1-X_squared)
pi = np.pi
computed_pi = np.mean(Y)
print("The real pi is: ", pi)
print("\nThe computed pi is: ", computed_pi)
print("\nThe error is: ", np.abs(pi-computed_pi))

