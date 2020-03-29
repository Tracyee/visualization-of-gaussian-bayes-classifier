import numpy as np
import matplotlib.pyplot as plt
from gaussian import BivariateGauss
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


def draw_contour(X, Y, Z, ax):
    '''
    Create a simple contour plot with labels using self-defined colors.
    The inline argument to clabel will control whether the labels
    are draw over the line segments of the contour, removing the lines beneath the label
    '''
    CS = ax.contour(X, Y, Z, colors='0.7')
    ax.clabel(CS, inline=1, fontsize=10)

def main(X, mu, Sigma):
    # unpack the params
    X1, X2 = X
    mu1, mu2 = mu
    Sigma1, Sigma2 = Sigma
    # Samples for scatter plot
    x1, x2 = np.random.multivariate_normal(mu1, Sigma1, 1000).T
    x3, x4 = np.random.multivariate_normal(mu2, Sigma2, 1000).T

    fig, ax = plt.subplots()
    fig.set_size_inches(10.5, 10.5)

    gauss1 = BivariateGauss(X1, X2, mu1, Sigma1)
    gauss2 = BivariateGauss(X1, X2, mu2, Sigma2)
    Z1 = gauss1.multivariate_gaussian()
    Z2 = gauss2.multivariate_gaussian()

    # Make the scatter plot for the samples
    ax.plot(x1, x2, '*',alpha=0.2)
    ax.plot(x3, x4, '*',alpha=0.2)

    # The decision lines
    ax.contour(X1, X2, (Z2-Z1))

    # The decision surface
    # ax.contourf(X1, X2, (Z2-Z1), colors=('1', '1', '1', '1', '.2', '.2', '.2', '.2', '.2'))

    # The probability density contour
    draw_contour(X1, X2, Z1, ax)
    draw_contour(X1, X2, Z2, ax)
    # ax.set_title('样本集、等密度点轨迹、分类面')
    ax.set_title('Samples, probability density contour and decision surface')
    plt.axis('equal')

    plt.show()
    fig.savefig('./results/line_line_3.png', dpi=100)

def three_D(X, mu, Sigma):
    # Create a surface plot and projected filled contour plot under it.
    gauss1 = BivariateGauss(X1, X2, mu1, Sigma1)
    gauss2 = BivariateGauss(X1, X2, mu2, Sigma2)
    Z1 = gauss1.multivariate_gaussian()
    Z2 = gauss2.multivariate_gaussian()

    fig = plt.figure()
    fig.set_size_inches(10.5, 10.5)
    ax = fig.gca(projection='3d')

    ax.plot_surface(X1, X2, Z1, rstride=3, cstride=3, linewidth=10, antialiased=True,
                    cmap=cm.hot)
    ax.plot_surface(X1, X2, Z2, rstride=3, cstride=3, linewidth=10, antialiased=True,
                    cmap=cm.viridis)

    cset1 = ax.contour(X1, X2, Z1, zdir='z', offset=-0.15, cmap=cm.hot)
    cset2 = ax.contour(X1, X2, Z2, zdir='z', offset=-0.15, cmap=cm.viridis)

    ax.contour(X1, X2, (Z2-Z1), offset=-0.15)
    # Adjust the limits, ticks and view angle
    ax.set_title('probability density distribution, contour and decision surface in 3D-view')
    ax.set_zlim(-0.15,0.2)
    ax.set_zticks(np.linspace(0,0.2,5))
    ax.view_init(27, -21)
    # ax.view_init(50, -40)

    plt.show()

if __name__ == "__main__":
    # Samples
    N = 200
    # Adjust the range of X1 and X2 for better viewing
    X1 = np.linspace(-10, 10, N)
    X2 = np.linspace(-10, 10, N)
    X1, X2 = np.meshgrid(X1, X2) # Construt coordinate matrices for contour-drawing

    # Mean vector and covariance matrix for two classes
    mu1 = np.array([2., 2.])
    Sigma1 = np.array([[ 1 , 0], [0,  2]])
    mu2 = np.array([-2, -2.])
    Sigma2 = np.array([[ 1 , 0], [0,  2]])

    # pack the params
    X = [X1, X2]
    mu = [mu1, mu2]
    Sigma = [Sigma1, Sigma2]

    # main(X, mu, Sigma)
    three_D(X, mu, Sigma)
