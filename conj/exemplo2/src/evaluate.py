from sklearn.metrics import accuracy_score

def evalute(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    return acc

