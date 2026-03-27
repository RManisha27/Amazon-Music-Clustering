# amazon_music_cli.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 1. Load dataset
try:
    df = pd.read_csv('single_genre_artists.csv')
    print("✅ Dataset 'single_genre_artists.csv' loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'single_genre_artists.csv' not found. Please ensure the file is in this folder.")
    exit()

# 2. Show data overview
print("\n--- Data Overview ---")
print(df.head())
print(f"\nDataset contains {df.shape[0]} songs and {df.shape[1]} features.")

# Recommended audio features for clustering
features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

X = df[features]

# 3. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Ask user for number of clusters
while True:
    try:
        k = int(input("\nEnter number of clusters (k, e.g., 2-10): "))
        if k < 2:
            print("Please enter a number >= 2")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# 5. K-Means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)
print(f"\n✅ K-Means clustering completed with k={k}")

# 6. Elbow Method
print("\nGenerating Elbow Method plot...")
sse = []
for k_val in range(1, 11):
    kmeans_elbow = KMeans(n_clusters=k_val, random_state=42)
    kmeans_elbow.fit(X_scaled)
    sse.append(kmeans_elbow.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), sse, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("SSE (Sum of Squared Errors)")
plt.title("Elbow Method for K-Means")
plt.axvline(x=k, color='red', linestyle='--', label=f'Selected k={k}')
plt.legend()
plt.tight_layout()
plt.savefig("elbow_plot.png")
print("✅ Elbow plot saved as 'elbow_plot.png'")

# 7. PCA for 2D visualization
print("\nGenerating PCA 2D scatter plot...")
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)
pca_df = pd.DataFrame(data=components, columns=['PC1','PC2'])
pca_df['Cluster'] = df['cluster'].astype(str)

plt.figure(figsize=(8,6))
for cluster in sorted(df['cluster'].unique()):
    subset = pca_df[pca_df['Cluster']==str(cluster)]
    plt.scatter(subset['PC1'], subset['PC2'], label=f'Cluster {cluster}', s=50, alpha=0.7)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title(f"Song Clusters Visualization (PCA) with {k} clusters")
plt.legend()
plt.tight_layout()
plt.savefig("pca_clusters.png")
print("✅ PCA scatter plot saved as 'pca_clusters.png'")

# 8. Cluster Characteristics
print("\n--- Cluster Characteristics ---")
cluster_profiles = df.groupby('cluster')[features].mean().round(2)
print(cluster_profiles)

# 9. Export clustered CSV
df.to_csv("clustered_songs.csv", index=False)
print("\n✅ Clustered data saved as 'clustered_songs.csv'")
print("\nAll done! You can view the plots and CSV in the current folder.")