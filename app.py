import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.title("🎵 Amazon Music Clustering App")

# Load dataset
try:
    df = pd.read_csv('single_genre_artists.csv')
    st.success("Dataset loaded successfully!")
except:
    st.error("Dataset not found. Upload file.")
    st.stop()

st.write(df.head())

features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

X = df[features]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔥 Replace input() with slider
k = st.slider("Select number of clusters (k)", 2, 10, 3)

# KMeans
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

st.success(f"K-Means clustering done with k={k}")

# Elbow Method
sse = []
for k_val in range(1, 11):
    kmeans_elbow = KMeans(n_clusters=k_val, random_state=42)
    kmeans_elbow.fit(X_scaled)
    sse.append(kmeans_elbow.inertia_)

fig1, ax1 = plt.subplots()
ax1.plot(range(1,11), sse, marker='o')
ax1.set_xlabel("k")
ax1.set_ylabel("SSE")
ax1.set_title("Elbow Method")

st.pyplot(fig1)

# PCA Plot
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(components, columns=['PC1','PC2'])
pca_df['cluster'] = df['cluster']

fig2, ax2 = plt.subplots()

for cluster in sorted(df['cluster'].unique()):
    subset = pca_df[pca_df['cluster'] == cluster]
    ax2.scatter(subset['PC1'], subset['PC2'], label=f'Cluster {cluster}')

ax2.set_title("PCA Clusters")
ax2.legend()

st.pyplot(fig2)

# Cluster summary
st.subheader("Cluster Characteristics")
st.write(df.groupby('cluster')[features].mean().round(2))

# Download CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download Clustered Data", csv, "clustered_songs.csv", "text/csv")
