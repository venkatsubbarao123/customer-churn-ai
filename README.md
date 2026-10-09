
````markdown
# 🚨 Customer Churn AI

> An AI-powered customer churn prediction application built with **Python, Scikit-learn, Pandas, and Streamlit** to estimate whether a customer is likely to leave a service.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://ai-customer-churns.streamlit.app/)

---

## 🚀 Live Demo

👉 **[Try Customer Churn AI Live] https://ai-customer-churns.streamlit.app

---

## 📌 Project Overview

Customer churn prediction is a machine learning problem that identifies customers who may stop using a company's service.

This project provides an interactive **Streamlit web application** that takes customer information and estimates churn risk using a trained Scikit-learn model.

The application demonstrates a complete machine learning workflow:

```text
Customer Data
      ↓
Data Preparation
      ↓
Feature Processing
      ↓
Machine Learning Model
      ↓
Churn Prediction
      ↓
Risk Probability
      ↓
Streamlit Dashboard
````

---

## 🎯 Project Objectives

* Predict whether a customer is likely to churn
* Estimate customer churn probability
* Build an interactive ML web application
* Demonstrate end-to-end machine learning workflow
* Provide a simple interface for customer risk analysis

---

## 🤖 Machine Learning

The project uses a Scikit-learn classification model trained on customer information.

### Input Features

The application uses:

* **Tenure** — customer relationship duration in months
* **Monthly Charges** — customer's monthly service charges
* **Support Calls** — number of customer support calls
* **Contract Type** — customer's contract category
* **Internet Service** — whether the customer has internet service

### Target Variable

```text
churn
```

Where:

```text
0 → Customer is not expected to churn
1 → Customer is expected to churn
```

---

## 📊 Prediction Output

The application provides:

```text
Churn Prediction
Churn Probability
Risk Level
```

Example:

```text
Prediction: Customer likely to churn

Churn Probability: 82.4%

Risk Level: High
```

---

## 🛠️ Technology Stack

### Programming

* Python

### Data & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Joblib

### Web Application

* Streamlit

### Development Tools

* VS Code
* Jupyter / Python
* Git
* GitHub

---

## 📁 Project Structure

```text
customer-churn-ai/
│
├── data/
│   ├── customer_churn.csv
│   └── churn_model.joblib
│
├── screenshots/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/venkatsubbarao123/customer-churn-ai.git
```

### 2. Open the Project

```bash
cd customer-churn-ai
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Run:

```bash
python train_model.py
```

The training script creates the demo dataset if required and saves the trained model to:

```text
data/churn_model.joblib
```

The dataset is stored at:

```text
data/customer_churn.csv
```

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

> `localhost:8501` is only for local testing. The public application is available through the Live Demo link above.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Production Application

👉 **[Customer Churn AI — Live Demo](https://ai-customer-churns.streamlit.app/)**

The deployment uses:

```text
Repository: customer-churn-ai
Branch: main
Entry Point: app.py
```

---

## 📈 Model Performance

The current model training run achieved:

```text
Accuracy: 78.7%
```

The model is intended as a portfolio/educational machine learning application and should not be treated as a production customer-retention decision system without further validation.

---

## 🔄 Machine Learning Workflow

```text
Raw Customer Data
       ↓
Data Loading
       ↓
Data Preprocessing
       ↓
Feature Encoding
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Serialization
       ↓
Streamlit Application
       ↓
Customer Churn Prediction
```

---

## 📌 Dataset

The project currently uses a **demo customer churn dataset** generated for the application.

Expected columns:

```text
tenure_months
monthly_charges
support_calls
contract
has_internet
churn
```

Target:

```text
churn
```

The dataset can later be replaced with a real-world customer churn dataset containing the same required fields or an appropriately adapted preprocessing pipeline.

---

## 💼 Business Use Case

Customer churn prediction can help organizations identify customers who may be at higher risk of leaving.

Potential applications include:

* Customer retention
* Support prioritization
* Customer segmentation
* Retention campaigns
* Service improvement
* Customer experience analysis

The model provides a prediction that can be used as an analytical signal rather than a guaranteed outcome.

---

## 🧠 Skills Demonstrated

### Python

* Python programming
* File handling
* Data processing
* Modular scripts

### Machine Learning

* Classification
* Feature preprocessing
* Model training
* Model evaluation
* Probability prediction
* Model serialization

### Data Science

* Pandas
* NumPy
* Dataset preparation
* Feature analysis

### Deployment

* Streamlit
* Git
* GitHub
* Streamlit Community Cloud

---

## 👨‍💻 Author

**CH. Venkata Subba Rao**

Python Developer | AI/ML | Python | Scikit-learn | Streamlit

GitHub:

[https://github.com/venkatsubbarao123](https://github.com/venkatsubbarao123)

---

## ⭐ Project Links

🔗 **GitHub Repository**

[https://github.com/venkatsubbarao123/customer-churn-ai](https://github.com/venkatsubbarao123/customer-churn-ai)

🚀 **Live Demo**

[https://ai-customer-churns.streamlit.app/](https://ai-customer-churns.streamlit.app/)
