# Cadastro de Alunos
# Programa que cadastra alunos, valida suas notas e calcula a média.
# Também identifica a maior e menor nota e conta aprovados e reprovados.

alunos = 0
soma = 0
maior = 0
menor = 0
aprovados = 0
reprovados = 0
nome_maior = 0
nome_menor = 0

while True:
    nome = input("Digite seu nome (Digite fim para sair): ")

    if nome == "fim":
        break

    idade = int(input("Digite sua idade: "))
    nota = float(input("Digite sua nota: "))

    while nota > 10 or nota < 0:
        nota = float(input("Nota inválida. Digite sua nota: "))

    if alunos == 0:
        maior = nota
        menor = nota
        nome_maior = nome
        nome_menor = nome

    if nota > maior:
        maior = nota
        nome_maior = nome

    if nota < menor:
        menor = nota
        nome_menor = nome

    if nota >= 7:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1

    soma = soma + nota
    alunos = alunos + 1

if alunos > 0:
    media = soma / alunos

    print("Quant. de alunos: ", alunos)
    print("Média das notas:", media)
    print("Aluno que tirou a maior nota e a maior nota: ", nome_maior, maior)
    print("Aluno que tirou a menor nota e a menor nota: ", nome_menor, menor)
    print("Quantos alunos foram aprovados: ", aprovados)
    print("Quantos alunos foram reprovados: ", reprovados)
else:
    print("Nenhum aluno foi cadastrado.")
