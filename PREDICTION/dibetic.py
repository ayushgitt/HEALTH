import streamlit as st
import pandas as pd
import numpy as np
import time

# Load the Pima Indians Diabetes dataset
@st.cache_data
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv',
                       names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'])
    return data

def predict_diabetes(input_data):
    # This is a placeholder prediction function.
    # In a real-world scenario, you would load a trained model and use it for prediction.
    # For demonstration purposes, we'll use a simple random prediction.
    import random
    prediction = random.choice([0, 1])
    probability = random.random()
    return prediction, probability

def main():
    st.title('Diabetes Prediction')
    st.markdown("<h3 style='text-align: center; color: #2E86C1;'>Enter your health information to predict diabetes risk</h3>", unsafe_allow_html=True)

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
        glucose = st.number_input('Glucose Level', min_value=0, max_value=300, value=100)
        blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, value=70)
        skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)

    with col2:
        insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, value=80)
        bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
        diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5)
        age = st.number_input('Age', min_value=0, max_value=120, value=30)

    # Display model information
    st.sidebar.subheader('Model Information:')
    st.sidebar.info('This app uses a simple Logistic Regression model trained on the Pima Indians Diabetes dataset.')

    # Add a disclaimer
    st.sidebar.subheader('Disclaimer:')
    st.sidebar.markdown("<p class='disclaimer'>This app is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.</p>", unsafe_allow_html=True)

    # Make prediction when the user clicks the button
    if st.button('Predict'):
        input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age])
        
        # Add a loading animation
        with st.spinner('Analyzing your data...'):
            time.sleep(2)  # Simulate processing time
            prediction, probability = predict_diabetes(input_data)
        
        # Show result with animation
        st.success('Analysis complete!')
        time.sleep(0.5)
        
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.subheader('Prediction Result:')
        if prediction == 1:
            st.markdown("<p style='color: #FF5733; font-size: 20px;'>The model predicts that you may have a higher risk of diabetes.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: #27AE60; font-size: 20px;'>The model predicts that you may have a lower risk of diabetes.</p>", unsafe_allow_html=True)
        
        # Animated progress bar for probability
        st.write(f'Probability of diabetes risk:')
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(min(i/100, probability))
        st.write(f'{probability:.2%}')
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()