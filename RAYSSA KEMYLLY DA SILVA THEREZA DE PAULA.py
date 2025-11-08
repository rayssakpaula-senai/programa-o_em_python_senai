try:
    numero = int(input("Insira um número inteiro: "))
    print(f"O número inserido foi: {numero}")
except ValueError:
    print("Erro! Você não inseriu um número inteiro válido.")
    
    
    
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero.")
except ValueError:
    print("Erro! Você deve inserir números válidos.")
    
    
    
    
    
minha_lista = [1, 2, 3, 4, 5]

try:
    indice = int(input("Digite o índice que você deseja acessar: "))
    print(f"O valor no índice {indice} é: {minha_lista[indice]}")
except IndexError:
    print("Erro! O índice fornecido não existe na lista.")
except ValueError:
    print("Erro! Você deve inserir um número válido para o índice.")