from src import dataset, model, predict, evaluate

# carregar dados
X_train, x_test, y_train, y_test = dataset.load_data()

# treinar modelo
model = model.train_model(X_train, y_train)

# fazer previsões
y_pred = predict.predicter(model, x_test)

# avaliar modelo
acc = evaluate.accuracy_score(y_test, y_pred)

# mostrando o resultado
print(f'Acurária: {acc:.2f}')