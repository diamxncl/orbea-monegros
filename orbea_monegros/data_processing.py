import pandas as pd

def importarConjuntoDatos(rutaArchivo):
    """
    Importar el conjunto de datos en un DataFrame de Pandas.

    Args:
        rutaArchivo (str): Ruta al archivo del conjunto de datos.

    Returns:
        pd.DataFrame: DataFrame importado.
    """
    try:
        conjuntoDatos = pd.read_csv(rutaArchivo, delimiter=";")
        return conjuntoDatos
    except Exception as error:
        print(f"Error al importar el conjunto de datos: {error}")
        return None

def mostrarPrimerasFilas(conjuntoDatos, numeroFilas=5):
    """
    Mostrar las primeras `numeroFilas` filas del DataFrame.

    Args:
        conjuntoDatos (pd.DataFrame): El DataFrame a mostrar.
        numeroFilas (int): Número de filas a mostrar. Por defecto, 5.

    Returns:
        pd.DataFrame: Las primeras `numeroFilas` filas del DataFrame.
    """
    return conjuntoDatos.head(numeroFilas)

def contarCiclistas(conjuntoDatos):
    """
    Contar el número de ciclistas en el conjunto de datos.

    Args:
        conjuntoDatos (pd.DataFrame): El DataFrame a analizar.

    Returns:
        int: Número de ciclistas.
    """
    return len(conjuntoDatos)

def obtenerColumnas(conjuntoDatos):
    """
    Obtener los nombres de las columnas del DataFrame.

    Args:
        conjuntoDatos (pd.DataFrame): El DataFrame a analizar.

    Returns:
        list: Lista de nombres de las columnas.
    """
    return conjuntoDatos.columns.tolist()