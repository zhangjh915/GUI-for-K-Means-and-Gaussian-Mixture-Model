# Visualization of K-means and GMM algorithms

## Description:
This repository includes a vectorized version of K-means and GMM based on numpy; 
as well as GUIs for visualization purposes on 2D datasets and images.

## Package Requirements:
`numpy >= 1.15`

`matplotlib >= 2.2.2`

`tkinter` (For Anaconda, run `conda install -c anaconda tk` to install)

## GUI Visualization:
**GUI for K-Means and GMM on 2D datasets:**

![](images/GUI_dataset.gif)

**GUI for K-Means on image clusterings:**

![](images/GUI_image.gif)

**Results for GMM on image clusterings:**

![](images/GUI_GMM.PNG)

## Algorithm for K-means:
1. Random initialization of cluster centers.

2. Assign all data points to their closest cluster center according to the Euclidean distance function.

3. Calculate the centroid or mean of all data points in each cluster.

4. Repeat steps 1, 2 and 3 until the same points are assigned to each cluster in consecutive rounds.

The objective function used for the algorithm is

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?J=\sum_{n=1}^{N}\sum_{k=1}^{K}r_{nk}||\mathbf{x}_n&space;-&space;\bm{\mu}_k||" title="J=\sum_{n=1}^{N}\sum_{k=1}^{K}r_{nk}||\mathbf{x}_n - \bm{\mu}_k||" />
</p>

## Algorithm for GMM:
1. Initialize the means <img src="https://latex.codecogs.com/gif.latex?\mu_k" title="\mu_k" />, covariances <img src="https://latex.codecogs.com/gif.latex?\Sigma_k" title="\Sigma_k" />, and mixing coefficient <img src="https://latex.codecogs.com/gif.latex?\pi_k" title="\pi_k" />. Then evaluate the initial value of the log likelihood.

2. **E step**. Evaluate the responsibilities using the current parameter values:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\gamma(z_{nk})=\tfrac{\pi_k&space;N(x_n|\mu_k,&space;\Sigma_k)}{\sum_{j=1}^{K}\pi_j&space;N(x_n|\mu_j,&space;\Sigma_j)}" title="\gamma(z_{nk})=\tfrac{\pi_k N(x_n|\mu_k, \Sigma_k)}{\sum_{j=1}^{K}\pi_j N(x_n|\mu_j, \Sigma_j)}" />
</p>

3. **M step**. Re-estimate the parameters using the current responsibilities:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\mu_k^{new}=\tfrac{1}{N_k}\sum_{n=1}^{N}\gamma(z_{nk})x_n" title="\mu_k^{new}=\tfrac{1}{N_k}\sum_{n=1}^{N}\gamma(z_{nk})x_n" />
</p>

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\Sigma_k^{new}=\tfrac{1}{N_k}\sum_{n=1}^{N}\gamma(z_{nk})(x_n-\mu_k^{new})(x_n-\mu_k^{new})^T" title="\Sigma_k^{new}=\tfrac{1}{N_k}\sum_{n=1}^{N}\gamma(z_{nk})(x_n-\mu_k^{new})(x_n-\mu_k^{new})^T" />
</p>

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\pi_k^{new}=\tfrac{N_k}{N}" title="\pi_k^{new}=\tfrac{N_k}{N}" />
</p>

where

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?N_k&space;=&space;\sum_{n=1}^{N}\gamma(z_{nk})" title="N_k = \sum_{n=1}^{N}\gamma(z_{nk})" />
</p>

4. Evaluate the log likelihood:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?ln\:&space;p(X|\mu,&space;\Sigma,&space;\pi)&space;=&space;\sum_{n=1}^{N}ln\{\sum_{k=1}^{K}\pi_kN(x_k|\mu_k,\Sigma_k)\}" title="ln\: p(X|\mu, \Sigma, \pi) = \sum_{n=1}^{N}ln\{\sum_{k=1}^{K}\pi_kN(x_k|\mu_k,\Sigma_k)\}" />
</p>

5. Check for convergence of the log likelihood. If the convergence criterion is not satisfied, then return to step 2.


## Code Usage:
All rights preserved. No one should use the code without permission from the author.

Note that GUI for GMM is not recommended to run on personal laptops since the strict converge condition may 
make the model to take minutes until clustered images to appear, which may freeze the GUI window for a short 
amount of time. If personal laptop users want to wait for the result, make sure to close other applications 
that might consume high CPU resources.

1. Run GUI_2D_datasets.py and play with the buttons to visualize K-means and GMM algorithms on 2D datasets.
2. Run GUI_image_clusters.py and play with the buttons to visualize K-means and GMM algorithms on image clusterings.


## References:
1. [https://www.saedsayad.com/clustering_kmeans.htm](https://www.saedsayad.com/clustering_kmeans.htm)
2. [http://www.rmki.kfki.hu/~banmi/elte/bishop_em.pdf](http://www.rmki.kfki.hu/~banmi/elte/bishop_em.pdf)
