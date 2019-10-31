#Exercício 2: Escreva um programa que exiba na tela em ordem decrescente,
#apenas os números ímpares existentes entre dois números
#digitados pelo usuário (inclusive eles).

numUm = int(input("Insira o primeiro número: "))
numDois = int(input("Insira o segundo número: "))

for i in reversed(range(numUm, numDois)):
    if i % 2 != 0:
        print(i)


            
