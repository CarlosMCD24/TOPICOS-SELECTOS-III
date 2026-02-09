# WiDS2025
WiDS Datathon 2025

# Comenzando: Instalación y Autenticación de Kaggle API

Para bajar los datos y no tenerlos en Github, la formá más sencilla es interactuar con la API pública de Kaggle a través de su línea de comandos (CLI) implementada en Python.

## Instalación

Asegúrate de tener Python y el administrador de paquetes `pip` instalados. Luego, ejecuta el siguiente comando para acceder a la API de Kaggle desde la línea de comandos:

```bash
pip install kaggle
```


Para una instalación local en Linux, la ubicación predeterminada es `~/.local/bin`. En Windows, la ubicación predeterminada es `$PYTHON_HOME/Scripts`.

## Autenticación

Para utilizar la API pública de Kaggle, primero debes autenticarte mediante un token de API.

1. Ve a la pestaña "Settings" en tu perfil de usuario de Kaggle.
2. Selecciona "Create New Token".
3. Esto descargará un archivo llamado `kaggle.json`, que contiene tus credenciales de la API.

Si estás usando la herramienta CLI de Kaggle, esta buscará el token en:

* Linux, macOS y otros sistemas basados en UNIX: `~/.kaggle/kaggle.json`
* Windows: `C:\Users\<tu-usuario>\.kaggle\kaggle.json`

Si el token no se encuentra en la ubicación correcta, se generará un error. Por lo tanto, una vez descargado el token, muévelo desde la carpeta de descargas a la ubicación correspondiente. En este caso, para descargar los datos de la competencia, colócate en la carpeta `/data` y escribe el siguiente comando,

```bash
kaggle competitions download -c widsdatathon2025
```

**Nota**: Hay que estar registrado en la competencia.

Si utilizas la API de Kaggle directamente, la ubicación del token no es relevante, siempre que puedas proporcionar tus credenciales en tiempo de ejecución.



## 💻 Tareas para mejorar el Pipeline de Aprendizaje Automático

Cada estudiante debe elegir (o se le asignará) una tarea para contribuir a la mejora del código existente. Por favor, realiza tus cambios en el módulo correspondiente o crea uno nuevo si es necesario. Las contribuciones se realizarán mediante un pull request de Github.


### ✅ Tareas asignadas

1. **Modularizar los Transformadores de Preprocesamiento**  
   Reestructurar el paso de preprocesamiento (por ejemplo, `StandardScaler`, `MinMaxScaler`) del archivo `module_data.py` en una función reutilizable o un pipeline de preprocesamiento.

2. **Agregar Visualización del Análisis de Componentes Principales (PCA)**  
   Después de aplicar PCA, generar gráficos que muestren:
   - Varianza explicada por componente  
   - Varianza explicada acumulada  
   Guardar las figuras en el directorio `plots/`.

3. **Implementar Búsqueda de Hiperparámetros con GridSearch**  
   Agregar funcionalidad en `module_model.py` para realizar ajuste de hiperparámetros con `GridSearchCV` para los modelos existentes (por ejemplo, LogisticRegression, RandomForest).

4. **Reestructurar el Bucle de Comparación de Modelos**  
   En `run_classification.py`, reemplazar la evaluación estática de modelos por un bucle que entrene y evalúe múltiples modelos. Registrar todos los resultados usando MLflow.

5. **Agregar Validación Cruzada con Stratified K-Fold**  
   Extender `ModelEvaluation` para soportar `StratifiedKFold`. Calcular métricas promedio (F1, accuracy, etc.) entre los diferentes folds.

6. **Crear un Módulo `model_metrics.py`**  
   Mover los cálculos de métricas (F1 score, precisión, recall, AUC) a un módulo reutilizable. Este módulo debe ser utilizado tanto por `ModelEvaluation` como por las evaluaciones de `GridSearchCV`.

7. **Implementar Gráficas de Matriz de Confusión**  
   Agregar funcionalidad para generar y guardar gráficas de matriz de confusión para cada modelo evaluado. Guardar los gráficos en el directorio `plots/`.

8. **Crear un Generador de Importancia de Características**  
   Extraer y graficar las importancias de características para modelos tipo árbol (por ejemplo, RandomForest). Guardar las gráficas y archivos CSV ordenados por importancia en `plots/` y `data/`.

9. **Exportar Métricas de Evaluación a CSV**  
   Después de cada evaluación de modelo, exportar las métricas detalladas (F1, accuracy, precisión, recall, AUC) a un archivo CSV para su registro y comparación.

10. **Hacer Configurable la Estrategia de Imputación**  
   Permitir configurar la estrategia de imputación (`mean`, `median`, `mode`) mediante parámetros o archivo de configuración, en lugar de dejarlo codificado como `median`.

11. **Automatizar el Manejo del Directorio de submission**  
   Mejorar el método `ModelSubmission.to_submission()` para que cree archivos o carpetas con fecha y hora, evitando sobrescribir resultados anteriores.

12. **Agregar un Módulo de Selección de Características (`feature_selection.py`)**  
   Implementar métodos de selección automática de variables usando:
   - `SelectKBest` con puntuaciones de chi-cuadrado o ANOVA
   - `Recursive Feature Elimination (RFE)`
   - Importancia de características basada en modelos (por ejemplo, RandomForest)
   Permitir elegir el método y el número de características por parámetro.

13. **Evaluación el Impacto del Preprocesamiento en el Desempeño del Modelo**  
   Comparar distintos pipelines de preprocesamiento (por ejemplo, con o sin escalado, distintas imputaciones o codificaciones) y registrar cómo cambia el desempeño del modelo (F1, accuracy, etc.). Documentar resultados en CSV y MLflow.

