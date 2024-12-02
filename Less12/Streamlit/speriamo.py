import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def carica_modello():
    model = joblib.load("titanic_pip.pkl")
    return model

def main():
    st.title("Predizione Sopravvivenza Titanic")
    st.write("Questa app predice se un passeggero è sopravvissuto o meno basandosi sulle variabili inserite.")
    with st.form("form_predizione"):
        
        Pclass = st.selectbox("Classe Passeggero (1=First, 2=Second, 3=Third)", [1, 2, 3])
        Age = st.slider("Età (anni)", 0, 100, 30)
        SibSp = st.number_input("Numero di Fratelli/Coniugi a bordo", min_value=0, max_value=10, step=1, value=0)
        Parch = st.number_input("Numero di Genitori/Figli a bordo", min_value=0, max_value=10, step=1, value=0)
        Fare = st.number_input("Tariffa pagata (£)", min_value=0.0, max_value=500.0, step=0.1, value=30.0)
        Embarked_Q = st.selectbox("Imbarco da Queenstown?", [0, 1])
        Embarked_S = st.selectbox("Imbarco da Southampton?", [0, 1])
        Sex_male = st.selectbox("Sesso (0=Femmina, 1=Maschio)", [0, 1])

submit = st.form_submit_button("Predici Sopravvivenza")

if submit:
        input_data = np.array([["Pclass", "Age", "SibSp", "Parch", "Fare", "Embarked_Q", "Embarked_S", "Sex_male"]])
modello = carica_modello()