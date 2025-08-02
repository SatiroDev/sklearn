from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import ExtraTreeClassifier
from sklearnProject.dataset import load_avaliacoes_nee
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


# carrega os dados
data = load_avaliacoes_nee()

vetor = TfidfVectorizer()

# x -> dados ded entrada y -> é o alvo ('respostas')
X, y = vetor.fit_transform(data.data), data.target
X_treino, X_test, y_treino, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



# modelo
# model = ExtraTreeClassifier()
# model = MultinomialNB(alpha=0.5)
model = LogisticRegression(C=5) # menor = mais simples; maior = mais detalhado



# treina o modelo
model.fit(X_treino, y_treino)

y_pred = model.predict(X_test)

acuracia = accuracy_score(y_test, y_pred)

print(f"Acurácia: {(acuracia*100):.2f}%")