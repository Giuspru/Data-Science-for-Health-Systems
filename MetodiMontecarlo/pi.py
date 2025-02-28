import numpy as np 
import matplotlib.pyplot as plt

#Computing pi using a montecarlo numeric integration method:

N = 100000

#plot a circular arc:
theta = np.linspace(0,(np.pi)/2,100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x,y)
#plot a square with the side of 1:
plt.plot([0,1,1,0,0],[0,0,1,1,0])
plt.axis('equal')
plt.show()

#Montecarlo Loop:
count = 0 
for i in range(N):
    u1 = np.random.uniform(0,1)
    u2 = np.random.uniform(0,1)

    if u1**2 + u2**2 < 1:
        count += 1

print(count)
pi_estimate = count/N*4
p_error = pi_estimate - np.pi
print("pi estimated:", pi_estimate)
print("\npi error :", p_error)



