import pandas as pd
from io import StringIO
import streamlit as st

"""
Modulo de Carga y Procesamiento de Datos

Este módulo proporciona funciones para cargar y preprocesar datos desde archivos CSV.
"""


def load_csv(uploaded_file):
    """
    Carga un archivo CSV en un DataFrame de pandas.
    """
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None


def preprocess_data(df):
    """
    Preprocesa los datos seleccionando un subconjunto de características relevantes.
    """
    feature_columns = [
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
    X = df[feature_columns]
    return X
