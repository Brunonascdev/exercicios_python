#Exercício 3: Escreva um programa que exiba na tela a tabuada de um número
#que deverá ser informado pelo usuário (deverá ser usada qualquer
#estrutura de repetição).

num = int(input("Insira um número para ver sua tabuda: "))

for i in range(1, 11):
    print("{0} x {1} = {2}".format(num, i, num * i))
    
