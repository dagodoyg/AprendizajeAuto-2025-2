# Step 1: Generate some experimental data
import numpy as np
import matplotlib.pyplot as plt

N = 20

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

plt.plot(x_displacement, y_force, 'b.', label = 'data')
plt.xlabel('x', size = 15)
plt.ylabel('F', size = 15)
plt.title("Hooks's law: Force vs. Displacement")

# Build and train the model using Scikit-Learn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a linear regression model object
# Check https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
model = LinearRegression()

# Train the model using our data
# The .fit() method is where the 'learning' (Gradient Descent) happens!
model.fit(x_displacement, y_force) # USE ALL data
# Analyze the results

# Get the learned parameters (theta_0 and theta_1)
# .intercept_ is an array, so we take the first element
theta_0 = model.intercept_[0]
# .coef_ is a 2D array, so we access it with [0][0]
theta_1 = model.coef_[0][0]

print(f"The model has learned the following equation:")
print(f"Force = {theta_0:.3f} + {theta_1:.3f} * Displacement\n")

print(f"The estimated spring constant (k) is: {theta_1:.3f} N/m")
print(f"The true spring constant was: {k_true} N/m")

y_predicted = theta_0 + theta_1*x_displacement

plt.plot(x_displacement, y_predicted, 'g--', label = 'Predicted curve')

plt.legend()
plt.show()
