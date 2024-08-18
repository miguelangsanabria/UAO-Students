import streamlit as st
import pandas as pd
from io import StringIO

from catboost import CatBoostClassifier

model = CatBoostClassifier()
model.load_model("catboost_model.cbm")

uploaded_file = st.file_uploader("Selecciona un Archivo", type="csv")
if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Seleccionar las características que utilizaste para entrenar el modelo
    # Supongamos que estas son las columnas que utilizaste
    X = df[
        [
            "Application mode",
            "Application order",
            "Course",
            "Previous qualification",
            "Nacionality",
            "Mother's qualification",
            "Father's qualification",
            "Mother's occupation",
            "Father's occupation",
            "Displaced",
            "Debtor",
            "Tuition fees up to date",
            "Gender",
            "Scholarship holder",
            "Age at enrollment",
            "Curricular units 1st sem (credited)",
            "Curricular units 1st sem (enrolled)",
            "Curricular units 1st sem (evaluations)",
            "Curricular units 1st sem (approved)",
            "Curricular units 1st sem (without evaluations)",
            "Curricular units 2nd sem (credited)",
            "Curricular units 2nd sem (enrolled)",
            "Curricular units 2nd sem (evaluations)",
            "Curricular units 2nd sem (approved)",
            "Curricular units 2nd sem (without evaluations)",
            "Unemployment rate",
            "Inflation rate",
            "GDP",
        ]
    ]

    # Realizar las predicciones
    predictions = model.predict(X)

    # Añadir las predicciones al DataFrame
    df["Predicción Deserción"] = predictions

    st.write("Resultados de las predicciones:")
    st.dataframe(
        df[["Application mode", "Course", "Predicción Deserción"]]
    )  # Muestra columnas relevantes
