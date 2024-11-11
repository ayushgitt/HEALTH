import streamlit as st
import pandas as pd
import numpy as np
import time

# Load the Heart Disease dataset
@st.cache_data
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    column_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]
    data = pd.read_csv(url, names=column_names, na_values="?")
    data = data.dropna()
    return data

def predict_heart_attack_risk(input_data):
    # This is a placeholder prediction function.
    # In a real-world scenario, you would load a trained model and use it for prediction.
    # For demonstration purposes, we'll use a simple random prediction.
    import random
    prediction = random.choice([0, 1])
    probability = random.random()
    return prediction, probability


def main():
    st.title('Heart Attack Risk Prediction')
    st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Enter your health information to predict heart attack risk</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .main {
        margin-bottom: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age', min_value=20, max_value=100, value=50)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=90, max_value=200, value=120)
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
        restecg = st.selectbox('Resting ECG Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=6.2, value=0.0, step=0.1)
        slope = st.selectbox('Slope of Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=3, value=0)
        thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Make prediction when the user clicks the button
    if st.button('Predict'):
        input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
        # Add a loading animation
        with st.spinner('Analyzing your data...'):
            time.sleep(2)  # Simulate processing time
            prediction, probability = predict_heart_attack_risk(input_data)
        
        # Show result with animation
        st.success('Analysis complete!')
        time.sleep(0.5)
        
        st.markdown("<div class='result-box' style='background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader('Prediction Result:')
        if prediction == 1:
            st.markdown("<p style='color: #E74C3C; font-size: 20px;'>The model predicts that you may have a higher risk of heart disease.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: #27AE60; font-size: 20px;'>The model predicts that you may have a lower risk of heart disease.</p>", unsafe_allow_html=True)
        
        # Animated progress bar for probability
        st.write(f'Probability of heart disease risk:')
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(min(i/100, probability))
        st.write(f'{probability:.2%}')
        st.markdown("</div>", unsafe_allow_html=True)

    # Add footer with app information and disclaimer
   

if __name__ == "__main__":
    main()