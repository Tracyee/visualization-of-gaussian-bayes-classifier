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

You may fine some test samples in [here](decision_surface_with_diff_mu_sigma_pairs.md).
