import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

def generate_synthetic_data(n_samples=1000, n_features=2, n_clusters=3):

    X, true_labels = make_blobs(
        n_samples=n_samples, 
        n_features=n_features, 
        centers=n_clusters, 
        cluster_std=0.8,  # standard deviation 
        random_state=42   # reproducibility
    )
    return X, true_labels

def preprocess_data(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

def perform_kmeans_clustering(X, n_clusters=3):
    kmeans = KMeans(
        n_clusters=n_clusters, 
        random_state=42,
        n_init=10  # recommended number of initializations
    )
    labels = kmeans.fit_predict(X)
    return kmeans, labels

def evaluate_clustering(X, kmeans, labels):
    silhouette_avg = silhouette_score(X, labels)
    inertia = kmeans.inertia_
    return silhouette_avg, inertia

def visualize_clusters(X, labels, kmeans):
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.7)
    plt.scatter(
        kmeans.cluster_centers_[:, 0], 
        kmeans.cluster_centers_[:, 1], 
        color='red', 
        marker='x', 
        s=200, 
        linewidths=3, 
        label='Centroids'
    )
    plt.title('K-Means Clustering of Synthetic Data', fontsize=16)
    plt.xlabel('Feature 1', fontsize=12)
    plt.ylabel('Feature 2', fontsize=12)
    plt.colorbar(scatter, label='Cluster Labels')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def determine_optimal_clusters(X, max_clusters=10):
    inertias = []
    cluster_range = range(1, max_clusters + 1)
    
    for k in cluster_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    
    # plot the elbow curve
    plt.figure(figsize=(10, 6))
    plt.plot(cluster_range, inertias, marker='o')
    plt.title('Elbow Method for Optimal k', fontsize=16)
    plt.xlabel('Number of Clusters (k)', fontsize=12)
    plt.ylabel('Inertia', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    
    return inertias

def main():
    # generate synthetic data
    X, true_labels = generate_synthetic_data(
        n_samples=1200,  
        n_features=2,    
        n_clusters=3     # 3 distinct clusters
    )
    
    X_scaled = preprocess_data(X)
    
    # optimal number of clusters
    determine_optimal_clusters(X_scaled)
    
    # clustering
    kmeans, labels = perform_kmeans_clustering(X_scaled)
    
    # evaluate
    silhouette_avg, inertia = evaluate_clustering(X_scaled, kmeans, labels)
    
    print(f"Silhouette Score: {silhouette_avg:.4f}")
    print(f"Inertia: {inertia:.2f}")
    
    # visualize 
    visualize_clusters(X_scaled, labels, kmeans)

if __name__ == "__main__":
    main()