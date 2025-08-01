from src.dataset import load_data
from src.model import train_model
from src.evaluate import evaluate_model
from src.predict import predict

# Carregando dados
X_train, X_test, y_train, y_test = load_data()

# Treinando modelo
model = train_model(X_train, y_train)

# Avaliando
acc = evaluate_model(model, X_test, y_test)
print(f"Acurácia: {acc:.2f}")

# Predição com novo dado
novo_exemplo = [5.1, 3.5, 1.4, 0.2]
pred = predict(model, novo_exemplo)
print(f"Classe prevista: {pred[0]}")