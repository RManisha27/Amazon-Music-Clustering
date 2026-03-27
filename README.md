# 🎵 Amazon Music Clustering Dashboard

## 🚀 Live Demo

👉 https://amazon-music-clustering-fqjgfblzmpuqfm4nxxsteu.streamlit.app/

---

## 📌 Project Overview

This project is an interactive web application built using **Streamlit** that performs **K-Means clustering** on Amazon Music track data.

It allows users to explore song groupings based on audio features, visualize clusters in 2D space using **Principal Component Analysis (PCA)**, and analyze cluster characteristics in an intuitive dashboard.

---

## ✨ Features

### 📊 Data Processing

* Loads dataset: `single_genre_artists.csv`
* Selects key audio features like:

  * danceability
  * energy
  * tempo
  * acousticness
* Applies feature scaling using StandardScaler

---

### 📈 Elbow Method Visualization

* Displays SSE vs number of clusters
* Helps determine optimal value of **k**
* Interactive plot inside the app

---

### 🎛 Interactive Clustering

* Select number of clusters using a slider
* Real-time clustering using K-Means
* Instant updates in results

---

### 🔍 PCA Visualization

* Reduces high-dimensional data to 2D
* Visualizes clusters clearly
* Helps understand grouping patterns

---

### 📊 Cluster Profiling

* Displays mean values of features per cluster
* Helps interpret different types of songs

---

### 📥 Export Feature

* Download clustered dataset as CSV
* Useful for further analysis

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/amazon-music-clustering.git
cd amazon-music-clustering
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App Locally

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This project is deployed using **Streamlit Cloud**.

### Steps:

1. Push code to GitHub
2. Add `requirements.txt`
3. Deploy via Streamlit Cloud
4. App runs automatically with a public URL

---

## 📁 Project Structure

```
amazon-music-clustering/
│── app.py
│── single_genre_artists.csv
│── requirements.txt
│── README.md
```

---

## 📊 Output

* Clustered dataset
* Elbow method graph
* PCA visualization
* Cluster-wise feature summary

---

## 🎯 Learning Outcomes

* Unsupervised Machine Learning
* K-Means Clustering
* Feature Scaling
* Dimensionality Reduction (PCA)
* Data Visualization
* Cloud Deployment

---

## 📌 Future Enhancements

* 🎯 Song recommendation system
* 🎨 Improved UI design
* 📊 Advanced interactive charts (Plotly)
* 📁 Multiple dataset support

---

## 👩‍💻 Author

Manisha Ravi


Give it a ⭐ on GitHub!
