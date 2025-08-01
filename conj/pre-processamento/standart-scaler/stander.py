from sklearn.preprocessing import StandardScaler # iguala os valores, ninguém fica com vantagem
import numpy as np

dados = np.array([[1.0, 2.0], [3.0, 6.0], [5.0, 10.0]])

# objeto scaler
scaler = StandardScaler()

dados_normalizados = scaler.fit_transform(dados)
print(dados)
print(dados_normalizados)