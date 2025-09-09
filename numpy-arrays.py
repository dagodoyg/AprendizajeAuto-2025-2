import numpy as np
from sklearn.linear_model import LinearRegression

x = np.random.rand(10)
mean = np.sum(x)/len(x)

with open("data.txt", "w") as file:
    file.write(str(mean))
