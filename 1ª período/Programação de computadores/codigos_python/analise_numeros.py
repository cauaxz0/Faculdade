# ==========================================================
#          ANÁLISE DE NÚMEROS (POSITIVOS, NEGATIVOS,
#                 PARES, ÍMPARES E MÉDIA)
# ==========================================================

# Descrição:
# Programa que lê números inteiros digitados pelo usuário
# até que seja informado o valor 0 (sentinela).

# Conceitos utilizados:
# - Entrada de dados (input)
# - Laço de repetição (while True)
# - Sentinela (break)
# - Estrutura condicional (if / else)
# - Contador
# - Acumulador (soma)
# - Operador de resto da divisão (%)
# - Identificação de números positivos e negativos
# - Identificação de números pares e ímpares
# - Cálculo da média

# Resultados exibidos:
# - Quantidade de números digitados
# - Quantidade de números positivos
# - Quantidade de números negativos
# - Quantidade de números pares
# - Quantidade de números ímpares
# - Soma de todos os números
# - Média dos valores

contador = 0
soma = 0
positivo = 0
negativo = 0
par = 0
impar = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break

    if numero > 0:
        positivo = positivo + 1
    else:
        negativo = negativo + 1

    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

    soma = soma + numero
    contador = contador + 1

if contador > 0:
    media = soma / contador

    print("Foram digitados", contador, "números.")
    print("Números positivos:", positivo)
    print("Números negativos:", negativo)
    print("Números pares:", par)
    print("Números ímpares:", impar)
    print("Soma de todos os números:", soma)
    print("A média:", media)
else:
    print("Nenhum número foi digitado.")