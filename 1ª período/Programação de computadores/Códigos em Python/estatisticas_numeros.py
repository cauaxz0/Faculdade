
# ==========================================================
#                ESTATÍSTICAS DE NÚMEROS
# ==========================================================

# Descrição:
# Programa que lê números inteiros digitados pelo usuário
# até que seja informado o valor 0 (sentinela).

# Conceitos utilizados:
# - Entrada de dados (input)
# - Laço de repetição (while True)
# - Sentinela (break)
# - Estrutura condicional (if)
# - Contador
# - Acumulador (soma)
# - Cálculo da média
# - Identificação do maior e do menor valor

# Resultados exibidos:
# - Quantidade de números digitados
# - Soma dos números
# - Média dos valores
# - Maior número informado
# - Menor número informado

contador = 0
soma = 0
maior = 0
menor = 0

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    if contador == 0:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    contador = contador + 1
    soma = soma + numero

if contador > 0:
    media = soma / contador

    print("\n\nForam digitados:", contador, "números.")
    print("A soma dos números é:", soma)
    print("A média é:", media)
    print("O maior número é:", maior)
    print("O menor número é:", menor)
else:
    print("Nenhum número foi digitado.")
