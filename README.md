# 🏦 Financial Loan Risk Engine

An end-to-end **Machine Learning** application that predicts loan eligibility using real-world risk factors. This tool demonstrates how banks can use AI to automate the "Level 1" review of loan applications while maintaining strict risk standards.


## 🧠 Model Logic & Risk Factors

This project uses a **Random Forest Classifier** to evaluate applications. Unlike a simple chatbot, this model weights features based on industry standards:

* **Credit History:** The primary predictor of future behavior.
* **Debt-to-Income (DTI) Analysis:** A custom feature-engineered check to ensure the requested loan is serviceable relative to the applicant's monthly income.
* **Education & Employment:** Used to assess the long-term stability of the applicant.

---

## 🛠️ Technical Stack

* **Language:** Python 3.14
* **ML Library:** Scikit-Learn
* **Data Science:** Pandas & NumPy
* **Interface:** Streamlit
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
loan-predictor-ml/
├── app.py              # Main Streamlit web application
├── loan_data.csv       # Dataset used for training the model
├── requirements.txt    # List of dependencies for deployment
├── .gitignore          # Prevents venv and temp files from being uploaded
└── README.md           # Project documentation

```

---

## 🔧 Installation & Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/harshithaanugu5/loan-predictor-ml.git

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the app:**
```bash
streamlit run app.py

```
