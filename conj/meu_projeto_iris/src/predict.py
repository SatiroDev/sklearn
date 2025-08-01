# Define a função predict que recebe o modelo treinado e um novo dado para previsão.
def predict(model, new_data):
    # O modelo faz uma predição para o novo dado.
    # O new_data precisa estar dentro de uma lista (ou array 2D) porque o método predict
    # espera uma matriz de amostras (mesmo que seja só 1).
    return model.predict([new_data])
