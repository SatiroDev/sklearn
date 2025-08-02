from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from dataset import load_questions

data = load_questions()

vetor = TfidfVectorizer()

X, y = vetor.fit_transform(data.data), data.target

model = DecisionTreeClassifier()


# treindando o modelo
model.fit(X, y)
new = ["O DNA é o responsável por armazenar as informações genéticas dos seres vivos."]
new_vet = vetor.transform(new)


indice = model.predict(new_vet)[0]

prevision_name = data.target_names[indice]
print(f'Frase "{new[0]}"')
print(f'Assunto: {prevision_name}')







