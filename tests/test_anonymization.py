import pandas as pd
import pytest
from orbea_monegros.anonymization import name_surname, eliminarCiclistasSinTiempo, recuperarCiclista

def test_name_surname():
    # Crear un DataFrame de prueba
    datos = {
        "biker": ["John Doe", "Jane Roe"]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    df_anonimizado = name_surname(df, "biker")
    assert "biker" in df_anonimizado.columns
    assert all(isinstance(nombre, str) for nombre in df_anonimizado["biker"])
    assert len(df_anonimizado) == 2
    assert df_anonimizado["biker"].iloc[0] != "John Doe"


def test_eliminarCiclistasSinTiempo():
    # Crear un DataFrame de prueba
    datos = {
        "dorsal": [1, 2, 3],
        "time": ["00:00:00", "01:10:15", "00:00:00"]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    df_filtrado = eliminarCiclistasSinTiempo(df, "time")
    assert len(df_filtrado) == 1
    assert df_filtrado["dorsal"].iloc[0] == 2
    assert df_filtrado["time"].iloc[0] == "01:10:15"


def test_recuperarCiclista():
    # Crear un DataFrame de prueba
    datos = {
        "dorsal": [1, 2, 3],
        "biker": ["John Doe", "Jane Roe", "Alice Smith"]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    ciclista = recuperarCiclista(df, 2, "dorsal")
    assert not ciclista.empty
    assert ciclista.iloc[0]["biker"] == "Jane Roe"