from skleranMain import load_questions
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data():
    data = load_questions()

    vetor = TfidfVectorizer()

    X = vetor.fit_transform(data.data)
    y = data.target

    return X, y, data.target_names, vetor