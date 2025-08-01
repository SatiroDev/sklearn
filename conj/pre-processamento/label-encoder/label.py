from sklearn.preprocessing import LabelEncoder

# rótulos
names = ['peixe', 'gato', 'cachorro', 'gato', 'cachorro', 'tigre']
# objeto do tipo LabelEncoder
le =  LabelEncoder()

# faz duas coisas 
# fit -> aprende quais valores são únicos
# transform -> coverte cada string para um número
numbers = le.fit_transform(names)

print(numbers)

# mostra a ordem  que o LabelEncoder usou para classificar as categorias
print(le.classes_)