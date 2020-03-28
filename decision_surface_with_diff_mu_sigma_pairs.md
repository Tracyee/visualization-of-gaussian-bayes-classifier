### hyperbola (双曲线)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 2. , 0], [0,  1.]])
mu2 = np.array([-3, 5.])
Sigma2 = np.array([[ 1. , 0], [0,  2.]])
```
* the decision line, decision surface and corresponding 3D viewing

| <img src="./results/hyperbola_line.png" width="280" height="240"> <img src="./results/hyperbola_surface.png" width="280" height="240"> <img src="./results/hyperbola_3d.png" width="280" height="240"> |
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

| <img src="./results/parabola_line.png" width="350" height="270"> <img src="./results/parabola_surface.png" width="350" height="270"> <img src="./results/parabola_3d.png" width="350" height="270"> |
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

| ![ellipse_line](./results/ellipse_line.png =350x) ![ellipse_surface](./results/ellipse_surface.png =350x) ![ellipse_3d](./results/ellipse_3d.png =350x) |
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

| ![circle_line](./results/circle_line.png =350x) ![circle_surface](./results/circle_surface.png =350x) ![circle_3d](./results/circle_3d.png =350x) |
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

| ![circle_line_2](./results/circle_line_2.png =350x) ![circle_surface_2](./results/circle_surface_2.png =350x) ![circle_3d_2](./results/circle_3d_2.png =350x) |
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

| ![line_line](./results/line_line.png =350x) ![line_surface](./results/line_surface.png =350x) ![line_3d](./results/line_3d.png =350x) |
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

| ![line_line_2](./results/line_line_2.png =350x) ![line_surface_2](./results/line_surface_2.png =350x) ![line_3d_2](./results/line_3d_2.png =350x) |
|:--:|
| *Line 2* |
