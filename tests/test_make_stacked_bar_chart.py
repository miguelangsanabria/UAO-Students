import pytest
import altair as alt
from utils.charts import make_stacked_bar_chart


@pytest.fixture
def sample_data():
    return {
        "dropout": 10,
        "graduated": 20,
        "enrolled": 30,
    }


def test_make_stacked_bar_chart(sample_data):
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
