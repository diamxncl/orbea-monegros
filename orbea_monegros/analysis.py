import pandas as pd

def ciclistasDeClub(conjuntoDatos, clubNombre):
    """
    Filtrar ciclistas que pertenecen a un club específico.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas.
        clubNombre (str): Nombre limpio del club a filtrar.

    Returns:
        pd.DataFrame: DataFrame con los ciclistas que pertenecen al club indicado.
    """
    return conjuntoDatos[conjuntoDatos["club_clean"] == clubNombre]

def mejorTiempoClub(conjuntoDatos):
    """
    Obtener al ciclista con el mejor tiempo en el club.
    
    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas de un club.

    Returns:
        pd.Series: Fila del DataFrame correspondiente al ciclista con el mejor tiempo.
    """
    return conjuntoDatos.loc[conjuntoDatos["time"].idxmin()]

def posicionYPorcentaje(conjuntoDatos, ciclista):
    """
    Obtener la posición del ciclista en la clasificación total y su porcentaje.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de todos los ciclistas.
        ciclista (pd.Series): Fila del DataFrame correspondiente al ciclista a analizar.

    Returns:
        tuple: Posición del ciclista (int) y porcentaje sobre el total (float).
    """
    conjuntoDatosOrdenado = conjuntoDatos.sort_values(by="time").reset_index()
    posicion = conjuntoDatosOrdenado[conjuntoDatosOrdenado.index == ciclista.name].index[0] + 1
    porcentaje = (posicion / len(conjuntoDatosOrdenado)) * 100
    return posicion, porcentaje