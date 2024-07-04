#Exemplo do For com Range:
for numero in range(0, 11):
    print(numero, end=" ")

print() #Adiciona uma quebra de linha

#Exibindo a tabuada do 5:
for numero in range(0, 51, 5):
    print(numero, end=" ")

print() #Adiciona uma quebra de linha

for numero in range(10):
    if numero %2 == 0:
        continue

    print(numero, end=" ")