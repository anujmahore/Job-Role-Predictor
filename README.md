# 💼 AI Job Role Predictor

An interactive **Machine Learning web application** that predicts a suitable job role based on a candidate's **skills, qualification, and experience level**.

## 🧠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- JupyterLab
- Streamlit

## 🔄 Workflow

**Kaggle Dataset → Data Preprocessing → EDA → TF-IDF → Logistic Regression → Job Role Prediction → Streamlit Web App**

## ✨ Features

- Enter candidate skills
- Select qualification
- Select experience level
- Predict suitable job role
- View top job-role predictions
- View prediction probabilities
- Interactive Streamlit interface

## 📊 Dataset

**Candidate Job Role Dataset — Kaggle**

https://www.kaggle.com/datasets/ckshetty/candidate-job-role-dataset

> The dataset is synthetic and intended for educational and portfolio purposes.

## 📁 Project Structure

```text
AI-Job-Role-Predictor/
│
├── candidate_job_role_dataset.csv
├── Job_Role_Prediction.ipynb
├── app.py
├── job_role_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Open JupyterLab

```bash
jupyter lab
```

Open `Job_Role_Prediction.ipynb` and **Run All Cells**.

This will train the model and create:

```text
job_role_model.pkl
tfidf_vectorizer.pkl
```

### 3. Run Streamlit App

Open the **JupyterLab Terminal** and run:

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

## 👨‍💻 Author

**Anuj Mahore**

B.Tech — Computer Science & Engineering
