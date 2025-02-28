import numpy as np
import matplotlib.pyplot as plt
import math 

# Inverted CDF method: it is used for sampling elements from an arbitrary and not well defined distribution.
# generate data according an arbitrary distrivuition

#X = (np.randn(1,1e4).^2 + (3*randn(1,1e4)).^2) - 2*(rand(1,1e4))
N = 10000
X = np.random.randn(1,N)**2 + (3*np.random.randn(1,N)**2) -2*(np.random.rand(1,N))
X_transposed = X.transpose()
print(X)

#plotting an histogram of the data xlabel x y label count:

plt.hist(X_transposed, bins=100)
plt.xlabel('X')
plt.ylabel('Count')
plt.show()

#Getting data of the histogram:
counts, bins_count = np.histogram(X_transposed, bins=100)
pdf = counts / sum(counts)
cdf = np.cumsum(pdf)

plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.legend()
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.show()
plt.plot(bins_count[1:], cdf, label="CDF")
plt.xlabel("X")
plt.ylabel("Cumulative Probability")
plt.legend()
plt.show()

x_sorted = np.sort(X_transposed)

#Now we can use CDF to generate random samples from the distribution:
x_sampled = np.zeros(N)

for i in range(N):
    ro  = np.random.rand()
    idx_min = np.argmin(np.abs(cdf - ro))
    x_sampled[i] = x_sorted[idx_min]



print(x_sampled)
plt.hist(x_sampled, bins=100)
plt.xlabel('X')
plt.ylabel('Count')
plt.show()


# # empirical CDF from data:
# #sort the data
# X_sorted = np.sort(X_transposed)

# cdf_range = np.linspace(0,1,len(X_sorted))
# plt.plot(cdf_range,X_sorted )
# plt.xlabel('X')
# plt.ylabel('CDF')
# plt.show()



