# K-Means Clustering on Synthetic Data

## Problem Statement
This project demonstrates the K-Means clustering algorithm on a synthetic dataset. The goal is to simulate an abstract clustering problem, apply K-Means to group the data into clusters, and evaluate its performance using metrics and visualization.

---

## Methodology

### 1. Data Generation
- **Function Used**: `generate_synthetic_data()`
- **Steps**:
  1. Used Scikit-learn's `make_blobs` function to create a synthetic dataset.
  2. Parameters:
     - `n_samples=1200`: 1200 data points generated.
     - `n_features=2`: Two-dimensional feature space.
     - `n_clusters=3`: Data distributed among three clusters.
     - `cluster_std=0.8`: Controls cluster spread.
     - `random_state=42`: Ensures reproducibility.
  3. **Output**:
     - `X`: Feature matrix of shape (1200, 2).
     - `true_labels`: Ground truth labels for validation (not used in clustering).

---

### 2. Data Preprocessing
- **Function Used**: `preprocess_data()`
- **Steps**:
  1. Standardized features using Scikit-learn's `StandardScaler`.
  2. Standardization ensured mean=0 and standard deviation=1 to balance features.
  3. **Result**: Transformed dataset (`X_scaled`) with normalized values.

---

### 3. Determining Optimal Clusters (Elbow Method)
- **Function Used**: `determine_optimal_clusters()`
- **Steps**:
  1. Tested K-Means clustering for a range of clusters (`k`) from 1 to 10.
  2. For each value of `k`:
     - Initialized a K-Means model (`n_clusters=k`, `random_state=42`, `n_init=10`).
     - Recorded the inertia (sum of squared distances to nearest cluster center).
  3. Plotted inertia values against `k` to identify the "elbow point."
  4. **Finding**: Optimal clusters identified at `k=3`.

---

### 4. Clustering with K-Means
- **Function Used**: `perform_kmeans_clustering()`
- **Steps**:
  1. Initialized a K-Means model with `n_clusters=3`, `random_state=42`, and `n_init=10`.
  2. Fitted the model on the standardized dataset (`X_scaled`).
  3. Computed:
     - Cluster labels (`labels`): Assigns each data point to a cluster.
     - Cluster centers: Mean position of each cluster.
  4. **Result**: Data grouped into three clusters.

---

### 5. Evaluation Metrics
- **Function Used**: `evaluate_clustering()`
- **Steps**:
  1. Calculated **Silhouette Score**:
     - Measures cluster separation and compactness.
     - **Result**: Silhouette Score = 0.7463 (high, indicating well-defined clusters).
  2. Retrieved **Inertia**:
     - Indicates cluster tightness.
     - **Result**: Inertia = 1023.21 (low, indicating tight clusters).

---

### 6. Visualization
- **Function Used**: `visualize_clusters()`
- **Steps**:
  1. Plotted a 2D scatter plot of the data using Matplotlib.
  2. Enhanced visualization:
     - Colored points based on cluster labels.
     - Marked centroids with red crosses.
     - Added title, axis labels, colorbar, and gridlines.
  3. **Result**: Clear visualization of separated clusters and accurately positioned centroids.

---

## Findings

### 1. Optimal Clusters
- The **Elbow Method** identified `k=3` as the optimal number of clusters.

### 2. Clustering Performance
- **Silhouette Score**: 0.7463 (high, indicating well-separated clusters).
- **Inertia**: 1023.21 (low, indicating compact clusters).

---

## Challenges and Insights

1. **Determining Optimal Clusters**:
   - The Elbow Method can be subjective with gradual changes in inertia.
2. **Scaling**:
   - Standardizing features was critical for balanced clustering.
3. **Initialization Stability**:
   - Multiple initializations (`n_init=10`) reduced the risk of poor centroid selection.
4. **Synthetic Data**:
   - Clear clusters in synthetic data may not represent real-world datasets with noise or overlap.

---

## Conclusion
This project demonstrates the effectiveness of the K-Means algorithm in clustering synthetic data. It highlights the importance of preprocessing, cluster evaluation, and visualization. The results provide a foundation for applying this workflow to real-world problems and exploring more complex clustering algorithms for non-spherical or high-dimensional datasets.
