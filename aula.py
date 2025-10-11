# Usando range() para gerar números pares de 2 a 20 e imprimindo-os
for num in range(2, 21, 2):
    print(num)

# Criando a lista 'numeros' com inteiros de 1 a 10 e imprimindo-a
numeros = list(range(1, 11))
print(numeros)

# Imprimindo o terceiro elemento da lista 'numeros'
print(numeros[2])

# Adicionando o número 9 à lista 'numeros' e imprimindo a lista atualizada
numeros.append(9)
print(numeros)

# Removendo o número 5 da lista 'numeros' e imprimindo a lista resultante
numeros.remove(5)
print(numeros)

# Criando a lista 'carros' e concatenando-a com a lista 'numeros'
carros = ['Fusca', 'Civic', 'Corolla']
resultado = carros + numeros
print(resultado)
