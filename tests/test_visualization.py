import pandas as pd
import pytest
from orbea_monegros.visualization import minutes_002040, agruparTiempos, generarHistograma
import os

def test_minutes_002040():
    assert minutes_002040("01:05:30") == "01:00"
    assert minutes_002040("01:25:45") == "01:20"
    assert minutes_002040("01:45:15") == "01:40"

def test_agruparTiempos():
    # Crear un DataFrame de prueba
    datos = {
        "time": ["01:05:30", "01:25:45", "01:45:15"]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    df_agrupado = agruparTiempos(df)
    assert "time_grouped" in df_agrupado.columns
    assert df_agrupado["time_grouped"].tolist() == ["01:00", "01:20", "01:40"]

def test_generarHistograma():
    # Crear un DataFrame de prueba
    datos = {
        "time_grouped": ["01:00", "01:20", "01:00", "01:40", "01:20"]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    rutaSalida = "test_histograma.png"
    generarHistograma(df, "time_grouped", rutaSalida)

    # Verificar que el archivo se generó
    assert os.path.exists(rutaSalida)

    # Eliminar el archivo de prueba
    os.remove(rutaSalida)