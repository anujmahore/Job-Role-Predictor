# Job-Role-Predictor
💼 AI Job Role Predictor

An interactive Machine Learning web app that predicts a suitable job role based on a candidate's skills, qualification, and experience.

🧠 Tech Stack
Python
Pandas, NumPy
Scikit-learn
TF-IDF
Logistic Regression
JupyterLab
Streamlit
🔄 Workflow
Kaggle Dataset
     ↓
Data Preprocessing & EDA
     ↓
TF-IDF
     ↓
Logistic Regression
     ↓
Job Role Prediction
     ↓
Streamlit Web App
✨ Features
Enter candidate skills
Select qualification
Select experience level
Predict job role
View top predictions and probabilities
Interactive Streamlit interface
📊 Dataset

Candidate Job Role Dataset — Kaggle

https://www.kaggle.com/datasets/ckshetty/candidate-job-role-dataset

Dataset is synthetic and intended for educational/portfolio use.

📁 Project Structure
AI-Job-Role-Predictor/
├── candidate_job_role_dataset.csv
├── Job_Role_Prediction.ipynb
├── app.py
├── job_role_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
🚀 How to Run
1. Install dependencies
pip install -r requirements.txt
2. Open JupyterLab
jupyter lab

Run all cells in:

Job_Role_Prediction.ipynb

This creates:

job_role_model.pkl
tfidf_vectorizer.pkl
3. Run Streamlit

Open the JupyterLab terminal:

streamlit run app.py

Then open:

http://localhost:8501
👨‍💻 Author

Anuj Mahore
B.Tech — Computer Science & Engineering
