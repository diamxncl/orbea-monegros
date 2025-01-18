import pandas as pd
import re

def clean_club(nombreClub):
    """
    Limpiar el nombre del club ciclista siguiendo reglas específicas.

    Args:
        nombreClub (str): Nombre del club a limpiar.

    Returns:
        str: Nombre del club limpio.
    """
    # Convertir a mayúsculas
    nombreClub = nombreClub.upper()

    # Reemplazos globales
    reemplazosGlobales = [
        "PEÑA CICLISTA ", "PENYA CICLISTA ", "AGRUPACIÓN CICLISTA ", "AGRUPACION CICLISTA ",
        "AGRUPACIÓ CICLISTA ", "AGRUPACIO CICLISTA ", "CLUB CICLISTA ", "CLUB "
    ]
    for texto in reemplazosGlobales:
        nombreClub = nombreClub.replace(texto, "")

    # Reemplazos al inicio
    reemplazosInicio = [
        r"^C\.C\. ", r"^C\.C ", r"^CC ", r"^C\.D\. ", r"^C\.D ", r"^CD ",
        r"^A\.C\. ", r"^A\.C ", r"^AC ", r"^A\.D\. ", r"^A\.D ", r"^AD ",
        r"^A\.E\. ", r"^A\.E ", r"^AE ", r"^E\.C\. ", r"^E\.C ", r"^EC ",
        r"^S\.C\. ", r"^S\.C ", r"^SC ", r"^S\.D\. ", r"^S\.D ", r"^SD "
    ]
    for patron in reemplazosInicio:
        nombreClub = re.sub(patron, "", nombreClub)

    # Reemplazos al final
    reemplazosFinal = [
        r" T\.T\.$", r" T\.T$", r" TT$", r" T\.E\.$", r" T\.E$", r" TE$", r" C\.C\.$", r" C\.C$", r" CC$", r" C\.D\.$", r" C\.D$", r" CD$", r" A\.D\.$", r" A\.D$", r" AD$", r" A\.C\.$", r" A\.C$", r" AC$"
    ]
    for patron in reemplazosFinal:
        nombreClub = re.sub(patron, "", nombreClub)

    # Eliminar espacios en blanco al principio y al final
    return nombreClub.strip()

def limpiarNombresClubs(conjuntoDatos, columnaClub="club"):
    """
    Aplicar la limpieza de nombres de clubs a una columna del DataFrame.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas.
        columnaClub (str): Nombre de la columna que contiene los nombres de los clubs. Por defecto, "club".

    Returns:
        pd.DataFrame: DataFrame con una nueva columna "club_clean" con los nombres de clubs limpios.
    """
    conjuntoDatos["club_clean"] = conjuntoDatos[columnaClub].apply(clean_club)
    return conjuntoDatos

def agruparPorClub(conjuntoDatos, columnaClubLimpio="club_clean"):
    """
    Agrupar ciclistas por club limpio y contar el número de participantes.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas.
        columnaClubLimpio (str): Nombre de la columna con los nombres de clubs limpios. Por defecto, "club_clean".

    Returns:
        pd.DataFrame: DataFrame agrupado con el número de participantes por club.
    """
    agrupamiento = conjuntoDatos.groupby(columnaClubLimpio).size().reset_index(name="num_ciclistas")
    return agrupamiento.sort_values(by="num_ciclistas", ascending=False)