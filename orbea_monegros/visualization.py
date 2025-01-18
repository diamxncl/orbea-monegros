import pandas as pd
import matplotlib.pyplot as plt

def minutes_002040(tiempo):
    """
    Agrupar tiempos en intervalos de 20 minutos (00, 20, 40).

    Args:
        tiempo (str): Tiempo en formato hh:mm:ss.

    Returns:
        str: Tiempo agrupado en formato hh:mm.
    """
    horas, minutos, _ = map(int, tiempo.split(":"))
    if minutos < 20:
        minutosAgrupados = "00"
    elif minutos < 40:
        minutosAgrupados = "20"
    else:
        minutosAgrupados = "40"

    return f"{horas:02}:{minutosAgrupados}"

def agruparTiempos(conjuntoDatos):
    """
    Crear una nueva columna con tiempos agrupados en el DataFrame.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con la columna "time".

    Returns:
        pd.DataFrame: DataFrame con la nueva columna "time_grouped".
    """
    conjuntoDatos["time_grouped"] = conjuntoDatos["time"].apply(minutes_002040)
    return conjuntoDatos

def generarHistograma(conjuntoDatos, columnaAgrupada="time_grouped", rutaSalida="img/histograma.png"):
    """
    Generar un histograma a partir de la columna agrupada.

    Args:
        conjuntoDatos (pd.DataFrame): DataFrame con los datos agrupados.
        columnaAgrupada (str): Nombre de la columna con los tiempos agrupados. Por defecto, "time_grouped".
        rutaSalida (str): Ruta donde se guardará la imagen del histograma. Por defecto, "img/histograma.png".

    Returns:
        None
    """
    agrupamiento = conjuntoDatos.groupby(columnaAgrupada).size()
    agrupamiento.sort_index(inplace=True)

    plt.figure(figsize=(10, 6))
    agrupamiento.plot(kind="bar")
    plt.title("Distribución de Ciclistas por Tiempos Agrupados")
    plt.xlabel("Tiempos Agrupados (hh:mm)")
    plt.ylabel("Número de Ciclistas")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(rutaSalida)
    plt.close()
    print("\nHistograma guardado en 'img/histograma.png'.")