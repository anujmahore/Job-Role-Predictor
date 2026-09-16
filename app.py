import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(
    page_title="AI Job Role Predictor",
    page_icon="💼",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_artifacts():
    with open(BASE_DIR / "job_role_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open(BASE_DIR / "tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

try:
    model, vectorizer = load_artifacts()
except FileNotFoundError:
    st.error(
        "Model files not found. Run all cells in Job_Role_Prediction.ipynb "
        "first so job_role_model.pkl and tfidf_vectorizer.pkl are created."
    )
    st.stop()

st.title("💼 AI Job Role Predictor")
st.write(
    "Enter your skills, qualification, and experience. "
    "The trained ML model predicts a job role."
)

st.divider()

with st.sidebar:
    st.header("👤 Candidate Profile")

    qualification = st.selectbox(
        "Qualification",
        ["High School", "Bachelor's", "Master's", "PhD"]
    )

    experience = st.selectbox(
        "Experience Level",
        ["Entry", "Mid", "Senior"]
    )

st.subheader("🛠️ Your Skills")

skills = st.text_area(
    "Enter skills",
    placeholder="Example: Python, Pandas, NumPy, SQL, Machine Learning",
    height=150
)

st.caption("Separate multiple skills with commas.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    data_science = st.button("📊 Data Science Example", use_container_width=True)

with col2:
    web_dev = st.button("🌐 Web Development Example", use_container_width=True)

with col3:
    ai_ml = st.button("🤖 AI/ML Example", use_container_width=True)

if data_science:
    skills = "Python, Pandas, NumPy, SQL, Machine Learning, Scikit-learn"

if web_dev:
    skills = "HTML, CSS, JavaScript, React, Node.js, Express, MongoDB"

if ai_ml:
    skills = "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, NLP"

st.divider()

if st.button("🚀 Predict Job Role", use_container_width=True):

    if not skills.strip():
        st.warning("Please enter at least one skill.")
        st.stop()

    candidate_text = (
        f"{skills} {qualification} {experience}"
    )

    candidate_vector = vectorizer.transform([candidate_text])

    prediction = model.predict(candidate_vector)[0]

    probabilities = model.predict_proba(candidate_vector)[0]

    result = pd.DataFrame({
        "Job Role": model.classes_,
        "Probability": probabilities
    }).sort_values("Probability", ascending=False)

    st.success(f"### 🎯 Predicted Job Role: {prediction}")

    st.subheader("📊 Top Predictions")

    for _, row in result.head(5).iterrows():
        role = row["Job Role"]
        probability = float(row["Probability"])

        st.write(f"**{role}** — {probability * 100:.2f}%")
        st.progress(probability)

    st.divider()

    st.subheader("👤 Candidate Profile")

    c1, c2 = st.columns(2)

    with c1:
        st.write(f"**Qualification:** {qualification}")

    with c2:
        st.write(f"**Experience:** {experience}")

    st.write(f"**Skills:** {skills}")

st.divider()
st.caption(
    "Educational portfolio project. The Kaggle dataset is synthetic; "
    "predictions should not be treated as professional hiring advice."
)
