🎵 Amazon Music Clustering Dashboard
Project Overview
This project provides an interactive web application built with Streamlit that performs K-Means clustering on a dataset of Amazon Music tracks. The application allows users to explore song clusters based on various audio features, visualize these clusters using Principal Component Analysis (PCA), and examine the characteristic profiles of each cluster. The application is designed to be easily runnable in a Google Colab environment and exposed via ngrok for public access.

Features
Data Loading: Automatically loads single_genre_artists.csv for analysis.
Data Preprocessing: Handles feature selection and scaling for clustering.
Elbow Method Visualization: Displays an Elbow Method plot to help determine the optimal number of clusters (k).
Interactive K-Means Clustering: Users can select the number of clusters (k) via a sidebar slider.
PCA Visualization: Clusters are visualized in a 2D space using PCA, with interactive Plotly graphs for better exploration.
Cluster Profiling: Shows the mean values of audio features for each cluster, aiding in understanding cluster characteristics.
Export Clustered Data: Allows downloading the dataset with assigned cluster labels.
Colab & ngrok Integration: Designed to run seamlessly in Google Colab, with public access facilitated by ngrok.
Setup and Installation (Google Colab)
To run this project in Google Colab, follow these steps:

Open in Colab: Open your .ipynb notebook in Google Colab.

Upload Data: Ensure single_genre_artists.csv is uploaded to your Colab environment's root directory. You can do this by clicking the folder icon on the left sidebar -> Upload button -> select single_genre_artists.csv.

Install Dependencies: Run the following cell in your Colab notebook to install necessary libraries:

!pip install streamlit pandas numpy matplotlib seaborn scikit-learn plotly pyngrok
Set ngrok Authtoken: ngrok requires an authentication token to create a public tunnel.

Go to ngrok dashboard to get your authtoken.
Run the following cell, replacing 'YOUR_AUTHTOKEN' with your actual token:
from pyngrok import ngrok
import os

NGROK_AUTH_TOKEN = "YOUR_AUTHTOKEN" # Replace with your ngrok authtoken
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
print("ngrok authtoken configured.")
Create Streamlit App (app.py): The Streamlit application code is written to app.py. Execute the relevant cells in your Colab notebook to create and update this file with the application logic.

Run Streamlit App with ngrok: Execute the following cell. This will start the Streamlit application in the background and create a public ngrok URL.

import os
from pyngrok import ngrok

# Run Streamlit app in the background
os.system("nohup streamlit run app.py &")
# 2. Open a tunnel on port 8501 (Streamlit's default port)
public_url = ngrok.connect(8501)

print(f"Click the link to open your app: {public_url}")
Usage
After executing all the steps above, a public ngrok URL will be printed in the output of the last cell. Click on this URL to open your interactive Amazon Music Clustering Dashboard in your web browser.

Interacting with the Dashboard:

Sidebar: Use the sidebar to adjust the number of clusters (k) for the K-Means algorithm.
Data Overview: View a sample of the raw data.
Elbow Method: Observe the Elbow Method plot to guide your choice of k.
PCA Visualization: Explore the song clusters in a 2D PCA plot. This interactive plot allows you to zoom, pan, and hover over individual points to see details.
Cluster Characteristics: Analyze the table showing the average feature values for each cluster to understand their unique musical profiles.
Download Clustered Data: Download the dataset with the assigned cluster labels for further analysis.
Example Outputs (within the app)
Elbow Method Plot: A line plot showing SSE vs. number of clusters.
PCA Scatter Plot: An interactive scatter plot where each point is a song, colored by its assigned cluster.
Cluster Profile Table: A table summarizing the average values of audio features for each cluster (e.g., mean danceability, energy, loudness, etc.).
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Colab
