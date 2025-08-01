from sklearn.datasets import load_wine
# carrega o dataset de vinhos

from sklearn.model_selection import train_test_split

def load_data():
    vinhos = load_wine()

    X = vinhos.data

    y = vinhos.target

    return train_test_split(X, y,train_size=0.2, random_state=42)