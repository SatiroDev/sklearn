# Importa a função accuracy_score do scikit-learn, que calcula a acurácia do modelo.
# A acurácia é a proporção de previsões corretas feitas pelo modelo.
from sklearn.metrics import accuracy_score

# Define uma função evaluate_model que recebe o modelo treinado, os dados de teste e os rótulos reais.
def evaluate_model(model, X_test, y_test):
    # Usa o modelo para fazer previsões com os dados de teste.
    predictions = model.predict(X_test)

    # Compara as previsões com os rótulos reais e calcula a acurácia.
    accuracy = accuracy_score(y_test, predictions)

    # Retorna o valor da acurácia para informar o desempenho do modelo.
    return accuracy
