import streamlit as st
import pandas as pd
from io import StringIO
import altair as alt

from catboost import CatBoostClassifier

model = CatBoostClassifier()
model.load_model("catboost_model.cbm")

st.set_page_config(
    page_title="Student Dropout App",
    page_icon="📕",
    layout="wide",
)

course_mapping = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)",
}

prediction_mapping = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}


def make_stack(dropout, graduated, enrolled):
    chart_colors = ["#ef4565", "#27AE60", "#3da9fc"]  # rojo, verde, azul
    total_students = dropout + graduated + enrolled
    data = pd.DataFrame(
        [
            {"Category": "Desertores", "Count": dropout, "Total": "Students"},
            {"Category": "Inscritos", "Count": enrolled, "Total": "Students"},
            {"Category": "Graduados", "Count": graduated, "Total": "Students"},
        ]
    )

    # Crear el gráfico de barras
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x=alt.X(
                "Count", stack="normalize", title=None, axis=alt.Axis(labels=False)
            ),
            y=alt.Y("Total", title=None, axis=alt.Axis(labels=False)),
            color=alt.Color(
                "Category:N",
                scale=alt.Scale(
                    range=chart_colors,
                ),
                legend=None,
            ),
        )
        .configure_axis(grid=False)
    )

    return chart


def make_donut(dropout, graduated, enrolled):
    # Definir colores para cada categoría
    chart_colors = ["#ef4565", "#27AE60", "#3da9fc"]  # rojo, verde, azul
    background_color = "#E0E0E0"  # Color gris para el fondo

    # Calcular el total de estudiantes
    total_students = dropout + graduated + enrolled

    # Crear el DataFrame con los valores
    source = pd.DataFrame(
        {
            "Category": ["Dropout", "Graduated", "Enrolled"],
            "Value": [dropout, graduated, enrolled],
        }
    )

    # DataFrame para el fondo
    source_bg = pd.DataFrame(
        {
            "Category": ["Total"],
            "Value": [total_students],  # Valor total para la dona de fondo
        }
    )

    # Crear el gráfico de dona de fondo
    plot_bg = (
        alt.Chart(source_bg)
        .mark_arc(innerRadius=0, outerRadius=104, cornerRadius=20)
        .encode(
            theta="Value:Q",
            color=alt.value(background_color),  # Color fijo para el fondo
        )
        .properties(width=250, height=250)
    )

    # Crear el gráfico de dona principal
    plot = (
        alt.Chart(source)
        .mark_arc(radius=84, radius2=100, cornerRadius=15, padAngle=0.05)
        .encode(
            theta="Value",
            color=alt.Color(
                "Category:N",
                scale=alt.Scale(
                    domain=["Dropout", "Graduated", "Enrolled"],
                    range=chart_colors,
                ),
                legend=None,
            ),
        )
        .properties(width=250, height=250)
    )

    # Agregar el texto central
    text = (
        alt.Chart(pd.DataFrame({"Total": [total_students], "Label": ["Students"]}))
        .mark_text(
            align="center", baseline="middle", font="sans-serif", fontWeight="bold"
        )
        .encode(text="Total:Q", size=alt.value(48))
        .properties(width=250, height=250)
    )

    # Agregar el texto "Students" más pequeño
    text_label = (
        alt.Chart(
            pd.DataFrame(
                {
                    "Total": [""],  # Texto vacío para centrar la etiqueta
                    "Label": ["Total de Estudiantes"],
                }
            )
        )
        .mark_text(
            align="center",
            baseline="middle",
            dy=28,  # Desplazar hacia abajo
            font="sans-serif",
        )
        .encode(text="Label:N", size=alt.value(12))
        .properties(width=250, height=250)
    )

    return plot_bg + plot + text + text_label


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
    df["Prediction"] = predictions

    df["Prediction Name"] = df["Prediction"].map(prediction_mapping)

    count = df["Prediction"].value_counts()

    dropout_count = count.get(0, 0)
    enrolled_count = count.get(1, 0)
    graduate_count = count.get(2, 0)

    col1, col2 = st.columns([3, 1], vertical_alignment="center")
    with col1:
        with st.container(border=True):
            col11, col12, col13 = st.columns([4.6, 0.2, 10.9])
            with col11:
                donut_chart_greater = make_donut(
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
                        bar_chart_stack = make_stack(
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
        df[["Application mode", "Application order", "Previous qualification", "Admission grade", "Course Name", "Age at enrollment", "Prediction Name"]]
    )  # Muestra columnas relevantes
