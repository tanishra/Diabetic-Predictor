import streamlit as st
import numpy as np
import pickle

# Load the trained model and scaler
with open("diabetes_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit UI
def main():
    st.title("Diabetes Prediction System")
    st.write("Enter the following details to predict diabetes risk:")
    
    # Input features
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=80)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=79)
    bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=25.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    
    # Prediction button
    if st.button("Predict Diabetes"):
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
        
        st.success(f"Prediction: {result}")

if __name__ == "__main__":
    main()
