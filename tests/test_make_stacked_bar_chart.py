import pytest
import altair as alt
from utils.charts import make_stacked_bar_chart

"""
Módulo de Pruebas para Gráficos de Barras Apiladas

Este módulo contiene pruebas unitarias para la función `make_stacked_bar_chart` en el módulo `utils.charts`.
Las pruebas utilizan la librería `pytest` y `altair` para verificar que el gráfico de barras apiladas
se genere correctamente según los datos proporcionados.
"""


@pytest.fixture
def sample_data():
    return {
        "dropout": 10,
        "graduated": 20,
        "enrolled": 30,
    }


def test_make_stacked_bar_chart(sample_data):
    """
    Verifica que la función `make_stacked_bar_chart` devuelva un objeto de tipo `alt.Chart`,
    que el gráfico sea de tipo 'bar' y que las categorías estén correctamente asignadas.
    """
    chart = make_stacked_bar_chart(**sample_data)

    assert isinstance(chart, alt.Chart), "El gráfico devuelto debe ser un 'alt.Chart'"

    # Verificar que la propiedad 'mark' sea de tipo 'bar'
    assert chart.mark == "bar", "El gráfico debe ser un 'bar chart'."

    # Verificar que las categorías estén correctamente asignadas
    expected_categories = ["Desertores", "Inscritos", "Graduados"]
    actual_categories = chart.data["Category"].tolist()

    assert (
        expected_categories == actual_categories
    ), "Las categorías del gráfico no coinciden con las esperadas."
