# Programa: controle_notas.py
# Resumo:
# Este programa recebe várias notas de alunos, valida se as notas estão entre 0 e 10,
# calcula a média das notas, identifica a maior e a menor nota cadastrada,
# informa a quantidade de alunos aprovados (nota maior ou igual a 7)
# e a quantidade de alunos reprovados (nota menor que 7).
#
# Conceitos utilizados:
# - Variáveis e operadores matemáticos
# - Estrutura de repetição while
# - Validação de entrada de dados
# - Estrutura condicional if e else
# - Contadores e acumuladores
# - Cálculo de média
# - Identificação de maior e menor valor

notas = 0
maior = 0
menor = 0
soma = 0
maiores = 0
menores = 0

continuar = "Sim"

while continuar == "Sim":
    nota = float(input("Digite sua nota: "))
    
    while nota > 10 or nota < 0:
        nota = float(input("Nota inválida. Digite novamente: "))
    
    if notas == 0:
        maior = nota
        menor = nota
    
    if nota > maior:
        maior = nota
    
    if nota < menor:
        menor = nota
    
    if nota >= 7:
        maiores = maiores + 1
    else:
        menores = menores + 1

    soma = soma + nota
    notas = notas + 1

    continuar = input("Deseja continuar? (Sim ou não): ")

if notas > 0:
    media = soma / notas
    
    if media >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print("Foram cadastradas", notas, "notas.")
    print("A maior nota:", maior)
    print("A menor nota é:", menor)
    print("A soma das notas:", soma)
    print("A média:", media)
    print("Quant. de notas maiores ou igual a 7:", maiores)
    print("Quant. de notas menores que 7:", menores)

else:
    print("Nenhuma nota cadastrada.")