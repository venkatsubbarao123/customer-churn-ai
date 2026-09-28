# Customer Churn AI

A small Streamlit app that estimates customer churn risk with a scikit-learn model.

## Project structure

```text
customer-churn-ai/
├── data/
├── screenshots/
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## Train the model

```bash
python train_model.py
```

The first run creates demo data at `data/customer_churn.csv` and saves the model to `data/churn_model.joblib`.

## Run the app

```bash
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, choose **New app** and select this repository.
3. Set the main file to `app.py` and deploy.

The app includes the model and demo data under `data/`, so no separate setup command is required after deployment.

Replace `data/customer_churn.csv` with a real dataset later. It should contain these columns:

- `tenure_months`
- `monthly_charges`
- `support_calls`
- `contract`
- `has_internet`
- `churn` (0 or 1)
