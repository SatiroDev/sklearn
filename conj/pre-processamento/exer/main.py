# Criar uma base de 10 perguntas e aplicar TfidfVectorizer.


# from sklearn.feature_extraction.text import TfidfVectorizer
# import pandas as pd

# perguntas = [
#     "O que é inteligência artificial?",
#     "Qual a diferença entre machine learning e deep learning?",
#     "O que é uma variável em programação?",
#     "Para que serve um banco de dados?",
#     "Qual a função do sistema operacional?",
#     "O que é um algoritmo?",
#     "O que significa a sigla HTML?",
#     "Qual a diferença entre front-end e back-end?",
#     "O que é um loop em programação?",
#     "Qual a função de uma API?"
# ]

# vetor = TfidfVectorizer()

# matriz = vetor.fit_transform(perguntas)

# print(vetor.get_feature_names_out())

# df = pd.DataFrame(matriz.toarray(), columns=vetor.get_feature_names_out())
# print(df)



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
perguntas = [
    "O que é inteligência artificial?",
    "Qual a diferença entre machine learning e deep learning?",
    "O que é uma variável em programação?",
    "Para que serve um banco de dados?",
    "Qual a função do sistema operacional?",
    "O que é um algoritmo?",
    "O que significa a sigla HTML?",
    "Qual a diferença entre front-end e back-end?",
    "O que é um loop em programação?",
    "Qual a função de uma API?"
]

vetor = TfidfVectorizer()

matriz = vetor.fit_transform(perguntas)

similaridades = cosine_similarity(matriz)
print(similaridades)

for i, valor in enumerate(similaridades[0]):
    print(f'Similaridade com a pergunta {i}: {valor:.2f}')