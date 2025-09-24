#from aux.linear_regression_example_plot import generate_and_plot_regression_problems

# linear_regression_plots.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D projection

def generate_and_plot_regression_problems():
    """
    Generates data and plots 2D and 3D linear regression problems.
    Returns the matplotlib figure object.
    """
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6)) # 1 row, 2 columns

    # --- Left Subplot: 2D Linear Regression Problem ---
    # Generate data for a straight line with noise
    np.random.seed(42)
    x_2d = np.linspace(0, 10, 50)
    true_slope = 2.5
    true_intercept = 5
    y_true_2d = true_slope * x_2d + true_intercept
    noise_2d = np.random.normal(0, 2, size=len(x_2d))
    y_noisy_2d = y_true_2d + noise_2d

    from sklearn.linear_model import LinearRegression
    X = x_2d.reshape(-1, 1)
    model = LinearRegression().fit(X, y_noisy_2d)
    y_pred = model.predict(X)

    # Plot the true line
    ax1.plot(x_2d, y_true_2d, 'r-', label='True Line')
    ax1.plot(x_2d, y_pred, 'g--', label='Predicted line')
    # Plot the noisy points
    ax1.scatter(x_2d, y_noisy_2d, color='blue', label='Noisy Data')
    ax1.set_title('2D Linear Regression Problem')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.legend()
    ax1.grid(True)

    # --- Right Subplot: 3D Plane Regression Problem ---
    # Generate data for a plane with noise
    ax2 = fig.add_subplot(1, 2, 2, projection='3d') # Specify 3D projection
    x_3d = np.linspace(-5, 5, 20)
    y_3d = np.linspace(-5, 5, 20)
    X_3d, Y_3d = np.meshgrid(x_3d, y_3d)
    true_coeff_x = 1.2
    true_coeff_y = -0.8
    true_intercept_3d = 3
    Z_true_3d = true_coeff_x * X_3d + true_coeff_y * Y_3d + true_intercept_3d
    noise_3d = np.random.normal(0, 1.5, size=Z_true_3d.shape)
    Z_noisy_3d = Z_true_3d + noise_3d

    # Plot the true plane surface
    ax2.plot_surface(X_3d, Y_3d, Z_true_3d, alpha=0.5, cmap='viridis', label='True Plane')
    # Plot the noisy points
    ax2.scatter(X_3d, Y_3d, Z_noisy_3d, color='red', s=20, label='Noisy Data') # s is marker size
    ax2.set_title('3D Linear Regression Problem (Plane)')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    # Adjust layout to prevent overlap
    plt.tight_layout()
    # No plt.show() here, as we return the figure to be shown in Jupyter
    return fig

# if __name__ == '__main__':
#     # This block only runs if the script is executed directly, not when imported
#     fig = generate_and_plot_regression_problems()
#     plt.show()


fig_regression_problems = generate_and_plot_regression_problems()
plt.show()
