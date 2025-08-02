from dataset import load_questions
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# carrega dados (perguntas)
data = load_questions()
vetor = TfidfVectorizer()
# X -> dados de entradas (perguntas)
# y -> é o alvo, representa a classe da flor (0, 1, 2, 3 ou 4) -> 
X, y = vetor.fit_transform(data.perguntas), data.rotulos_target

# criar modelo
model = DecisionTreeClassifier()

# treina modelo
model.fit(X, y)

# pergunta em numero
pergunta_nova = ["Explique como funciona o protocolo TCP/IP e sua importância nas redes de computadores."]
pergunta_nova_vetorizada = vetor.transform(pergunta_nova)

indice = model.predict(pergunta_nova_vetorizada)[0]

print(data.rotulos_target_names[indice])