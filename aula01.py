tentativas = 4
logado = False

while logado == False and tentativas > 0:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cracha = str(input("Possui crachá? (S/N):"))
    monitor = str(input("É monitor? (S/N):"))

    if nome == "Cauã" and idade >= 18 and (cracha == "S" or monitor == "S"):
        print("Acesso liberado.")
        print("Bem-vindo ao laboratório.")
    else:
        print("Acesso negado.")
        tentativas = tentativas - 1
        if tentativas > 0:
            print("Você possui", tentativas, "tentativa(s) restante(s)")

if tentativas > 0:
    print("Acesso bloqueado.")


