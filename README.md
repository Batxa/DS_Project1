# DS_Project1

* Escuela: Soy Henry
* Curso: Data Science Part Time, cohorte 7
* Proyecto: Proyecto Individual 1, Machine Learning Operations
* Estudiante: Juan GARATE
* Video explicativo: XXX

* Contenidos & Fases del Proyecto
  * ETL (Extraction, transformation and loading of data)
  * Desarrollo API Application Program Interfase)
  * Deployment
  * EDA (Exploratory Dat Analysis)
  * Modelo de Aprendiaje Automático   


El presente trabajo constituye el primero de los proyectos individuales a presentar como parte de los requisitos para alcanzar la graduación del curso. El objetivo de este proyecto es la creación de un modelo de aprendizaje a partir de un conjunto de datasets.  

# Fases del proyecto:

* ETL (Extraction, transformation and loading of data). 
Los datasets son provistos en formato json comprimido y no vienen limpios, con lo cual se aplica una preparación de los datos. El primer paso es  FEATURE ENGINERERING (INGENIERIA DE CARACTERISTICAS), que consiste en el proceso de seleccionar, transformar y/o crear nuevas características (campos) a partir de los datos brutos. En particular, algunos campos se muestran como listas de diccionarios, por lo cual se deben desanidar pues cada par clave-valor contiene valiosa información para el modelo. 
Luego, se aplica sucesivamente una verificación y tratamiento de tipos de datos, valores duplicados y valores nulos. El ouput de esta fase es un conjunto de datasets limpio y listo para ser consumido por la fase siguiente.
Archivo ETL:

* DESARROLLO API (Application Program Interfase). Se definirá un código en el archivo "main.py" con funciones para comunicar los diferentes componentes del software. Los endpoints que se consumirán en la API son los siguientes:

  1) def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
  Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

  2) def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
  Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012,Horas: 100}, {Año: 2011, Horas: 23}]}
  
  3) def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  
  4) def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  
  5) def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
  Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

* DEPLOYMENT de la API
Se utilizará la herramienta RENDER para comunicar el servidor e intercambiar los datos de la API. La misma consiste en una interfaz gráfica que permite mostrar la interacción entre inputs y outputs, regida por las funciones definidas en el código del archivo "main.py".
  
* EDA (Exploratory data analysis). Esta fase consiste en un análisis de los contenidos de los datos. Se aplican sucesivos métodos para conocer el comportamiento estadístico de las variables principales, aplicables al análisis del mercado, análisis de precios, análisis de preferencias de usuario, y análisis de correlaciones entre variables

Armado de dataframe para correlaciones y modelo de aprendizaje:
![image.png](attachment:image.png)


* MODELO DE APRENDIZAJE AUTOMATICO

El trabajo propone aplicar el formato de SIMILITUD DEL COSENO.

La similitud del coseno no es un modelo de clasificación per se, sino más bien una medida utilizada para calcular la similitud entre dos vectores en un espacio de características. Es comúnmente utilizada en tareas de minería de texto y recuperación de información para determinar la similitud entre documentos, palabras clave, o cualquier otro tipo de datos representados como vectores.

La similitud del coseno calcula el coseno del ángulo entre dos vectores y devuelve un valor entre -1 y 1, donde 1 indica que los vectores son idénticos, 0 indica que son ortogonales (no tienen similitud) y -1 indica que son opuestos.

Aunque no es un modelo de clasificación en sí mismo, la similitud del coseno puede ser utilizada como una medida auxiliar en ciertos procesos de clasificación o agrupamiento, especialmente cuando se trabaja con datos de alta dimensionalidad, como en el procesamiento de texto.

Para este trabajo, he tenido en cuenta que el método de similitud del consumo implica generar tantos campos como registros tenga el dataframe. El dataframe que utilizamos tiene casi 25.000 registros, con lo cual he decidido tomar una muestra aleatoria de 2000 registros.

Luego, en el archivo "main.py" contamos con una función para consultar los outputs del modelo, adoptando un sistema de recomendación tipo item-item. La función tendrá un input que es el item_id de un juego, y devolverá un listado de 5 juegos:

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.