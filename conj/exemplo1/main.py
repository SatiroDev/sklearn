from arq import load_data, train_model, predict, evalute

# 1. Carregar dados
X_train, X_test,  y_train, y_test = load_data()

# 2. Treinar modelo
model = train_model(X_train, y_train)

# 3. Fazer previsões
y_pred = predict(model, X_test)

# 4. Avaliar o modelo
acc = evalute(y_test, y_pred)

# 5. Mostrar resultado
print(f'Acurária: {acc:.2f}')