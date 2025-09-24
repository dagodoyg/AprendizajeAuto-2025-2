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
alphas = [0.01, 0.1, 0.5, 0.9]
fig, ax = plt.subplots(1, 4, figsize=(14, 6)) 
ii = 0

for a in alphas:
    P0 = []
    P1 = []
    for n in nums:
        p0, p1 = step(theta_0, theta_1, N=n, alpha=a, verbose=False)
        P0.append(p0)
        P1.append(p1)
    ax[ii].set_title(f'alpha = {a}')
    ax[ii].set_xlabel('N')
    ax[ii].plot(nums, P0, label = r'${\theta}_0$')
    ax[ii].plot(nums, P1, label = r'${\theta}_1$')
    ii += 1

plt.legend()
plt.show()
