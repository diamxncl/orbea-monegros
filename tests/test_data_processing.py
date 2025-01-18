import pandas as pd
import pytest
from orbea_monegros.data_processing import (
    importarConjuntoDatos,
    mostrarPrimerasFilas,
    contarCiclistas,
    obtenerColumnas
)

def test_importarConjuntoDatos():
    # Crear un archivo CSV de ejemplo
    datos = "dorsal;biker;club;time\n1;John Doe;Club A;01:20:30\n2;Jane Roe;Club B;00:50:15"
    with open("test_dataset.csv", "w") as f:
        f.write(datos)

    # Probar la función
    df = importarConjuntoDatos("test_dataset.csv")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["dorsal", "biker", "club", "time"]


def test_mostrarPrimerasFilas():
    df = pd.DataFrame({
        "dorsal": [1, 2, 3],
        "biker": ["John", "Jane", "Alice"],
        "club": ["Club A", "Club B", "Club C"],
        "time": ["01:20:30", "00:50:15", "02:10:00"]
    })
    resultado = mostrarPrimerasFilas(df, 2)
    assert len(resultado) == 2


def test_contarCiclistas():
    df = pd.DataFrame({"dorsal": [1, 2, 3]})
    assert contarCiclistas(df) == 3


def test_obtenerColumnas():
    df = pd.DataFrame({"dorsal": [1, 2, 3], "biker": ["John", "Jane", "Alice"]})
    assert obtenerColumnas(df) == ["dorsal", "biker"]
