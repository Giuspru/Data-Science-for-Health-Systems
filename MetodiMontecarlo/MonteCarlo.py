import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import random

#modello da simulare Y = x1 * x2

#Numero di iterazioni:
n = 100000
sqrn = int(math.sqrt(n))

#Grandezze di ingresso:
x1 = 3
u1 = 0.1
a1 = x1 - u1
b1 = x1 + u1

X1 = np.random.uniform(a1,b1,size=(n,1))
#print(X1)
x2 = 4.15
u2 = 0.05 
a2 = x2 - u2
b2 = x2 + u2

X2 = np.random.uniform(a2,b2,size=(n,1))
#print(X2)

#plotting histogram of X1
plt.hist(X1, bins=70, density=True)
plt.xlabel('Value x1')
plt.ylabel('Count')
plt.title('Histogram of X1')
plt.show()

#Plotting histoogram of X2
plt.hist(X2, bins=70, density=True)
plt.xlabel('Value x2')
plt.ylabel('Count')
plt.title('Histogram of X2')
plt.show()


#Grandezza di uscita:
Y = X1 * X2
print(Y.shape)

#Plotting histogram of Y
plt.hist(Y, bins=70, density=True)
plt.xlabel('Value y')
plt.ylabel('Count')
plt.title('Histogram of Y')
plt.show()


y_sorted = np.sort(Y)

plt.plot(y_sorted, np.linspace(0,1,n,endpoint=True))
plt.show()






