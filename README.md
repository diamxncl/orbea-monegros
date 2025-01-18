# Orbea Monegros - PEC 4 - Programación para la Ciencia de Datos

## Descripción
Este proyecto tiene como objetivo analizar los datos de la prueba ciclista **Orbea Monegros 2024**, una carrera de ciclismo de montaña no competitiva celebrada en Sariñena (Huesca). Utilizando herramientas de Python, procesamos los datos para obtener información relevante sobre los ciclistas, sus tiempos y los clubs participantes.

## Requisitos del sistema
- **Python**: Versión 3.11 o superior.
- **Librerías necesarias**:
  - `pandas >= 2.2.3`
  - `matplotlib >= 3.9.0`
  - `faker >= 33.3.1`

## Instalación
### Clonar el repositorio
```bash
# Clonar el repositorio
git clone https://github.com/diamxncl/orbea-monegros/
cd orbea_monegros
```

### Instalar las dependencias
```bash
pip install -r requirements.txt
```

### Instalar el paquete localmente
```bash
pip install .
```

## Uso del proyecto
### Estructura del proyecto
El proyecto está organizado de la siguiente manera:
```
orbea_monegros_project/
│
├── data/                   # Dataset de entrada
├── img/                    # Imágenes generadas (e.g., histograma)
├── orbea_monegros/         # Código fuente del proyecto
│   ├── __init__.py         # Inicialización del paquete
│   ├── data_processing.py  # Funciones para EDA y limpieza de datos
│   ├── anonymization.py    # Anonimización de nombres
│   ├── analysis.py         # Análisis y generación de histogramas
│   ├── clubs.py            # Procesamiento de datos de clubs
│   ├── visualization.py    # Visualización de datos
├── tests/                  # Tests unitarios
│   ├── test_data_processing.py
│   ├── test_anonymization.py
│   ├── test_analysis.py
│   ├── test_clubs.py
│   ├── test_visualization.py
│   ├── test_main.py
├── README.md               # Documentación
├── requirements.txt        # Dependencias del proyecto
├── setup.py                # Configuración del paquete
└── main.py                 # Flujo principal
```

### Ejecución del proyecto
#### Ejecutar el script principal
```bash
python main.py
```
El archivo `main.py` realiza las siguientes operaciones:
1. Importa los datos.
2. Procesa y anonimiza los datos.
3. Agrupa tiempos y genera un histograma.
4. Limpia y agrupa los datos de los clubs ciclistas.
5. Analiza los datos del club UCSC.

#### Ejecutar los tests
```bash
pytest tests/
```
Los tests verifican la funcionalidad de los módulos principales del proyecto.

### Resultados generados
- **`img/histograma.png`**: Histograma con la distribución de ciclistas agrupados por intervalos de tiempo de 20 minutos.

## Funcionalidades principales
### 1. Importación y exploración de datos
- Importar el dataset (`data_processing.importarConjuntoDatos`).
- Mostrar las primeras filas y columnas del conjunto de datos.
- Contar el número total de ciclistas.

### 2. Anonimización y limpieza de datos
- Anonimizar los nombres de los ciclistas utilizando `Faker`.
- Eliminar registros de ciclistas sin tiempo registrado.
- Recuperar información específica de un ciclista por su dorsal.

### 3. Agrupamiento de tiempos
- Agrupar los tiempos en intervalos de 20 minutos (`00`, `20`, `40`).
- Generar un histograma basado en los datos agrupados.

### 4. Procesamiento de datos de clubs
- Normalizar nombres de clubs para evitar duplicados.
- Agrupar ciclistas por club y calcular el número de participantes.

### 5. Análisis del club UCSC
- Identificar los ciclistas del club UCSC.
- Encontrar al ciclista con el mejor tiempo en ese club.
- Determinar la posición y porcentaje del ciclista en la clasificación general.

## Cobertura de tests
Para verificar la cobertura de los tests, puedes ejecutar:
```bash
pytest --cov=orbea_monegros tests/
```

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
