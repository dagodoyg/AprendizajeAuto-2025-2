import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

# Data generation
np.random.seed(0)
n = 200
x = np.random.normal(size=n)
y = 2.0 * x + 0.8 * np.random.normal(size=n)
X = np.vstack([x, y]).T

#Xc = X - X.mean(axis=0)
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

explained_variance = pca.explained_variance_ratio_
print(f"\nVariance explained by PC1: {explained_variance[0]:.2%}")
print(f"Variance explained by PC2: {explained_variance[1]:.2%}")
print(f"Total variance explained: {np.sum(explained_variance):.2%}")
