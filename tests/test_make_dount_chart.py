import pytest
import altair as alt
from utils.charts import make_donut_chart

"""
Módulo de Pruebas para Gráficos de Dona

Este módulo contiene pruebas unitarias para la función `make_donut_chart` en el módulo `utils.charts`.
Las pruebas utilizan la librería `pytest` y `altair` para verificar que el gráfico de dona se genere correctamente
según los datos proporcionados.
"""


@pytest.fixture
def sample_data():
    return {
        "dropout": 10,
        "graduated": 20,
        "enrolled": 30,
    }


def test_make_donut_chart(sample_data):
    """
    Verifica que la función `make_donut_chart` devuelva un objeto de tipo `alt.LayerChart` y
    que el gráfico tenga las capas adecuadas configuradas.
    """
    chart = make_donut_chart(**sample_data)

    assert isinstance(
        chart, alt.LayerChart
    ), "El gráfico devuelto debe ser un 'alt.LayerChart'"

    # Verificar que las capas estén correctamente configuradas
    assert len(chart.layer) == 4, "El gráfico de dona debe tener 4 capas."
