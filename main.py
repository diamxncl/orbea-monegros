from orbea_monegros.data_processing import *
from orbea_monegros.anonymization import * 
from orbea_monegros.analysis import *
from orbea_monegros.clubs import *
from orbea_monegros.visualization import *

rutaConjuntoDatos = "data/dataset.csv"

# Importar conjunto de datos
conjuntoDatos = importarConjuntoDatos(rutaConjuntoDatos)

print("\n- - - - - - EDA - - - - - - ")

if conjuntoDatos is not None:
    # Mostrar las primeras filas
    print("\nPrimeras 5 filas del conjunto de datos:")
    print(mostrarPrimerasFilas(conjuntoDatos))
    
    # Contar ciclistas
    print(f"\nNúmero total de ciclistas: {contarCiclistas(conjuntoDatos)}")
    
    # Mostrar columnas
    print(f"\nColumnas: {obtenerColumnas(conjuntoDatos)}")

else:
    print("No se pudo cargar el conjunto de datos. Verifica la ruta y el archivo.")


print("\n- - - - - - Anonimización - - - - - - ")

# Anonimizar ciclistas
conjuntoDatos = name_surname(conjuntoDatos)
print("\nPrimeras filas tras anonimizar:")
print(conjuntoDatos.head())

# Eliminar ciclistas sin tiempo y mostrar los 5 primeros
conjuntoDatos = eliminarCiclistasSinTiempo(conjuntoDatos)
print("\nPrimeras filas tras la eliminación de los ciclistas.")
print(conjuntoDatos.head())
print(f"\nNúmero de ciclistas tras eliminar los que no participaron: {len(conjuntoDatos)}")

# Recuperar datos del ciclista con dorsal 1000
ciclistaDorsal1000 = recuperarCiclista(conjuntoDatos, 1000)
print("\nDatos del ciclista con dorsal 1000:")
print(ciclistaDorsal1000)

print("\n- - - - - - Visualización - - - - - - ")

# Agrupar tiempos
conjuntoDatos = agruparTiempos(conjuntoDatos)
print("\nPrimeras filas con tiempos agrupados:")
print(conjuntoDatos.head())

# Generar histograma
generarHistograma(conjuntoDatos)

print("\n- - - - - - Clubs - - - - - - ")

# Limpiar nombres de clubs
conjuntoDatos = limpiarNombresClubs(conjuntoDatos)
print("\nPrimeras filas con nombres de clubs limpios:")
print(conjuntoDatos.head(15))

# Agrupar por club
agrupamiento = agruparPorClub(conjuntoDatos)
print("\nAgrupamiento de ciclistas por club:")
print(agrupamiento.head())

print("\n- - - - - - Análisis - - - - - - ")

# Ciclistas de la UCSC
ucsCiclistas = ciclistasDeClub(conjuntoDatos, "UCSC")
print("\nCiclistas de la UCSC:")
print(ucsCiclistas)

# Mejor tiempo en la UCSC
mejorTiempo = mejorTiempoClub(ucsCiclistas)
print("\nCiclista con mejor tiempo en la UCSC:")
print(mejorTiempo)

# Posición y porcentaje
posicion, porcentaje = posicionYPorcentaje(conjuntoDatos, mejorTiempo)
print(f"\nEl ciclista con mejor tiempo en la UCSC está en la posición {posicion}, representando el {porcentaje:.2f}% del total.")
