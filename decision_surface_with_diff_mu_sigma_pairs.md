### hyperbola (双曲线)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 2. , 0], [0,  1.]])
mu2 = np.array([-3, 5.])
Sigma2 = np.array([[ 1. , 0], [0,  2.]])
```
* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/hyperbola_line.png" width="280" height="220"> <img src="./results/hyperbola_surface.png" width="280" height="220"> <img src="./results/hyperbola_3d.png" width="280" height="220"> |
|:--:|
| *Hyperbola* |

### parabola (抛物线)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 2. , 0.5], [0.5,  1.]])
mu2 = np.array([-4, -4.])
Sigma2 = np.array([[ 2. , 0], [0,  2.]])
```

* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/parabola_line.png" width="280" height="220"> <img src="./results/parabola_surface.png" width="280" height="220"> <img src="./results/parabola_3d.png" width="280" height="220"> |
|:--:|
| *Parabola* |

### ellipse (椭圆)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 0.8 , 0.3], [0.3,  0.8]])
mu2 = np.array([-4, -4.])
Sigma2 = np.array([[ 2. , 1], [1,  2.]])
```

* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/ellipse_line.png" width="280" height="220"> <img src="./results/ellipse_surface.png" width="280" height="220"> <img src="./results/ellipse_3d.png" width="280" height="220"> |
|:--:|
| *Ellipse* |


### circle (圆)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 0.5 , 0], [0,  0.5]])
mu2 = np.array([-4, -4.])
Sigma2 = np.array([[ 2. , 0], [0,  2.]])
```

* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/circle_line.png" width="280" height="220"> <img src="./results/circle_surface.png" width="280" height="220"> <img src="./results/circle_3d.png" width="280" height="220"> |
|:--:|
| *Circle 1* |


* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 1. , 0], [0,  1.]])
mu2 = np.array([-4, -4.])
Sigma2 = np.array([[ 2. , 0], [0,  2.]])
```

* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/circle_line_2.png" width="280" height="220"> <img src="./results/circle_surface_2.png" width="280" height="220"> <img src="./results/circle_3d_2.png" width="280" height="220"> |
|:--:|
| *Circle 2* |

### line (直线)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 1 , 0], [0,  1]])
mu2 = np.array([-4, -4.])
Sigma2 = np.array([[ 1 , 0], [0,  1]])
```

* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/line_line.png" width="280" height="220"> <img src="./results/line_surface.png" width="280" height="220"> <img src="./results/line_3d.png" width="280" height="220"> |
|:--:|
| *Line 1* |

* mean and covariance pairs for two distributions
```python
mu1 = np.array([2., 2.])
Sigma1 = np.array([[ 1 , 0], [0,  3]])
mu2 = np.array([-2, -2.])
Sigma2 = np.array([[ 3 , 0], [0,  1]])
```

* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/line_line_2.png" width="280" height="220"> <img src="./results/line_surface_2.png" width="280" height="220"> <img src="./results/line_3d_2.png" width="280" height="220"> |
|:--:|
| *Line 2* |
