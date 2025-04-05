# 🩺 Diabetic Predictor

A machine learning-based web application that predicts whether a person is diabetic or not using essential health-related features. Built using Python, trained on the **Kaggle Diabetes Dataset**, and deployed with a **Streamlit UI** for an interactive and easy-to-use experience.

---

## 📊 Dataset

- **Source**: [Kaggle - Diabetes Dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)
- **Features Used**:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- **Target Variable**: `Outcome` (1: Diabetic, 0: Non-Diabetic)

---

## ⚙️ Features

- Cleaned and preprocessed dataset.
- Built and trained a classification model (e.g., Logistic Regression, Random Forest, etc.).
- Evaluated model performance using accuracy, precision, recall, and F1-score.
- Streamlit-based UI for easy prediction.
- Simple and clean interface to input user health data and get predictions instantly.

---

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/diabetic-predictor.git
cd diabetic-predictor
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install dependencies
```bash
pip install -r streamlit_app/requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

# 🧠 Machine Learning Model

- **Model Used:** Logistic Regression
- **Testing Accuracy:** 78.57%

---

# 🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.


