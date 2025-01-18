import pandas as pd
from orbea_monegros.clubs import clean_club, limpiarNombresClubs, agruparPorClub

def test_clean_club():
    # Casos de prueba
    assert clean_club("C.C. Huesca") == "HUESCA"
    assert clean_club("CLUB CICLISTA SARIÑENA") == "SARIÑENA"
    assert clean_club("AGRUPACIÓN CICLISTA OSCENSE") == "OSCENSE"
    assert clean_club("PEÑA CICLISTA ZARAGOZA") == "ZARAGOZA"
    assert clean_club("C.D. BARBASTRO T.T.") == "BARBASTRO"

def test_limpiarNombresClubs():
    # Crear un DataFrame de prueba
    datos = {
        "club": [
            "C.C. Huesca", "CLUB CICLISTA SARIÑENA", "AGRUPACIÓN CICLISTA OSCENSE", "C.D. BARBASTRO T.T."
        ]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    df_limpio = limpiarNombresClubs(df, "club")
    assert "club_clean" in df_limpio.columns
    assert df_limpio["club_clean"].tolist() == ["HUESCA", "SARIÑENA", "OSCENSE", "BARBASTRO"]

def test_agruparPorClub():
    # Crear un DataFrame de prueba
    datos = {
        "club_clean": ["HUESCA", "SARIÑENA", "HUESCA", "OSCENSE", "SARIÑENA", "HUESCA"]
    }
    df = pd.DataFrame(datos)

    # Probar la función
    agrupado = agruparPorClub(df, "club_clean")
    assert len(agrupado) == 3
    assert agrupado.iloc[0]["club_clean"] == "HUESCA"
    assert agrupado.iloc[0]["num_ciclistas"] == 3
    assert agrupado.iloc[1]["club_clean"] == "SARIÑENA"
    assert agrupado.iloc[1]["num_ciclistas"] == 2
    assert agrupado.iloc[2]["club_clean"] == "OSCENSE"
    assert agrupado.iloc[2]["num_ciclistas"] == 1
