
import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load("employee_promotion_model.pkl")
columns = joblib.load("feature_columns.pkl")

st.title("employee_promotion_model.pkl")

age = st.slider("Age", 20, 60, 35)

previous_year_rating = st.slider(
    "Previous Year Rating",
    1,
    5,
    3
)

avg_training_score = st.slider(
    "Average Training Score",
    40,
    100,
    60
)

length_of_service = st.slider(
    "Length of Service",
    1,
    30,
    5
)

awards_won = st.selectbox(
    "Awards Won",
    [0,1]
)

no_of_trainings = st.slider(
    "Number of Trainings",
    1,
    10,
    2
)

if st.button("Predict Promotion"):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=columns
    )

    input_df["age"] = age
    input_df["previous_year_rating"] = previous_year_rating
    input_df["avg_training_score"] = avg_training_score
    input_df["length_of_service"] = length_of_service
    input_df["awards_won"] = awards_won
    input_df["no_of_trainings"] = no_of_trainings

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    st.write(
        f"Promotion Probability: {probability:.2%}"
    )

    if probability >= 0.25:
        st.success("Likely To Be Promoted")
    else:
        st.error("Unlikely To Be Promoted")
