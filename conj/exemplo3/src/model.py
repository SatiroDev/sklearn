from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):

    model = LogisticRegression(C=5)

    model.fit(X_train, y_train)

    return model