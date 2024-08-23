import pandas as pd
import altair as alt

"""
Modulo de Creación de Gráficas

Este módulo proporciona funciones para generar visualizaciones gráficas usando Altair 
para representar datos de estudiantes en riesgo de deserción, graduados y actualmente inscritos.
"""


def make_donut_chart(dropout, graduated, enrolled):
    """
    Crea un gráfico de dona que visualiza la proporción de estudiantes que han desertado, 
    se han graduado y están actualmente inscritos.
    """
    chart_colors = ["#ef4565", "#27AE60", "#3da9fc"]  # rojo, verde, azul
    background_color = "#E0E0E0"

    total_students = dropout + graduated + enrolled

    source = pd.DataFrame(
        {
            "Category": ["Dropout", "Graduated", "Enrolled"],
            "Value": [dropout, graduated, enrolled],
        }
    )

    source_bg = pd.DataFrame(
        {
            "Category": ["Total"],
            "Value": [total_students],
        }
    )

    plot_bg = (
        alt.Chart(source_bg)
        .mark_arc(innerRadius=0, outerRadius=104, cornerRadius=20)
        .encode(
            theta="Value:Q",
            color=alt.value(background_color),
        )
        .properties(width=250, height=250)
    )

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

    text = (
        alt.Chart(pd.DataFrame({"Total": [total_students], "Label": ["Students"]}))
        .mark_text(
            align="center", baseline="middle", font="sans-serif", fontWeight="bold"
        )
        .encode(text="Total:Q", size=alt.value(48))
        .properties(width=250, height=250)
    )

    text_label = (
        alt.Chart(
            pd.DataFrame(
                {
                    "Total": [""],
                    "Label": ["Total de Estudiantes"],
                }
            )
        )
        .mark_text(
            align="center",
            baseline="middle",
            dy=28,
            font="sans-serif",
        )
        .encode(text="Label:N", size=alt.value(12))
        .properties(width=250, height=250)
    )

    return plot_bg + plot + text + text_label


def make_stacked_bar_chart(dropout, graduated, enrolled):
    """
    Crea un gráfico de barras apiladas que visualiza la proporción de estudiantes que han 
    desertado, se han graduado y están actualmente inscritos.
    """
    chart_colors = ["#ef4565", "#27AE60", "#3da9fc"]  # rojo, verde, azul
    total_students = dropout + graduated + enrolled
    data = pd.DataFrame(
        [
            {"Category": "Desertores", "Count": dropout, "Total": "Students"},
            {"Category": "Inscritos", "Count": enrolled, "Total": "Students"},
            {"Category": "Graduados", "Count": graduated, "Total": "Students"},
        ]
    )

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
