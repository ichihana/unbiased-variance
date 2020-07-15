import numpy as np
import scipy as sp

x = np.array([1,2,3,4,5])
N = len(x)
sum_value = sp.sum(x)
mu = sum_value / N

sigma2 = sp.sum((x - mu) ** 2) / (N - 1)
print(sigma2)
