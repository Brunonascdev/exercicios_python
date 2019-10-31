#Exercício 4: Escreva um programa que exiba na tela a quantidade de
#números ímpares existentes entre dois números que o usuário digitar
#(testar inclusive os números digitados).

numUm = int(input("Insira o primeiro número: "))
numDois = int(input("Insira o segundo número: "))
contador = 0

for i in range(numUm, numDois + 1):
    if i % 2 != 0:
        contador = contador + 1
        print(contador)
        
