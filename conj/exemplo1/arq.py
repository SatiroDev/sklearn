from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
def load_data():
    iris = load_iris()

    X = iris.data

    y = iris.target

    return train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def predict(model, X_test):
    iris = load_iris()
    y_pred = model.predict(X_test)
    for i in y_pred:
        nome_da_flor = iris.target_names[i]
        print(f'Nome da flor prevista: {nome_da_flor}')
    return y_pred

from sklearn.metrics import accuracy_score as sklearn_accuracy
def evalute(y_test, y_pred):
    acc = sklearn_accuracy(y_test, y_pred)
    return acc
    