# visualization-of-gaussian-bayes-classifier
Draw the samples, probability density contour and decision surface of two bi-variant Gaussian distributions（贝叶斯分类器可视化——对满足高斯分布的样本）


### 任务1：设计两类二维正态分布样本，决策面为线性

* **已知**：来自于两类的随机数样本，等先验概率，分别满足二维正态分布，协方差分别满足下列两种情况：

<p align="center">
<img src="http://latex.codecogs.com/svg.latex?\Sigma_{i}=\sigma^{2} I \quad \Sigma_{i}=\Sigma" border="0"/>
</p>

* **要求**：针对上述两种情况，分别画出样本集(注意区分)、等密度点轨迹以及分类面

### 任务2 ：设计两类二维正态分布样本，决策面为非线性

* **已知**：来自于两类的随机数样本，等先验概率，分别满足二维正态分布，两类协方差不相等

* **要求**：画出样本集(注意区分)、等密度点轨迹以及分类面


### 运行 Run
Run `run.py` for 2D or 3D visualization of bayes classifier.


With special thanks to previous work done by [Visualizing the bivariate Gaussian distribution](https://scipython.com/blog/visualizing-the-bivariate-gaussian-distribution/).

You may fine some test samples in [here](decision_surface_with_diff_mu_sigma_pairs.md)
### hyperbola (双曲线)

* mean and covariance pairs for two distributions
```python
mu1 = np.array([0., 1.])
Sigma1 = np.array([[ 2. , 0], [0,  1.]])
mu2 = np.array([-3, 5.])
Sigma2 = np.array([[ 1. , 0], [0,  2.]])
```
* the decision line, decision surface and corresponding 3D viewing

| ![hyperbola_line](./results/hyperbola_line.png =350x) ![hyperbola_surface](./results/hyperbola_surface.png =350x) ![hyperbola_3d](./results/hyperbola_3d.png =350x) |
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

| ![parabola_line](./results/parabola_line.png =350x) ![parabola_surface](./results/parabola_surface.png =350x) ![parabola_3d](./results/parabola_3d.png =350x) |
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
