nome = "Thais"
idade = 26
profissao = "programadora"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Thais", "idade": 26, "profissao": "programadora", "linguagem": "Python"}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.".format(**dados))
print(f"Nome: {nome}. Idade: {idade}")
print(f"Nome: {nome}. Idade: {idade}. Saldo: {saldo:0.2f}")
print(f"Nome: {nome}. Idade: {idade}. Saldo: {saldo:10.2f}")