from sklearn.cluster import KMeans

# Sample data points (2D)
X = [[1, 2], [1, 4], [1, 0],
     [10, 2], [10, 4], [10, 0]]

# Apply KMeans with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Output cluster labels
print("Labels:", kmeans.labels_)
print("Centers:", kmeans.cluster_centers_)
