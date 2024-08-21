import streamlit as st
from utils.data_loader import load_csv, preprocess_data
from utils.prediction import (
    make_predictions,
    enrich_dataframe,
    get_prediction_counts,
    get_course_grouped_data,
)
from utils.charts import make_donut_chart, make_stacked_bar_chart
from config.mappings import course_mapping

st.set_page_config(
    page_title="Student Dropout App",
    page_icon="📕",
    layout="wide",
)

uploaded_file = st.file_uploader("Selecciona un Archivo", type="csv")
if uploaded_file is not None:

    df = load_csv(uploaded_file)

    X = preprocess_data(df)
    predictions = make_predictions(X)
    df = enrich_dataframe(df, predictions)
    dropout_count, enrolled_count, graduate_count = get_prediction_counts(df)
    course_grouped = get_course_grouped_data(df)

    col1, col2 = st.columns([3, 1], vertical_alignment="center")
    with col1:
        with st.container(border=True):
            col11, col12, col13 = st.columns([4.6, 0.2, 10.9])
            with col11:
                donut_chart_greater = make_donut_chart(
                    dropout=dropout_count,
                    graduated=graduate_count,
                    enrolled=enrolled_count,
                )
                st.altair_chart(donut_chart_greater)
                st.metric(label="🔵 Potenciales Inscritos", value=enrolled_count)
                st.metric(label="🔴 Potenciales Desertores", value=dropout_count)
                st.metric(label="🟢 Potenciales Graduados", value=graduate_count)
            with col12:
                st.html(
                    """
                <div class="divider-vertical-line"></div>
                <style>
                    .divider-vertical-line {
                        border-left: 2px solid rgba(49, 51, 63, 0.2);
                        height: 520px;
                        margin: auto;
                    }
                </style>
            """
                )
            with col13:
                df["Course Name"] = df["Course"].map(course_mapping)
                grouped = (
                    df.groupby(["Course Name", "Prediction"])
                    .size()
                    .unstack(fill_value=0)
                )
                grouped = grouped.rename(
                    columns={0: "Dropout", 1: "Enrolled", 2: "Graduate"}
                )
                with st.container(height=636, border=False):
                    for course in grouped.index:
                        course_dropout_count = grouped.loc[course, "Dropout"]
                        course_enrolled_count = grouped.loc[course, "Enrolled"]
                        course_graduate_count = grouped.loc[course, "Graduate"]
                        st.markdown("Curso")

                        st.markdown(f"### {course}")
                        bar_chart_stack = make_stacked_bar_chart(
                            dropout=course_dropout_count,
                            graduated=course_graduate_count,
                            enrolled=course_enrolled_count,
                        )
                        st.altair_chart(bar_chart_stack, use_container_width=True)
                        st.markdown(
                            f"""
    <div style='display: flex; justify-content: space-between;'>
        <span>{course_dropout_count} desertores</span>
        <span>{course_enrolled_count} inscritos</span>
        <span>{course_graduate_count} graduados</span>
    </div>
    """,
                            unsafe_allow_html=True,
                        )
                        st.markdown("---")

    with col2:
        with st.container(border=True):
            st.header("⚠️ :orange[Atención]")
            st.subheader(
                f":red[{dropout_count}] estudiantes están en riesgo de abandonar sus estudios"
            )
        with st.container(border=True):
            st.header("Información Adicional")
            average_unemployment_rate = df["Unemployment rate"].mean().round(2)
            average_inflation_rate = df["Inflation rate"].mean().round(2)
            average_gdp = df["GDP"].mean().round(2)
            st.metric(
                label="Promedio Tasa de Desemleo", value=average_unemployment_rate
            )
            st.metric(label="Promedio Tasa de Inflación", value=average_inflation_rate)
            st.metric(label="Promedio GDP", value=average_gdp)

    st.write("Información de Estudiantes:")
    st.dataframe(
        df[
            [
                "Application mode",
                "Application order",
                "Previous qualification",
                "Admission grade",
                "Course Name",
                "Age at enrollment",
                "Prediction Name",
            ]
        ]
    )
