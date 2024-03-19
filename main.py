from fastapi import FastAPI
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()

# http://127.0.0.1:8001 Para trabajar en local

# Endpoint1
# Debe devolver año con mas horas jugadas para dicho género.
# Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}


@app.get("/playtimegenre/{genero}")
def PlayTimeGenre(genero: str):
    try:
        df_e1 = pd.read_csv("df_e1.csv")
        df_e1 = df_e1[df_e1["genres"] == genero]
        output_year = df_e1['year'].iloc[0]
        output_year = int(output_year)

        return {f"Año de lanzamiento con más horas jugadas para {genero}": output_year}
    except Exception as e:
        return {"error": str(e)}

# ======================================================================================================
# #Endpoint2
# Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
# Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}


@app.get("/usergenre/{genero}")
def UserForGenre(genero: str):
    try:
        # df_e2_users = pd.read_csv("df_e2_users.csv")
        # df_e2_playtime = pd.read_csv("df_e2_playtime.csv")

        # df_e2_users = df_e2_users[df_e2_users["genres"] == genero]
        # output_user = df_e2_users['year'].iloc[0]
        # output_playtime = df_e2_playtime[]

        # return {f"Usuario con más horas jugadas para el género {genero}": output_user}

        # Read the user and playtime data from CSV files
        df_e2_users = pd.read_csv("df_e2_users.csv")
        df_e2_playtime = pd.read_csv("df_e2_playtime.csv")

        # Filter users DataFrame to include only users with the specified genre
        users_with_genre = df_e2_users[df_e2_users["genres"] == genero]

        # Calculate total played hours per user
        total_hours_per_user = df_e2_playtime.groupby(
            "user_id")["playtime_forever"].sum()

        # Find the user with the highest total played hours
        user_with_most_hours = total_hours_per_user.idxmax()

        # Get the user's information (assuming "year" column contains the user ID)
        user_info = df_e2_users[df_e2_users["user_id"]
                                == user_with_most_hours].iloc[0]

        # Calculate total played hours per year for the user with the most played hours
        hours_per_year = df_e2_playtime[df_e2_playtime["user_id"] == user_with_most_hours].groupby("year")[
            "playtime_forever"].sum()

        # Format the output as required
        output_hours_per_year = [{"Año": year, "Horas": hours}
                                 for year, hours in hours_per_year.items()]
        output = {
            f"Usuario con más horas jugadas para el género {genero}": user_info["user_id"],
            "Horas jugadas": output_hours_per_year
        }

        return output
    except Exception as e:
        return {"error": str(e)}

# ======================================================================================================
# Endpoint3
# Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]


@app.get("/usersrecommend/{year}")
def UsersRecommend(year: int):
    try:
        df_e3 = pd.read_csv("df_e3.csv")

        df_filtered = df_e3[df_e3['year_review'] == year]
        df_sorted = df_filtered.sort_values(
            by='recommend_count', ascending=False)
        output_top3 = df_sorted.head(3)

        # Formatear la salida como una lista de diccionarios
        output_top3_list = [{"Puesto {}: {}".format(
            i+1, game)} for i, game in enumerate(output_top3['app_name'])]

        return output_top3_list
    except Exception as e:
        return {"error": str(e)}

# ======================================================================================================
# Endpoint4
# Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
# Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]


@app.get("/usersnotrecommend/{year}")
def UsersNotRecommend(year: int):
    try:
        df_e4 = pd.read_csv("df_e3.csv")

        df_filtered = df_e4[df_e4['year_review'] == year]
        df_sorted = df_filtered.sort_values(
            by='recommend_count', ascending=False)
        output_last3 = df_sorted.tail(3)

        # Formatear la salida como una lista de diccionarios
        output_last3_list = [{"Puesto {}: {}".format(
            i+1, game)} for i, game in enumerate(output_last3['app_name'])]

        return output_last3_list
    except Exception as e:
        return {"error": str(e)}

# ======================================================================================================
# Endpoint5
# Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.


@app.get("/sentimentanalysis/{year}")
# Definir la función
def SentimentAnalysis(year: int):
    try:
        df_e5 = pd.read_csv("df_e5.csv")
        df_year = df_e5[df_e5['year'] == year]
        value_negative = df_year['negative'].values[0]
        value_neutral = df_year['neutral'].values[0]
        value_positive = df_year['positive'].values[0]

        # Crear la cadena de salida con los valores obtenidos
        output_sentiment_list = f"Para el año {year} se registran los siguientes valores: negative: {value_negative}, neutral: {value_neutral}, positive: {value_positive}"

        return output_sentiment_list
    except Exception as e:
        return {"error": str(e)}


# ======================================================================================================
# Endpoint MLO

# Entrenar nuestro modelo de machine learning para armar un sistema de recomendación.
# El modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto,
# se recomiendan similares.
# Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar
# el modelo de similitud del coseno.
@app.get("/recomendacionjuego/{item_id}")
def recomendacion_juego(item_id: int):
    try:
        df_mlo = pd.read_csv('df_mlo.csv')

        # Filtrar el DataFrame para obtener solo el juego de interés
        juego = df_mlo[df_mlo['item_id'] == item_id]

        # Seleccionar solo las características numéricas relevantes para el cálculo de similitud
        numeric_features = juego.select_dtypes(
            include=['number']).drop(columns=['item_id'])

        # Calcular la similitud del coseno entre el juego de interés y todos los demás juegos
        cosine_sim = cosine_similarity(numeric_features, df_mlo.select_dtypes(
            include=['number']).drop(columns=['item_id']))

        # Ordenar los resultados de similitud y obtener los índices de los juegos más similares
        similar_indices = cosine_sim.argsort()[0][-6:-1][::-1]

        # Obtener los nombres de los juegos más similares
        juegos_similares = df_mlo.loc[similar_indices, 'app_name']

        # Convertir a conjunto para eliminar duplicados y luego a lista
        # list(set(juegos_similares))
        juegos_similares_unique = juegos_similares

        # Si hay menos de 5 recomendaciones únicas, seleccionar todas
        if len(juegos_similares_unique) < 5:
            return {"recomendaciones": juegos_similares_unique}
        else:
            # Retornar solo los primeros 5 elementos
            return {"recomendaciones": juegos_similares_unique[:5]}
    except Exception as e:
        return {"error": str(e)}
