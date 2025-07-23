import streamlit as st
import requests


st.title("📑Score Predicton✅✔️")
study=st.slider("Study Time",0,10)
atd=st.slider("Attended Days",0,80)
gen=st.selectbox("Gender",["Male","Female"])

gender=1 if(gen=="Male") else 0

if (st.button("Predict the score")):
    data={
        "Study_time":study,
        "attendence":atd,
        "gender_Male":gender

    }
    res=requests.post(" http://127.0.0.1:8000/predict",json=data)
    result=res.json()
    st.write("The Predicted Score is", result.get("Predicted_score", "Key not found"))

