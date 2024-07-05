nome = "Thais"

mensagem = f'''
    Olá, meu nome é {nome}!
         Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
'''

print(mensagem)

menu = "MENU"

print(f'''{menu.center(40)}
============================================
            
    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

============================================
      Obrigada por usar nosso sistema!
''')