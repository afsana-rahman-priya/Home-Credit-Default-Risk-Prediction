
# 🏦 Home Credit Default Risk Prediction

A machine learning project that predicts whether a loan applicant is likely to default on repayment using the Home Credit Default Risk dataset. The project focuses on data preprocessing, feature engineering, model development, evaluation, and deployment using FastAPI and Docker.

---

## 📌 Project Overview

Financial institutions need accurate risk assessment to make informed lending decisions. This project develops a predictive model that estimates the probability of loan default based on applicants' financial and historical credit information.

The complete workflow includes:

- Data preprocessing
- Feature engineering
- Handling missing values
- Model training and evaluation
- API deployment using FastAPI
- Docker containerization

---

## 🎯 Objectives

- Predict customer loan default risk.
- Perform extensive data cleaning and preprocessing.
- Engineer meaningful features from multiple related datasets.
- Compare different machine learning models.
- Select the best-performing model using ROC-AUC.
- Deploy the trained model as a REST API.

---

## 📂 Dataset

This project uses the **Home Credit Default Risk** dataset from Kaggle.

**Dataset Source**

https://www.kaggle.com/competitions/home-credit-default-risk

**Note**

The dataset is **not included** in this repository due to Kaggle's licensing terms and file size limitations.

---

## 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Matplotlib
- Seaborn

### Deployment

- FastAPI
- Docker

---

## 📊 Data Preprocessing

The following preprocessing steps were performed:

- Handling missing values
- Label encoding for categorical features
- Aggregating multiple relational datasets
- Feature engineering
- Dataset merging
- Data cleaning

---

## 📈 Feature Engineering

Features were generated from multiple datasets, including:

- Bureau records
- Previous applications
- Installment payments
- Credit card balance
- POS cash balance

Aggregated statistical features were created to improve model performance.

---

## 🤖 Machine Learning Models

The following models were evaluated:

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

LightGBM achieved the best overall performance and was selected as the final model.

---

## 📊 Model Performance

| Metric | Value |
|---------|------:|
| ROC-AUC Score | **0.77545** |

Additional evaluation metrics include:

- Confusion Matrix
- Classification Report
- ROC Curve

---

## 📷 Results

### ROC Curve

![ROC Curve](ROC.PNG)

### Confusion Matrix

![Confusion Matrix](CONFUSIONMatrix.png)

---

## 🚀 Deployment

The trained model is deployed using:

- FastAPI
- Docker

The API accepts customer information and returns:

- Predicted class
- Default probability

---

## 📁 Project Structure

```
Home-Credit-Default-Risk-Prediction
│
├── README.md
├── requirements.txt
│
├── notebook
│   └── Home_Credit_Default_Risk.ipynb
│
├── deployment
│   ├── Dockerfile
│   └── main.py
│
├── images
│   ├── roc_curve.png
│   └── confusion_matrix.png
│
└── data
    └── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Home-Credit-Default-Risk-Prediction.git
```

Move into the project directory

```bash
cd Home-Credit-Default-Risk-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI application

```bash
uvicorn main:app --reload
```

---

## 📌 Future Improvements

- Hyperparameter optimization
- Explainability using SHAP
- Interactive dashboard using Streamlit
- Cloud deployment
- Automated model retraining

---

## 👩‍💻 Author

**Afsana Rahman Priya**

- MSc in Computer Science & Engineering (Data Science)
- BRAC University

---

## ⭐ If you found this project useful, consider giving it a star.
