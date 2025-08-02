

def predict(vetor, model, frase):

    frase_vet = vetor.transform(frase)

    indice = model.predict(frase_vet)[0]

    return indice