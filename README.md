# DS_Project1

# DS_PI1_MLOps
* Escuela: Soy Henry
* Curso: Data Science Part Time, cohorte 7
* Proyecto: Proyecto Individual 1
* Estudiante: Juan GARATE
* Video explicativo:
* Archivos para evaluación:
* Contenidos & Fases del Proyecto
  * ETL
  * Desarrollo API
  * Deployment
  * EDA
  * Modelo de Aprendiaje Automático   


El presente trabajo constituye el primero de los proyectos individuales a presentar como parte de los requisitos para alcanzar la graduación del curso. El objetivo de este proyecto es la creación de un modelo de aprendizaje a partir de un conjunto de datasets.  

# Fases del proyecto:

* ETL (Extraction, transformation and loading of data). No se solicita una extracción y transformación de datos desde la web ya que los mismos son provistos, aunque es necesaria una adecuación de los archivos pues vienen en formato json comprimido . Se realiza una preparación de los datos, dentro de lo cual se aplica una FEATURE ENGINERERING (INGENIERIA DE CARACTERISTICAS), la cual consiste en el proceso de seleccionar, transformar o crear nuevas características o campos a partir de los datos brutos con el fin de mejorar el rendimiento de los modelos de aprendizaje automático. Los datasets no vienen limpios, y además contienen campos cuyos valores se muestran como una lista de diccionarios, en donde a cada registro se le asocia varios pares clave-valor. Estos campos contienen valiosa información que es necesario transformar a un formato cuantificable. Asimismo, iremos seleccionando aquellos campos o caraceterísticas del dataset que serán útiles para el modelo de predicción.
  Archivo ETL:

* DESARROLLO API  (Application Program Interfase). Se definirá un código con funciones para comunicar los diferentes componentes del software. Los endpoints que se consumirán en la API son los siguientes:

  1) def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
  2) def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
  3) def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  4) def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  5) def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

* DEPLOYMENT
  
* EDA (Exploratory data analysis)

  * Análisis exploratorio de datos (EDA, Exploratory data analysis). Estructura y distribución de los datos, estadísticas descriptivas (media, mediana, desvío estándar, etc), visualizaciones generales
  * Análisis de correlación. Matriz de correlación, mapa de calor
  * Análisis de datos avanzado. Análisis específicos XXXXX
  * Comunicación de resultados

* MODELO DE APRENDIZAJE AUTOMATICO