nomes = ['Gabriel', 'Pablo', 'Rafaela', 'Pedro']

# Ordenar pela última letra
nomes.sort(key = lambda palavra: palavra[-1])
print(nomes)

# Ordenar pela primeira letra
nomes2 = ['Gabriel', 'Pablo', 'Wellington', 'Gustavo', 'guilherme']
nomes2.sort(key = lambda palavra: palavra.upper())

print(nomes2)
