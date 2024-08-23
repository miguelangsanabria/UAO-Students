import pandas as pd
from models.model_loader import ModelLoader
from config.mappings import prediction_mapping, course_mapping

"""
Módulo de Predicción

Este módulo proporciona funciones para realizar predicciones, enriquecer DataFrames con predicciones, 
y obtener conteos y datos agrupados de predicciones.
"""


def make_predictions(X):
    """
    Realiza predicciones utilizando un modelo cargado.
    """
    model_loader = ModelLoader()
    predictions = model_loader.predict(X)
    return predictions


def enrich_dataframe(df, predictions):
    """
    Enriquese un DataFrame con las predicciones y mapea los nombres de las predicciones y cursos.
    """
    df["Prediction"] = predictions
    df["Prediction Name"] = df["Prediction"].map(prediction_mapping)
    df["Course Name"] = df["Course"].map(course_mapping)
    return df


def get_prediction_counts(df):
    """
    Obtiene el conteo de cada tipo de predicción (desertores, inscritos, graduados).
    """
    counts = df["Prediction"].value_counts().to_dict()
    dropout_count = counts.get(0, 0)
    enrolled_count = counts.get(1, 0)
    graduate_count = counts.get(2, 0)
    return dropout_count, enrolled_count, graduate_count


def get_course_grouped_data(df):
    """
    Agrupa y cuenta los datos por curso y predicción.
    """
    grouped = df.groupby(["Course Name", "Prediction"]).size().unstack(fill_value=0)
    grouped = grouped.rename(columns=prediction_mapping)
    return grouped
