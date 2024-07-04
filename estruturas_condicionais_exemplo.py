import sys

saldo = 1000

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor para saque: "))
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        print("Saque realizado com sucesso!")

elif opcao == 2:
    print("Exibindo o extrato... ")

else:
    sys.exit("Opção inválida!")