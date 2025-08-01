# Importa o RandomForestClassifier do scikit-learn.
# Esse é um modelo de aprendizado supervisionado baseado em várias árvores de decisão (floresta aleatória).
from sklearn.ensemble import RandomForestClassifier

# Define uma função chamada train_model que recebe os dados de treino (X_train e y_train).
def train_model(X_train, y_train):
    # Cria uma instância do modelo Random Forest.
    # O random_state garante que os resultados serão reproduzíveis (mesma aleatoriedade toda vez).
    model = RandomForestClassifier(random_state=42)

    # Treina o modelo com os dados de entrada (X_train) e os rótulos (y_train).
    model.fit(X_train, y_train)

    # Retorna o modelo treinado para uso posterior (como avaliação ou predição).
    return model
