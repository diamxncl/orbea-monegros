from faker import Faker
import pandas as pd

def name_surname(conjuntoDatos, columnaNombre="biker"):
    """
    Anonimizar los nombres de los ciclistas utilizando la librería Faker.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas.
        columnaNombre (str): Nombre de la columna que contiene los nombres a anonimizar. Por defecto, "biker".

    Returns:
        pd.DataFrame: DataFrame con los nombres anonimizados.
    """
    faker = Faker()
    Faker.seed(42)  # Para resultados reproducibles

    conjuntoDatos[columnaNombre] = conjuntoDatos[columnaNombre].apply(
        lambda _: f"{faker.first_name()} {faker.last_name()}"
    )
    return conjuntoDatos

def eliminarCiclistasSinTiempo(conjuntoDatos, columnaTiempo="time"):
    """
    Eliminar los ciclistas que no participaron en la carrera (tiempo igual a "00:00:00").

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas.
        columnaTiempo (str): Nombre de la columna que contiene los tiempos. Por defecto, "tiempo".

    Returns:
        pd.DataFrame: DataFrame sin los ciclistas que no participaron.
    """
    return conjuntoDatos[conjuntoDatos[columnaTiempo] != "00:00:00"].reset_index(drop=True)

def recuperarCiclista(conjuntoDatos, dorsal, columnaDorsal="dorsal"):
    """
    Recuperar los datos de un ciclista específico por su dorsal.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos de los ciclistas.
        dorsal (int): Dorsal del ciclista a buscar.
        columnaDorsal (str): Nombre de la columna que contiene los dorsales. Por defecto, "dorsal".

    Returns:
        pd.Series: Fila del DataFrame correspondiente al ciclista encontrado.
    """
    return conjuntoDatos[conjuntoDatos[columnaDorsal] == dorsal]
