# -----------------------------------------
# SISTEMA DE ANÁLISE — ESCOLA E EMPRESAS
# -----------------------------------------
# Autor: ChatGPT
# Descrição: Calcula média, mediana, moda,
# desvio padrão, menor e maior valor
# para notas de alunos e salários de empresas.
# -----------------------------------------

import statistics

# === FUNÇÕES DE ANÁLISE ===

def media(valores):
    return statistics.mean(valores)

def mediana(valores):
    return statistics.median(valores)

def moda(valores):
    return statistics.mode(valores)

def desvio(valores):
    return statistics.stdev(valores)

def menor_valor(valores):
    return min(valores)

def maior_valor(valores):
    return max(valores)


# === ANÁLISE DE NOTAS (ESCOLA) ===

def analisar_escola():
    print('\n===== ESCOLA FUTURO BRILHANTE =====')

    notas = [9, 8, 7, 10, 5, 6, 8, 9, 7, 10]
    print(f"\nNotas dos alunos: {notas}")

    print('\n📊 Estatísticas das Notas:')
    print(f"Média: {media(notas):.2f}")
    print(f"Mediana: {mediana(notas):.2f}")
    print(f"Moda: {moda(notas)}")
    print(f"Desvio padrão: {desvio(notas):.2f}")
    print(f"Menor nota: {menor_valor(notas)}")
    print(f"Maior nota: {maior_valor(notas)}")

    print('\n🧠 Análise:')
    print("→ A turma apresenta um bom desempenho geral.")
    print("→ Notas entre 7 e 9 predominam, mostrando consistência.")
    print("→ O desvio padrão baixo indica aprendizado equilibrado.")


# === ANÁLISE DE SALÁRIOS (EMPRESAS) ===

def analisar_empresas():
    print('\n===== ANÁLISE DE SALÁRIOS =====')

    empresa1 = [1500, 2500, 3000, 8000, 1200]
    empresa2 = [4000, 4200, 3800, 3500, 3900]
    empresa3 = [1300, 1500, 9500, 3000, 12000]
    empresa4 = [2000, 2500, 2700, 2600, 2650]

    empresas = {
        "Empresa 1": empresa1,
        "Empresa 2": empresa2,
        "Empresa 3": empresa3,
        "Empresa 4": empresa4
    }

    for nome, dados in empresas.items():
        print(f"\n📈 {nome}:")
        print(f"Salários: {dados}")
        print(f"Média: {media(dados):.2f}")
        print(f"Mediana: {mediana(dados):.2f}")
        print(f"Moda: {moda(dados)}")
        print(f"Desvio Padrão: {desvio(dados):.2f}")
        print(f"Menor salário: {menor_valor(dados)}")
        print(f"Maior salário: {maior_valor(dados)}")

    print('\n Conclusão:')
    print("→ A Empresa 2 tem a média salarial mais estável e justa.")
    print("→ A Empresa 3 tem o maior potencial de ganhos, mas alta variação.")
    print("→ A escolha depende do perfil: estabilidade (Empresa 2) ou risco (Empresa 3).")


# === MENU PRINCIPAL ===

def menu():
    while True:
        print("\n===============================")
        print("     SISTEMA DE ANÁLISE")
        print("===============================")
        print("1 - Analisar notas da escola")
        print("2 - Analisar salários de empresas")
        print("3 - Sair")
        print("===============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            analisar_escola()
        elif opcao == "2":
            analisar_empresas()
        elif opcao == "3":
            print("\nEncerrando o sistema... 👋")
            break
        else:
            print("Opção inválida! Tente novamente.")


# === EXECUÇÃO DO PROGRAMA ===

if __name__ == "__main__":
    menu()
