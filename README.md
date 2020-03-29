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

###  工具

* 平台：Python、numpy

* 画图：matplotlib

  

### 思路

* 样本集（散点）： 
  - 利用`numpy.random`方法中的多变量正态分布方法`(multivariate_normal(mean, cov, size)`)，生成样本集1（`x1`,`x2`）和样本集2（`x3`,`x4`）
  - 利用`matplotlib.pyplot`中的`plot`方法，画出两类样本集的散点图
* 等密度点轨迹以及分类面：
  - 根据二维正态分布的数学定义，手动构造一个`BivariateGauss`类——调用其中的方法可返回给定均值和协方差矩阵的二维正态分布数学表达式（**重点**）
  - 利用`matplotlib.pyplot`中的等高线（`contour`）方法，代入采样点和两类二维正态分布的数学表达式（`Z1`, `Z2`），画出两类分布的等密度点轨迹
  - 同样利用等高线方法，代入采样点和两类分布的数学表达式之差`Z1 - Z2`，可视化`Z1 - Z2 = 0`的等高线，即可画出分类面
  - 利用`matplotlib.pyplot`中的`plot_surface`方法，还可以实现两类二维正态分布的3D可视化


### 运行 Run
Run `run.py` for 2D or 3D visualization of bayes classifier.


With special thanks to previous work done by [Visualizing the bivariate Gaussian distribution](https://scipython.com/blog/visualizing-the-bivariate-gaussian-distribution/).

You may fine some test samples in [here](decision_surface_with_diff_mu_sigma_pairs.md).
