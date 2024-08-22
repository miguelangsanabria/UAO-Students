import pytest
import altair as alt
from utils.charts import make_donut_chart


@pytest.fixture
def sample_data():
    return {
        "dropout": 10,
        "graduated": 20,
        "enrolled": 30,
    }


def test_make_donut_chart(sample_data):
    chart = make_donut_chart(**sample_data)

    assert isinstance(
        chart, alt.LayerChart
    ), "El gráfico devuelto debe ser un 'alt.LayerChart'"

    # Verificar que las capas estén correctamente configuradas
    assert len(chart.layer) == 4, "El gráfico de dona debe tener 4 capas."
