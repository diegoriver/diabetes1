import numpy as np
# from tensorflow.keras.models import load_model
import tensorflow as tf


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model_cargado):

    clasification_cargada = model_cargado.predict([x_in])
    n_cargada = clasification_cargada.ravel().tolist()
    i_cargada = n_cargada.index(max(n_cargada))

    if i_cargada == 0:
        resultado_final_cargada = "No diabetico"
    elif i_cargada == 1:
        resultado_final_cargada = "Pre diabetico"
    elif i_cargada == 2:
        resultado_final_cargada = "Diabetico"

    return resultado_final_cargada


def main(datos, model):
    predictS = model_prediction(datos, model)
    print(predictS)
  

if __name__ == '__main__':
    model = ''
    # Se carga el modelo
    if model == '':
        model = tf.keras.models.load_model("models/model_diabetes.h5")


    """TESTEO registro individualCON MODELO CARGADO""" 
    "clasificacion diabetico"
    # datos = [1,1,1,25,1,0,0,1,0,0,0,1,0,2,0,0,0,1,12,5,7]  # no Diabetico 
    # datos = [1,1,1,26,1,1,1,0,0,1,0,1,0,5,30,30,1,0,12,2,1] # diabetico [2]
    datos = [1,0,1,37,0,0,0,1,1,1,0,1,0,2,0,0,0,0,10,6,8] # No Diabetico - ahora Diabetico
    # datos = [1,1,1,27,1,0,0,1,1,1,0,1,0,4,0,0,1,1,9,2,2] # diabetico [51]

    "clasificacion NO diabetico"

    # datos = [1,1,1,27,1,0,0,0,0,0,0,1,1,2,0,0,0,0,10,4,1] #  diabetico
    # datos = [0,0,1,21,0,0,0,1,1,1,0,1,0,2,0,0,0,0,9,6,8] # no diabetico
    # datos = [0,1,1,24,0,0,0,0,1,1,0,1,0,2,0,0,0,1,10,6,8] # no diabetico

    main(datos, model)
