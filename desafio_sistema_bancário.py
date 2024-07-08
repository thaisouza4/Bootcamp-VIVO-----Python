import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

menu = """
            MENU
===========================

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

===========================

"""

saldo = 0.0
limite = 500
extrato_depositos = ["Depósitos: "]
extrato_saques = ["Saques: "]
extrato = [extrato_depositos, extrato_saques]
numero_saques = 0
limite_saques = 3
saque_total_dia = 0

while True:
    opcao = input(menu + "Digite a opção desejada: ")

    if opcao == "1":
        print("Depositar".center(25))
        for i in range(1):
            depositos = float(input("Digite o valor a ser depositado: "))
            saldo += depositos
            valor_formatado1 = locale.currency(depositos, grouping=True)
            extrato_depositos.append(valor_formatado1)
            print("Depósito efetuado com sucesso!")

    elif opcao == "2":
        print("Sacar".center(25))
        for i in range(1):
            saques = float(input("Digite o valor a sacar: "))
            if saques > 0:
                if saques <= saldo:
                    saldo -= saques
                    valor_formatado2 = locale.currency(saques, grouping=True)
                    extrato_saques.append(valor_formatado2)
                    numero_saques +=1
                    saque_total_dia += saques
                    print("Saque realizado com sucesso!")
                    if numero_saques == limite_saques:
                        print("Você só pode realizar 3 saques diários.")
                    elif saques > limite:
                        print("Limite máximo de saque diário é de R$500,00.")
                    elif saque_total_dia > limite:
                        print("Limite máximo de saque diário é de R$500")
                    elif saques > saldo and saques > limite:
                        print("Limite máximo de saque diário é de R$500 e seu saldo é insuficiente!")
                else:
                    print("Saldo insuficiente para saque!")
            else:
                print("O valor do saque deve ser positivo.")

    elif opcao == "3":
        print("Extrato".center(25))
        for transacao in extrato:
            print(transacao, f"Saldo: R${saldo:.2f}")
    
    elif opcao == "0":
        print("Obrigada por usar o Banco Mel".center(25))
        break

    else:
        print("Opção inválida! Por favor, selecione novamente a operação desejada!".center(25))