# Sistema de Notas com Menu
# Programa que permite cadastrar notas, validar notas entre 0 e 10
# e mostrar a quantidade, média, maior e menor nota cadastrada.

notas = 0
soma = 0
maior = 0
menor = 0

while True:
    print("Menu Principal")
    escolha_opcao = input("Escolha Opção 1: Cadastrar nota. Opção 2: Mostrar estatísticas. Opção 3: Sair: \n")

    if escolha_opcao == "1":
        nota = float(input("Digite sua nota: "))

        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida. Digite sua nota: "))

        if notas == 0:
            maior = nota
            menor = nota

        soma = soma + nota
        notas = notas + 1

        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

    elif escolha_opcao == "2":
        if notas > 0:
            media = soma / notas

            print("Quant.notas cadastradas: ", notas)
            print("Média: ", media)
            print("Maior nota: ", maior)
            print("Menor nota: ", menor)
        else:
            print("Nenhuma nota cadastrada.")

    elif escolha_opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção Inválida.")
