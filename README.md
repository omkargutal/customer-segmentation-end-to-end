# 👥 Customer Segmentation using K-Means Clustering

> **Unsupervised Machine Learning | K-Means Clustering | Streamlit Deployment**

A complete end-to-end machine learning project that segments customers into distinct behavioral groups based on their demographic profiles, purchasing history, and campaign engagement — enabling targeted and personalized marketing strategies.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Defination](#-problem-defination)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Customer Segments](#-customer-segments)
- [Project Structure](#-project-structure)
- [Tech Stack](#️-tech-stack)
- [Setup & Installation](#️-setup--installation)
- [Running the App](#-running-the-app)
- [Results & Insights](#-results--insights)
- [Contributors](#-contributors)

---

## 📌 Overview

Customer segmentation is the process of dividing customers into groups based on shared characteristics. This project uses **K-Means Clustering** — an unsupervised machine learning algorithm — to identify four distinct customer personas from a marketing campaign dataset.

The findings are deployed as an interactive **Streamlit web application** that allows business users to input any customer's profile and instantly predict which segment they belong to, along with actionable marketing insights.

---

##  Problem Defination

Modern businesses struggle to deliver personalized experiences at scale. A one-size-fits-all marketing approach leads to wasted budget and poor customer engagement. The goal of this project is to:

- Identify natural groupings of customers from behavioral data
- Understand the key traits of each customer segment
- Build a deployable tool that classifies new customers in real time

---

## 📊 Dataset

- **Source:** `marketing_campaign.xlsx`
- **Records:** ~2,200 customer entries
- **Features Used:**

| Category | Features |
|---|---|
| **Demographics** | Age, Income, Education Level, Marital Status |
| **Purchase Behavior** | Total Spending, Total Purchases, Recency |
| **Engagement** | Web Visits/Month, Deals Purchased, Campaigns Accepted, Last Campaign Response |
| **Household** | Total Dependents |

---

## 🔬 Methodology

The project follows a structured data science workflow:

1. **Data Loading & Exploration (EDA)**
   - Univariate & bivariate analysis
   - Identifying distributions, outliers, and correlations

2. **Data Preprocessing**
   - Handling missing values (income imputation)
   - Feature engineering (e.g., Age from `Year_Birth`, `Total_Spend`, `Total_Purchases`, `Total_Dependents`, `Total_Campaigns_Accepted`)
   - Encoding categorical variables (Education, Marital Status)

3. **Feature Scaling**
   - Applied `StandardScaler` to normalize all features before clustering

4. **Dimensionality Reduction**
   - PCA (Principal Component Analysis) used for 2D visualization of clusters

5. **Model Building — K-Means Clustering**
   - Optimal number of clusters determined using the **Elbow Method** and **Silhouette Score**
   - Final model: **K = 4 clusters**

6. **Model Persistence**
   - Trained `KMeans` model saved as `kmeans_model.pkl`
   - `StandardScaler` saved as `scaler.pkl`

7. **Deployment**
   - Interactive prediction app built with **Streamlit** (`app.py`)

---

## 🎯 Customer Segments

The model identifies **4 distinct customer personas**:

| Cluster | Segment Name | Description |
|:---:|---|---|
| **0** | 🔵 Average Mainstream | Steady customers with moderate spending habits. Respond to standard offers. |
| **1** | 🟢 Budget-Conscious | Price-sensitive customers; highly responsive to discounts and deals. |
| **2** | 🟠 High-Value | High income earners who shop frequently across all product channels. |
| **3** | 🔴 Premium Loyal | Top-tier customers with high spending and very high campaign engagement. |

---

## 📁 Project Structure

```
customer-segmentation/
│
├── Customer_Segmentation_Final.ipynb   # Main notebook: EDA, preprocessing, modeling
│
├── app.py                              # Streamlit web application for live prediction
│
├── kmeans_model.pkl                    # Trained K-Means clustering model
├── scaler.pkl                          # Fitted StandardScaler for feature normalization
│
├── marketing_campaign.xlsx             # Raw dataset
├── customer_segmentation_model_ready.csv   # Preprocessed & scaled data (model input)
├── customer_segmentation_clustered.csv     # Dataset with predicted cluster labels
│
├── requirements.txt                    # Python dependencies
├── .env                                # Environment variables (NGROK token) — do 
└── README.md                           # Project documentation
```

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **Pandas & NumPy** | Data manipulation and numerical computing |
| **Matplotlib & Seaborn** | Data visualization and EDA |
| **Scikit-learn** | K-Means clustering, StandardScaler, PCA, Silhouette Score |
| **OpenPyXL** | Reading Excel dataset files |
| **Streamlit** | Interactive web application deployment |
| **Pickle** | Model serialization and persistence |

---

## 🔐 Environment Variables

This project uses a `.env` file to store sensitive credentials. A `.env` file is already provided in the project directory.


## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or download the project**
   ```bash
   git clone `https://github.com/omkargutal/customer-segmentation-end-to-end.git`
   cd customer-segmentation
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install python-dotenv
   ```

4. **Configure your `.env` file**
   - Open `.env` in the project folder
   - Paste your NGROK auth token (see [Environment Variables](#-environment-variables) section above)

---

## 🚀 Running the App

Once dependencies are installed, launch the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

### How to Use the App

1. Fill in the **customer's demographic** details (Age, Income, Education, Marital Status)
2. Enter the **purchase history** (Total Spending, Purchases, Recency, Dependents)
3. Provide **engagement data** (Web Visits, Deals, Campaigns Accepted, Last Response)
4. Click **🚀 Predict Segment**
5. The app displays the predicted **cluster** and a **business insight** for that customer

---

## 📈 Results & Insights

- Successfully segmented customers into **4 meaningful behavioral clusters** with clear business interpretability
- **Premium Loyal** customers (Cluster 3) showed the highest spending and campaign acceptance rates — prime targets for premium product launches
- **Budget-Conscious** customers (Cluster 1) are best targeted with discount-driven campaigns and deal promotions
- **High-Value** customers (Cluster 2) engage across all purchase channels — ideal for cross-sell and upsell strategies
- **Average Mainstream** customers (Cluster 0) respond well to consistent loyalty programs

---

## 👥 Contributors

- **Omkar Gutal** 
- **Moin Mohammed** 
- **Khushi Choudhari** 

---

## 📄 License

This project is submitted as part of an academic/professional data science assessment. All rights reserved © 2026 Omkar Gutal.
