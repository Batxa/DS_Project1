from fastapi import FastAPI 
import pandas as pd
from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#http://127.0.0.1:8001

#Endpoint1
#Debe devolver año con mas horas jugadas para dicho género.
#Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013} 
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
    
#======================================================================================================
# #Endpoint2
#Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
#Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
@app.get("/usergenre/{genero}")
def UserForGenre(genero: str):
    try:
        df_e2_users = pd.read_csv("df_e2_users.csv")
        df_e2_playtime = pd.read_csv("df_e2_playtime.csv")

        df_e2_users = df_e2_users[df_e2_users["genres"] == input_genre]
        output_user = df_e2_users['year'].iloc[0]
        #output_playtime = df_e2_playtime[]
        
        return {f"Usuario con más horas jugadas para el género {input_genre}": output_user}
    except Exception as e:
        return {"error": str(e)}
   
#======================================================================================================
#Endpoint3
#Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
#Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
@app.get("/usersrecommend/{año}")
def UsersRecommend(año: int):
    try:
        df_e3 = pd.read_csv("df_e3.csv")
        año = int(año)
        df_e3 = df_e3[df_e3['year'] == año]
        output_top3 = df_e3[df_e3['year_review'] == año].head(3)
        output_top3 = int(output_top3)
        #output_top3_list = [{"Puesto {}: {}".format(i+1, game)} for i, game in enumerate(output_top3['app_name'])]
        
        # Filtrar por el año dado y comentarios positivos/neutrales y recomendaciones verdaderas
        #filtered_df = df_e3[(df_e3['year_review'] == año) & (df_e3['sentiment'].isin(['positive', 'neutral'])) & (df_e3['recommend'] == True)]
        # Ordenar por la cantidad de recomendaciones en orden descendente y seleccionar los 3 mejores juegos
        #top3_games = filtered_df.sort_values(by='recommend', ascending=False).head(3)['app_name'].tolist()
        
        # Formatear la salida como una lista de diccionarios
        output_top3_list = [{"Puesto {}: {}".format(i+1, game)} for i, game in enumerate(output_top3)]
        
        # Formatear la salida como una lista de diccionarios utilizando zip
        #output_top3_list = [{"Puesto {}: {}".format(i+1, game)} for i, game in zip(range(3), output_top3)]
        #output_top3_list = [{"Puesto {}: {}".format(i+1, game)} for i, game in zip(range(3), output_top3['app_name'])]
        


        return output_top3_list
    except Exception as e:
        return {"error": str(e)}

#======================================================================================================
#Endpoint4    
#Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
#Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
@app.get("/usersnotrecommend/{año}")
def UsersNotRecommend(año: int):
    try:
        df_e4 = pd.read_csv("df_e4.csv")
        output_last3 = df_e4[df_e4['year_review'] == año].tail(3)
        output_last3_list = [{"Puesto {}: {}".format(i+1, game)} for i, game in enumerate(output_last3['app_name'])]
        return output_last3_list
    except Exception as e:
        return {"error": str(e)}

#======================================================================================================
#Endpoint5
#Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

@app.get("/sentimentanalysis/{año}")
# Definir la función
def SentimentAnalysis(año: int):
    try:
        df_e5 = pd.read_csv("df_e5.csv")

        value_negative = df_e5['negative'].values[0]
        value_neutral = df_e5['neutral'].values[0]
        value_positive = df_e5['positive'].values[0]

        output_sentiment_list = f"Para el año {año} se registran los siguientes valores: negative: {value_negative}, neutral: {value_neutral}, neutral: {value_positive}"       
        return output_sentiment_list
    except Exception as e:
        return {"error": str(e)}