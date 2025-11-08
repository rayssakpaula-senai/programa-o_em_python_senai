# ----------------------------------------
# Exercícios com Funções - Menu Interativo
# ----------------------------------------

from datetime import date

# 1 - Função para comparar 2 números (par ou ímpar)
def comparar_paridade(num1, num2):
    if num1 % 2 == 0:
        print(f"O número {num1} é par.")
    else:
        print(f"O número {num1} é ímpar.")

    if num2 % 2 == 0:
        print(f"O número {num2} é par.")
    else:
        print(f"O número {num2} é ímpar.")


# 2 - Função para multiplicar 3 números
def multiplicar_tres(a, b, c):
    resultado = a * b * c
    print(f"O resultado da multiplicação é: {resultado}")


# 3 - Função para elevar um número a uma potência
def elevar_numero(base, expoente):
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é igual a {resultado}")


# 4 - Função para verificar idade (mensagem se for 18 anos)
def verificar_idade(idade):
    if idade == 18:
        print("🎉 Parabéns! Você já é maior de idade!")
    else:
        print(f"Sua idade é {idade}. Ainda não completou 18 anos.")


# 5 - Função para descobrir idade a partir do ano de nascimento
def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(f"Você tem aproximadamente {idade} anos.")


# 6 - Função para verificar se o Brasil ganhou a Copa de 1999
def brasil_ganhou_copa(ano):
    if ano == 1999:
        print("O Brasil NÃO ganhou a Copa do Mundo de 1999.")
    elif ano == 2002:
        print("🏆 O Brasil ganhou a Copa do Mundo de 2002!")
    else:
        print(f"O Brasil não ganhou a Copa de {ano}.")


# 7 - Sistema de restaurante
def cumprimentar_cliente(nome):
    print(f"\nOlá {nome}, seja bem-vindo ao Restaurante Python Saboroso!")

def restaurante():
    menu = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]
    print("\nCardápio:")
    for i, item in enumerate(menu, start=1):
        print(f"{i} - {item}")

    try:
        opcao = int(input("\nEscolha uma opção (1 a 4): "))
        if 1 <= opcao <= 4:
            print(f"Você escolheu: {menu[opcao - 1]}")
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

def sistema_restaurante():
    nome = input("Digite seu nome: ")
    cumprimentar_cliente(nome)
    restaurante()


# -------------------------------
# MENU PRINCIPAL
# -------------------------------
def menu():
    while True:
        print("\n====== MENU DE EXERCÍCIOS ======")
        print("1 - Comparar 2 números (par ou ímpar)")
        print("2 - Multiplicar 3 números")
        print("3 - Elevar um número a uma potência")
        print("4 - Verificar idade (18 anos)")
        print("5 - Calcular idade a partir do ano de nascimento")
        print("6 - Ver se o Brasil ganhou a Copa de 1999")
        print("7 - Sistema de Restaurante")
        print("0 - Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 0:
            print("\n👋 Encerrando o programa... Até logo!")
            break

        elif opcao == 1:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            comparar_paridade(n1, n2)

        elif opcao == 2:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            c = int(input("Digite o terceiro número: "))
            multiplicar_tres(a, b, c)

        elif opcao == 3:
            base = float(input("Digite a base: "))
            exp = int(input("Digite o expoente: "))
            elevar_numero(base, exp)

        elif opcao == 4:
            idade = int(input("Digite sua idade: "))
            verificar_idade(idade)

        elif opcao == 5:
            ano = int(input("Digite o ano do seu nascimento: "))
            calcular_idade(ano)

        elif opcao == 6:
            ano = int(input("Digite o ano da Copa que deseja verificar: "))
            brasil_ganhou_copa(ano)

        elif opcao == 7:
            sistema_restaurante()

        else:
            print("Opção inválida! Tente novamente.")


# Executar o menu
menu()