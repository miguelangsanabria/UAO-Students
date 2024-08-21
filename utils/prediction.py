import pandas as pd
from models.model_loader import ModelLoader
from config.mappings import prediction_mapping, course_mapping


def make_predictions(X):
    model_loader = ModelLoader()
    predictions = model_loader.predict(X)
    return predictions


def enrich_dataframe(df, predictions):
    df["Prediction"] = predictions
    df["Prediction Name"] = df["Prediction"].map(prediction_mapping)
    df["Course Name"] = df["Course"].map(course_mapping)
    return df


def get_prediction_counts(df):
    counts = df["Prediction"].value_counts().to_dict()
    dropout_count = counts.get(0, 0)
    enrolled_count = counts.get(1, 0)
    graduate_count = counts.get(2, 0)
    return dropout_count, enrolled_count, graduate_count


def get_course_grouped_data(df):
    grouped = df.groupby(["Course Name", "Prediction"]).size().unstack(fill_value=0)
    grouped = grouped.rename(columns=prediction_mapping)
    return grouped
