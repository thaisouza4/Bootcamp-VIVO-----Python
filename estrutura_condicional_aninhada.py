conta_normal = True
conta_universitaria = False
conta_especial = True
saldo = 2500
cheque_especial = 450

saque = int(input("Digite o valor a sacar: "))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta Especial selecionada!")

else:
    print("O sistema não reconheceu seu tipo de conta, por favor, entre em contato com o seu gerente.")