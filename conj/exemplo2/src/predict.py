from sklearn.datasets import load_wine
def predicter(model, X_test):
    vinhos = load_wine()
    y_pred = model.predict(X_test)
    for i in y_pred:
        nome_vinho = vinhos.target_names[i]
        print('Nome do vinho: ', nome_vinho)
    print(y_pred)
    return y_pred
