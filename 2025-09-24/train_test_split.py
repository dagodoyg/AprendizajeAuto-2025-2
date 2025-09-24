import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

N = 100

# Let's assume the true spring constant k is 4.5 N/m
k_true = 4.5
np.random.seed(42) # for reproducibility

# Displacement (x) in meters. This is our feature X.
# The .reshape(-1, 1) is needed because scikit-learn expects 2D arrays for features.
xdata = np.linspace(0, 2, N)
x_displacement = xdata.reshape(-1, 1)

# Force (F) in Newtons. This is our target y.
# We'll calculate the true force and add some random "measurement noise"
noise = np.random.normal(0, 0.5, x_displacement.shape)
y_force = k_true * x_displacement + noise

#Split data
x_train, x_test, y_train, y_test = train_test_split(x_displacement, y_force, test_size=0.2, random_state=42)

#Regresoor
reg = SGDRegressor(
    max_iter=1000, alpha=0.0001, learning_rate='invscaling', random_state=42)

#Train and predict
sgd_regressor.fit(x_train, y_train)
y_pred = sgd_regressor.predict(X_test)

#Statistical measurements
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test,y_pred)
print('Statistical test')
print(f'mse = {mse}')
print(f'$R^2= {r2}$)')

plt.legend()
plt.show()
