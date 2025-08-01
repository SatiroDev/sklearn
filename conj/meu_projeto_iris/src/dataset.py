# Importa o dataset Iris diretamente do scikit-learn.
# Esse dataset é comumente usado em exemplos e possui dados sobre flores (comprimento/largura de pétalas e sépalas).
from sklearn.datasets import load_iris

# Importa a função train_test_split, que divide os dados em conjuntos de treino e teste.
from sklearn.model_selection import train_test_split

# Define a função load_data, que carrega e separa os dados.
def load_data():
    # Carrega o dataset Iris em um objeto semelhante a um dicionário.
    iris = load_iris()

    # Separa as features (X) — ou seja, os dados de entrada como comprimento/largura das pétalas e sépalas.
    X = iris.data

    # Separa os rótulos (y) — ou seja, a espécie da flor (0 = setosa, 1 = versicolor, 2 = virginica).
    y = iris.target

    # Divide os dados em conjuntos de treino e teste.
    # 80% dos dados vão para treino, 20% para teste. O random_state garante que a divisão será sempre a mesma.
    return train_test_split(X, y, test_size=0.2, random_state=42)
