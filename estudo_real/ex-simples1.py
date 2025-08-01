from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# carrega dados (flores)
data = load_iris()

# X -> dados de entradas (medida das flores)
# y -> é o alvo, representa a classe da flor (0, 1 ou 2)
X, y = data.data, data.target

# cria o modelo (vazio, sem traino inicialmente)
model = DecisionTreeClassifier()

# treina o modelo (vai aprender a relacionar dados de entrada 'X' com as classes 'y')
model.fit(X, y)
tipo = model.predict([[5.1, 3.5, 1.4, 0.2]])
print(data.target_names[tipo])