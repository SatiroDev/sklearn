from sklearn.feature_extraction.text import TfidfVectorizer

textos = ['gato gosta de peixe', 'cachorro gosta de osso', 'gato e cachorro']

vetor = TfidfVectorizer()

matriz = vetor.fit_transform(textos)

print(vetor.get_feature_names_out())
print(matriz.toarray())