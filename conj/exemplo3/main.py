from skleranMain import load_data
from src.model import train_model
from src.predict import predict




X, y, target_names, vetor = load_data()

model = train_model(X, y)


frase = ["Ele partiu porque não via mais sentido em ficar. O que motivou realmente essa decisão?"]

indice = predict(vetor, model, frase)

print(target_names[indice])