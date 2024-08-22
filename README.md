<h1 align="center">Proyecto Deserción Escolar 📕</h1>

<h4 align="center">Proyecto realizado por <a href="https://github.com/miguelangsanabria" target="_blank">Miguel Angel Sanabria</a> - Código 2240373 para la asignatura de Desarrollo de Proyectos de Inteligencia Artificial.</h4>

> Aplicación de Machine Learning para la predicción de deserción estudiantil en educación superior utilizando datos demográficos y académicos.
> El modelo predictivo clasifica a los estudiantes en tres categorías diferentes:
> 1. Potenciales Desertores
> 2. Potenciales Inscritos
> 3. Potenciales Graduados
> 
> La aplicación presenta visualizaciones interactivas que permiten analizar la distribución de estudiantes en riesgo de abandono por curso, proporcionando una herramienta valiosa para la toma de decisiones en instituciones educativas.

## 📂 Estructura del Proyecto

```
UAO-neumonia/
│
├── app.py             # Archivo principal para ejecutar la aplicación
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Descripción del proyecto
├── Dockerfile          # Archivo de configuración de la imagen de Docker
├── pytest.ini          # Archivo de configuración para las pruebas
├── utils/              # Módulos de utilidad
│   └── __init__.py
│   └── charts.py
│   └── data_loader.py
│   └── prediction.py
├── data/               # Datasets de ejemplo
│   └── *.csv
├── models/             # Subida de Modelo
│   └── catboost_model.csv
│   └── catboost_model.csv
└── tests/              # Pruebas del proyecto
    └── __init__.py
    └── test_make_donut_chart.py
    └── test_make_stacked_bar.py
```

## 🔧 Requisitos

- Anaconda ([Instrucciones para Windows]( https://docs.anaconda.com/anaconda/install/windows/))
- [Docker](https://docs.docker.com/get-docker/)

## 🚀 Uso

1. Abrir una terminal (preferiblemente `Powershell` en Windows) y ejecutar el comando para crear un entorno virtual:
   
   ```sh
   conda create -n sl streamlit
   ```
   
3. Activa el entorno virtual:
   
   ```sh
   conda activate sl
   ```
   
3. Ve a la carpeta del proyecto
   
   ```sh
   cd UAO-Students
   ```
   
4. Instala las dependencias necesarias
   
   ```sh
   pip install -r requirements.txt
   ```

5. Ejecuta la Aplicación
   
   ```sh
   streamlit run app.py
   ```
   
## 📲 Uso de la Interfaz Gráfica 

- Pulsar en el botón `Browse Files`
- Seleccionar un dataset con la información de los estudiantes (en la carpeta data hay 5 datasets de muestra)
- La Inteligencia Artificial realizará las predicciones con la información subida
- Se pueden observar gráficas, tablas e información de interes para las instituciones educativas.

## ✅ Pruebas

Se realizaron dos pruebas unitarias utilizando `pytest`: 
- **Prueba para la función `make_donut_chart`:** Esta prueba verificará que se cree correctamente un gráfico de tipo donut conteniendo todas las capas correspondientes.
- **Prueba para la función `make_stacked_bar`:** Esta prueba verificará que se cree correctamente un gráfico de barras con sus categorías debidamente asignadas

Se pueden ejecutar las pruebas por medio del comando:
```sh
pytest
```

## 🐳 Instrucciones utilizando Docker

1. El proyecto ya tiene la imagen de Docker configurada en el `Dockerfile` para construirla utiliza el comando dentro de la carpeta del proyecto:

   ```sh
   docker build -t streamlit .
   ```

2. Ejecuta la imagen utilizando:

   ```sh
   docker run -p 8501:8501 streamlit
   ```

3. Ingresar al navegador utilizando el siguiente link http://localhost:8501


## 🤖 Acerca del Modelo

En este proyecto, se ha utilizado un modelo de clasificación CatBoostClassifier. La preparación de los datos incluye una división en conjuntos de entrenamiento y prueba, utilizando un tamaño de prueba del 20% de los datos y una semilla aleatoria de 23 para asegurar la reproducibilidad.

El modelo CatBoostClassifier se ha configurado con una semilla aleatoria de 400 y se ha entrenado durante 500 iteraciones. CatBoost es un algoritmo de boosting basado en árboles de decisión que maneja bien características categóricas y se adapta eficazmente a diversos tipos de datos.

## 📝 Acerca del Dataset

El dataset que se utilizará en este proyecto es “Predict Students’ Dropout and Academic Success” (Valentim Realinho, 2021). El dataset contiene información sobre estudiantes de educación superior como su recorrido académico, datos demográficos, factores socioeconómicos y rendimiento académico. El dataset se obtuvo de varias bases de datos separadas y fue creado con el objetivo de contribuir a la reducción del abandono académico y el fracaso en la educación superior.

El Dataset se encuentra disponible en [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

## 🧑‍💻 Proyecto original realizado por:

Miguel Angel Sanabria - https://github.com/miguelangsanabria 
