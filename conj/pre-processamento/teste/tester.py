from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

textos = ['gato gosta de peixe', 'cachorro gosta de osso', 'gato e cachorro']

vetor = TfidfVectorizer()

le = LabelEncoder()

matriz = vetor.fit_transform(textos)

numbers = le.fit_transform(vetor.get_feature_names_out())

print(vetor.get_feature_names_out())
print(le.classes_)
for palavra, numero in zip(vetor.get_feature_names_out(), numbers):
    print(f'{palavra}: {numero}')