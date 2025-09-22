# Step 1: Generate some experimental data
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D projection

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

def step(theta_0:float, theta_1:float, N:int = 1, alpha: float = 0.1, verbose:bool = False) -> (float, float):
    # util function to print
    mylog = lambda msg: print(msg) if verbose else None
    ytheo = k_true * x_displacement

    for ii in np.arange(0, N):
        mylog("Prediction with full data")
        ypred = theta_0 + theta_1*x_displacement

        mylog("Computing loss")
        error = ypred-ytheo
        loss = np.power(error, 2).sum()/2
        mylog(f"{loss=}")

        mylog("Computing the gradients")
        grad_0 = error.mean()
        grad_1 = (error*x_displacement).mean()
        mylog(f"{grad_0=}, {grad_1=}")

        mylog("Improving paramether estimation")
        # NOTE: learning rate hyper paramemeter alpha
        theta_0 = theta_0 - alpha*grad_0
        theta_1 = theta_1 - alpha*grad_1
        mylog(f"{theta_0=}, {theta_1=}")

        mylog("")

    return theta_0, theta_1

theta_0 = 1.0
theta_1 = 1.0

# Params
nums = range(1,1001,10)
alphas = np.linspace(0.01, 0.9, 10) 
theta0_coords = []
theta1_coords = []

for n in nums:
    for a in alphas:
        p0, p1 = step(theta_0, theta_1, N=n, alpha=a, verbose=False)
        theta0_coords.append(p0)
        theta1_coords.append(p1)

NUMS, ALPHAS = np.meshgrid(nums, alphas)
theta1_coords = np.array(theta1_coords)
theta0_coords = np.array(theta0_coords)  # Convert to NumPy array

# Ensure that theta0_coords is 2D
theta1_coords = np.reshape(theta1_coords, (len(alphas), len(nums)))
theta0_coords = np.reshape(theta0_coords, (len(alphas), len(nums)))

fig1 = plt.figure(figsize=(14, 6)) # 1 row, 2 columns

fig1 = fig1.add_subplot(1, 1, 1, projection='3d') # Specify 3D projectionf
fig1.plot_surface(NUMS, ALPHAS, theta0_coords, alpha=0.5, cmap='viridis')# Plot the noisy points
fig1.set_title('Intersection as a function of N and learning rate')
fig1.set_xlabel('N')
fig1.set_ylabel(r'${\alpha}$')
fig1.set_zlabel(r'${\theta}_0$')

plt.show()

fig2 = plt.figure(figsize=(14, 6))

fig2 = fig2.add_subplot(1, 1, 1, projection='3d') # Specify 3D projection
fig2.plot_surface(NUMS, ALPHAS, theta1_coords, alpha=0.5, cmap='viridis')# Plot the noisy points
fig2.set_title('Slope as a function of N and learning rate')
fig2.set_xlabel('N')
fig2.set_ylabel(r'${\alpha}$')
fig2.set_zlabel(r'${\theta}_1$')

plt.show()
