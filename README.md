<div align="center">

# 👥 Customer Segmentation — End-to-End Data Science Project

**Unsupervised Learning · K-Means Clustering · Supervised Classification · Full-Stack Deployment**

[![Try the Live App](https://img.shields.io/badge/🚀_Try_the_Live_App-Click_Here-28a745?style=for-the-badge&logoColor=white)](https://customer-segmentation-app-production.up.railway.app)

A production-ready data science pipeline that discovers natural customer groups from a real-world marketing dataset, evaluates three clustering algorithms, selects the best model, and deploys a live segment predictor — all in one cohesive project.

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Home.png" width="720"/>

<br/>

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [EDA — Key Findings](#-eda--key-findings)
- [Model Building & Evaluation](#-model-building--evaluation)
- [Final Customer Segments](#-final-customer-segments)
- [Classification Model for Deployment](#-classification-model-for-deployment)
- [App Preview](#-app-preview)
- [Project Structure](#-project-structure)
- [Tech Stack](#️-tech-stack)
- [Setup & Installation](#️-setup--installation)
- [Running the App](#-running-the-app)
- [Contributors](#-contributors)
- [License](#-license)

---

## 📌 Overview

Customer segmentation is the strategic practice of dividing a customer base into distinct groups sharing common characteristics. This project implements an **end-to-end machine learning pipeline** that:

1. Performs thorough **Exploratory Data Analysis (EDA)** on a marketing campaign dataset  
2. Evaluates three clustering algorithms — **K-Means**, **Hierarchical (Ward)**, and **DBSCAN**  
3. Selects the best-performing model based on silhouette scores and business interpretability  
4. Labels all customers with **4 behavioral personas**  
5. Trains a **supervised classifier** (Logistic Regression, **99.55% test accuracy**) on the cluster labels for real-time prediction  
6. Deploys the full pipeline as an interactive **web application**

---

## 🎯 Problem Statement

Modern businesses struggle to deliver personalized experiences at scale. A one-size-fits-all marketing strategy leads to wasted budget, poor engagement, and missed revenue. This project addresses that by:

- Identifying **natural, data-driven customer groupings** from behavioral signals
- Quantifying the key traits that define each customer segment
- Providing a **deployable prediction tool** that classifies any new customer in real time

---

## 📊 Dataset

| Property | Details |
|---|---|
| **Source File** | `marketing_campaign.xlsx` |
| **Total Records** | ~2,236 customers |
| **Final Records** | 2,236 (after cleaning) |

### Feature Categories

| Category | Features |
|---|---|
| **Demographics** | `Year_Birth` → Age, `Income`, `Education`, `Marital_Status` |
| **Household** | `Kidhome`, `Teenhome` → `Total_Dependents` |
| **Purchase Behavior** | `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds` → `Total_Spend` |
| **Purchase Channels** | `NumWebPurchases`, `NumCatalogPurchases`, `NumStorePurchases` → `Total_Purchases` |
| **Engagement** | `NumWebVisitsMonth`, `NumDealsPurchases`, `AcceptedCmp1–5`, `Response` → `Total_Campaigns_Accepted` |
| **Recency** | `Recency` (days since last purchase) |

<div align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Data Explorer.png" width="720"/>

<sub><b>Data Explorer</b> — Browse, filter, and inspect the full customer dataset</sub>

</div>

---

## 🔬 Methodology

```
Raw Data → EDA → Preprocessing → Feature Engineering → Scaling
    → Clustering (K-Means / Hierarchical / DBSCAN)
    → Model Selection → Cluster Labeling
    → Supervised Classification → Deployment
```

---

## 🔍 EDA — Key Findings

### 1. Data Quality

| Issue | Action Taken |
|---|---|
| 24 missing `Income` values | Filled with **median income** |
| 4 extreme outliers (age/income) | **Removed** to prevent skewing clusters |
| 2 constant columns | **Dropped** (carry no information) |
| Categorical encoding | Categoricals cleaned, grouped, and label-encoded |

### 2. Customer Profile

- **Age:** Most customers fall in the **45–70** age range (older, established demographic)
- **Education:** Majority are **Graduates**; Post-graduates significant too
- **Relationship:** ~**65%** are partnered (Married/Together)
- **Household:** ~**72%** are parents with at least one dependent child

### 3. Spending Patterns

- 🍷 **Wine + Meat = ~75% of total revenue** — dominant product categories
- 💰 **Income** is the strongest positive predictor of total spending
- 👶 **Dependents** suppress spending (budget diverted to household costs)
- 📊 Spending distributions are **right-skewed** — a small cohort of high spenders drives disproportionate revenue

### 4. Purchase Channels

- 🏪 **In-store purchases** are the most common channel overall
- 📦 **Catalog buyers** are the highest-spending (premium buyer profile)
- 🌐 Web and deal purchases are predominantly used by budget-sensitive segments

### 5. Campaign Performance

- 📉 Campaign acceptance rates are **very low (1–7%)** across all 5 campaigns
- 💎 Campaign **responders** have measurably higher income and total spend than non-responders
- 🎯 Campaigns are most effective when targeted at high-income segments

---

## 📈 Model Building & Evaluation

### K-Means — Elbow & Silhouette Analysis

<div align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Model 1 .png" width="720"/>

<sub><b>Left:</b> Elbow Method — inertia flattens around K=4 &nbsp;|&nbsp; <b>Right:</b> Silhouette Score peaks at K=4</sub>

</div>

<br/>

| K | Silhouette Score |
|:---:|:---:|
| 2 | 0.2227 |
| 3 | 0.1581 |
| **4** | **0.1783** ✅ |
| 5 | 0.1535 |
| 6 | 0.1547 |
| 7 | 0.1331 |
| 8 | 0.1310 |
| 9 | 0.1309 |
| 10 | 0.1371 |

> K=4 sits at a **local silhouette peak** and the elbow curve shows a clear inflection — confirming **4 as the optimal cluster count**.

---

### Hierarchical Clustering (Ward Linkage)

<div align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/ Model 2.png" width="720"/>

<sub><b>Dendrogram</b> — The red dashed line shows where cutting the tree yields 4 clusters</sub>

</div>

<br/>

| K | Silhouette Score | Cluster Sizes |
|:---:|:---:|---|
| 2 | 0.2312 | [1726, 510] |
| 3 | 0.1354 | [829, 510, 897] |
| **4** | **0.1434** | [510, 659, 897, 170] |

---

### DBSCAN

| Parameter | Value |
|---|---|
| Best `eps` | 2.5 |
| Best `min_samples` | 15 |
| Clusters found | 3 |
| Noise points | 123 (5.5%) |
| Silhouette Score | 0.1539 |
| Cluster Sizes | [1866, 117, 130] |

---

### Model Comparison — Cluster Visualization (PCA 2D)

<div align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Model Comparison.png" width="720"/>

<sub><b>K-Means</b> vs <b>Hierarchical Ward</b> vs <b>DBSCAN</b> — cluster shapes and separation in PCA space</sub>

</div>

<br/>

> **Verdict:** K-Means produces the most **balanced, interpretable, and business-useful** segmentation for this dataset. **K-Means with K=4 is selected as the final model.**

---

## 🎯 Final Customer Segments

All 2,236 customers were labeled with one of four behavioral personas using the final K-Means model.

<div align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Final Cluster Visualization (PCA 2D).png" width="720"/>

<sub><b>Final Segmentation</b> — PCA 2D scatter with centroids (✕) colored by customer persona</sub>

</div>

<br/>

### Cluster Profiles

| Cluster | Label | Size | Share |
|:---:|---|:---:|:---:|
| 0 | 🟠 **Deal-Seeking Parents** | 409 | 18.3% |
| 1 | 🔵 **Budget-Conscious** | 973 | 43.5% |
| 2 | 🟢 **High-Value** | 627 | 28.0% |
| 3 | 🔴 **Premium Loyal** | 227 | 10.2% |

---

<table>
<tr>
<td width="50%" align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Deal-Seeking.png" width="360"/>

**🟠 Cluster 0 — Deal-Seeking Parents**

Middle-income parents who actively hunt for deals

| Metric | Value |
|---|---|
| Income | $52,515 |
| Total Spend | $605 |
| Dependents | 1.5 |
| Campaigns | 0.21 |
| Deals | 5.3 |

*→ Bundle deals, family promos, loyalty rewards*

</td>
<td width="50%" align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Budget-Conscious.png" width="360"/>

**🔵 Cluster 1 — Budget-Conscious**

The largest segment — low income & spend, minimal engagement

| Metric | Value |
|---|---|
| Income | $34,054 |
| Total Spend | $97 |
| Dependents | 1.2 |
| Campaigns | 0.08 |
| Deals | 1.8 |

*→ Discount campaigns, budget product lines*

</td>
</tr>
<tr>
<td width="50%" align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/High-Value.png" width="360"/>

**🟢 Cluster 2 — High-Value**

High earners, strong multi-channel spending

| Metric | Value |
|---|---|
| Income | $70,207 |
| Total Spend | $1,066 |
| Dependents | 0.5 |
| Campaigns | 0.22 |
| Deals | 1.6 |

*→ Cross-sell, upsell, new product launches*

</td>
<td width="50%" align="center">

<img src="Customer Segmentation Data Science Project Files/data_card/Assets/Premium-Loyal.png" width="360"/>

**🔴 Cluster 3 — Premium Loyal**

Top-tier customers — highest spend AND highest engagement

| Metric | Value |
|---|---|
| Income | $77,237 |
| Total Spend | $1,517 |
| Dependents | 0.2 |
| Campaigns | 1.59 |
| Deals | 1.3 |

*→ VIP programs, exclusive access, personalized outreach*

</td>
</tr>
</table>

---

### Saved Artifacts

| File | Contents | Used For |
|---|---|---|
| `scaler.pkl` | Trained `StandardScaler` (means & std devs) | Scaling any new customer input |
| `kmeans_model.pkl` | Trained K-Means model (4 centroids) | Predicting segment for new customers |
| `customers.csv` | Full dataset + `Cluster` + `Cluster_Label` columns | Final reporting & app data source |

---

## 🤖 Classification Model for Deployment

To enable **real-time prediction** on new customers, a supervised classifier was trained using the K-Means cluster labels as ground truth.

> 💡 **Why a Classifier on Top of Clustering?** K-Means can't classify a new, unseen customer without re-running the full pipeline. A trained classifier replicates this mapping instantly — with confidence scores.

### Models Evaluated

| Model | Rationale |
|---|---|
| **Logistic Regression** | Simple baseline; gives probabilities; highly interpretable |
| **Random Forest** | Handles non-linear boundaries; built-in feature importance |
| **Gradient Boosting** | Often best accuracy; sequential error correction |
| **SVM (RBF Kernel)** | Good with scaled data; captures complex decision boundaries |

### Cross-Validation Results (5-Fold)



| Model | Accuracy (mean ± std) | F1-Weighted (mean ± std) |
|---|:---:|:---:|
| **Logistic Regression** | **0.9771 ± 0.0059** ✅ | **0.9773 ± 0.0058** ✅ |
| Random Forest | 0.9575 ± 0.0074 | 0.9572 ± 0.0074 |
| Gradient Boosting | 0.9541 ± 0.0063 | 0.9541 ± 0.0062 |
| SVM (RBF) | 0.9625 ± 0.0076 | 0.9631 ± 0.0073 |

> **Logistic Regression achieves 97.71% accuracy** — the highest of all four models — making it the selected deployment classifier.

---

### 📊 Test Set Performance

After hyperparameter tuning with `GridSearchCV`, the final Logistic Regression model achieves:

| Metric | Score |
|---|:---:|
| **Test Accuracy** | **0.9955** |
| **Test F1 Weighted** | **0.9956** |

#### Classification Report

```
                      precision    recall  f1-score   support

    Budget-Conscious     1.0000    0.9897    0.9948       195
Deal-Seeking Parents     0.9762    1.0000    0.9880        82
          High-Value     1.0000    1.0000    1.0000       126
       Premium Loyal     1.0000    1.0000    1.0000        45

            accuracy                         0.9955       448
           macro avg     0.9940    0.9974    0.9957       448
        weighted avg     0.9956    0.9955    0.9956       448
```

> 🏆 **99.55% accuracy** on unseen test data — with **perfect precision & recall** on High-Value and Premium Loyal segments. Only 2 misclassifications out of 448 test samples.

---

### Classification Pipeline Design

| Step | What We Did | Why |
|---|---|---|
| **Data Source** | Used K-Means cluster labels as ground truth | Clusters discovered the segments; the classifier learns to replicate them |
| **Train/Test Split** | 80/20 stratified split | Preserves class ratios, especially for minority Premium Loyal (10%) |
| **Scaling** | `StandardScaler` fitted on train only | Prevents data leakage; consistent with the clustering pipeline |
| **Model Selection** | 4-way cross-validation comparison | Objective algorithm selection without cherry-picking |
| **Hyperparameter Tuning** | `GridSearchCV` | Extracts the last few % of performance |
| **Class Imbalance** | `class_weight='balanced'` | Prevents the model from ignoring rare segments |
| **Feature Importance** | Built-in or permutation importance | Business insight: what actually drives segment membership |
| **Confidence Scores** | `predict_proba()` | Handles borderline customers intelligently |

---


## 📁 Project Structure

```
Customer Segmentation Data Science Project/
│
├── README.md                                        # ← You are here
│
├── Customer Segmentation Data Science Project Files/
│   │
│   ├── jupyter_notebooks/
│   │   └── Customer_Segmentation_Final.ipynb        # Full EDA → Clustering → Classification pipeline
│   │
│   ├── artifacts/
│   │   ├── kmeans_model.pkl                         # Trained K-Means model (4 centroids)
│   │   └── scaler.pkl                               # Fitted StandardScaler
│   │
│   ├── data_card/
│   │   ├── marketing_campaign.xlsx                  # Raw dataset
│   │   └── Assets/                                  # Visualization previews
│   │
│   └── customer-segmentation-app/                   # Deployed Web Application
│       ├── backend/                                  # FastAPI / Python backend
│       ├── frontend/                                 # HTML/CSS/JS frontend
│       ├── Dockerfile                                # Container configuration
│       ├── requirements.txt                          # Python dependencies
│       └── .env                                      # Environment variables
```

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **Pandas & NumPy** | Data manipulation and numerical computing |
| **Matplotlib & Seaborn** | EDA visualizations and cluster plots |
| **Scikit-learn** | K-Means, Hierarchical, DBSCAN, PCA, GridSearchCV, Logistic Regression |
| **FastAPI** | Backend API serving predictions |
| **Docker** | Container for consistent deployment |
| **MongoDB Atlas** | Cloud database for storing segmented customer records |
| **Pickle** | Model serialization and persistence |

---

## ⚙️ Setup & Installation

### Prerequisites

- Python **3.8+**
- pip package manager
- (Optional) Docker for containerized deployment

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/omkargutal/customer-segmentation-end-to-end.git
cd customer-segmentation-end-to-end
```

**2. Create and activate a virtual environment** *(recommended)*
```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**
```bash
# Copy the example and fill in your values
cp .env.example .env
```

---

## 🚀 Running the App

### Option A — Run Locally

```bash
cd "Customer Segmentation Data Science Project Files/customer-segmentation-app"
uvicorn backend.main:app --reload
```

Open `frontend/index.html` in your browser or visit `http://localhost:8000`.

### Option B — Run with Docker

```bash
cd "Customer Segmentation Data Science Project Files/customer-segmentation-app"
docker build -t customer-segmentation .
docker run -p 8000:8000 --env-file .env customer-segmentation
```

### How to Use

1. Enter customer **demographic details** (Age, Income, Education, Marital Status)  
2. Input **purchase history** (Total Spend, Purchases per channel, Recency)  
3. Provide **engagement data** (Web Visits, Deals Purchased, Campaigns Accepted)  
4. Click **🚀 Predict Segment**  
5. View the predicted **segment label**, **confidence score**, and tailored **marketing recommendations**

---

## 👥 Contributors

**Omkar Gutal**  
**Moin Mohammed**  
**Khushi Choudhari**

---

## 📄 License

This project was developed as part of a professional data science assessment.  
All rights reserved © 2026 Omkar Gutal.
