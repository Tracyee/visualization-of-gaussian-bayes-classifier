import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

class BivariateGauss:
    def __init__(self, X, Y, mu, Sigma):
        self.X = X
        self.Y = Y
        self.mu = mu
        self.Sigma = Sigma
        # Pack X and Y into a single 3-dimensional array
        self.pos = np.empty(self.X.shape + (2,))
        self.pos[:, :, 0] = self.X
        self.pos[:, :, 1] = self.Y

    def multivariate_gaussian(self):
        """
        Return the multivariate Gaussian distribution on array pos.

        pos is an array constructed by packing the meshed arrays of variables
        x_1, x_2, x_3, ..., x_k into its _last_ dimension.
        """

        n = self.mu.shape[0]
        Sigma_det = np.linalg.det(self.Sigma)
        Sigma_inv = np.linalg.inv(self.Sigma)
        N = np.sqrt((2*np.pi)**n * Sigma_det)
        # This einsum call calculates (x-mu)T.Sigma-1.(x-mu) in a vectorized
        # way across all the input variables.
        fac = np.einsum('...k,kl,...l->...', self.pos-self.mu, Sigma_inv, self.pos-self.mu)
        return np.exp(-fac / 2) / N


def in_test():
    # Our 2-dimensional distribution will be over variables X1 and X2
    N = 60
    X1 = np.linspace(-3, 3, N)
    X2 = np.linspace(-3, 4, N)
    X1, X2 = np.meshgrid(X1, X2)

    # Mean vector and covariance matrix
    mu = np.array([0., 1.])
    Sigma = np.array([[ 1. , -0.5], [-0.5,  1.5]])

    fig, ax = plt.subplots()
    gauss = BivariateGauss(X1, X2, mu, Sigma)
    Z = gauss.multivariate_gaussian()
    CS = ax.contour(X1, X2, Z, colors='0.4')
    ax.clabel(CS, inline=1, fontsize=10)
    plt.show()


if __name__ == "__main__":
    in_test()
