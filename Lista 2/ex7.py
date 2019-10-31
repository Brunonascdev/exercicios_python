#Exercício 7: Escreva um programa que exiba todos os números de 1 a 100 e a
#cada número que for múltiplo de 10, exiba a mensagem “MÚLTIPLO DE 10”.

for i in range(1,101):
    print(i)
    if i % 10 == 0:
        print("^ MÚLTIPLO DE 10")
