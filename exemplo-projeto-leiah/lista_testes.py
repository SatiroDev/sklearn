# teste com lista de palavra e seu gabarito

from sklearnProject.dataset import load_avaliacoes_nee
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import ExtraTreeClassifier
from sklearn.naive_bayes import MultinomialNB


from sklearn.ensemble import RandomForestClassifier



data = load_avaliacoes_nee()


vetor = TfidfVectorizer()


X, y = vetor.fit_transform(data.data), data.target

model = MultinomialNB()

model.fit(X, y)


frases = [
    "Quem é o personagem principal da narrativa?",                                 # literal
    "O que o personagem fez logo após encontrar o bilhete?",                       # simples
    "Explique, com suas palavras, o motivo da mudança de atitude do narrador.",    # discursiva
    "Qual a crítica social implícita na relação entre patrão e empregado?",        # crítica
    "Assinale a alternativa que apresenta corretamente o ponto de vista do texto.",# objetiva
    "Interprete a metáfora 'prisão invisível' usada para descrever a rotina.",     # interpretativa
    "Descreva os sentimentos do personagem ao reencontrar a família.",             # discursiva
    "Qual era a profissão do pai do protagonista?",                                # literal
    "Compare o comportamento do protagonista antes e depois do conflito central.", # complexa
    "O que acontece logo após a queda de energia na narrativa?",                   # simples
    "Quais elementos da narrativa revelam uma crítica ao sistema educacional?",    # crítica
    "Qual alternativa expressa melhor o clímax do texto?",                         # objetiva
    "Quem é o personagem que simboliza a esperança no final da história?",         # literal
    "Interprete o significado do espelho na construção da identidade do personagem.", # interpretativa
    "Como o ambiente influencia as decisões do personagem principal?",             # complexa
]

gabarito = [
    [2, 'literal'],
    [0, 'simples'],
    [6, 'discursiva'],
    [4, 'crítica'],
    [5, 'objetiva'],
    [3, 'interpretativa'],
    [6, 'discursiva'],
    [2, 'literal'],
    [1, 'complexa'],
    [0, 'simples'],
    [4, 'crítica'],
    [5, 'objetiva'],
    [2, 'literal'],
    [3, 'interpretativa'],
    [1, 'complexa']
]

for i in range(len(frases)):
    frase = [frases[i]]
    frase_vetorizada = vetor.transform(frase)
    indice = model.predict(frase_vetorizada)[0]
    if indice == gabarito[i][0]:
        continue
    else:
        print('-=-'*25)
        print('Erro')
        print(frase)
        print()
        print('Resposta do modelo: ',data.target_names[indice])
        print()
        print('Resposta correta: ', gabarito[i][1])

    print()
