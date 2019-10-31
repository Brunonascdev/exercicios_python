#Exercício 9: Escreva um programa que leia vários números inteiros e
#ao final informe quantos números pares, quantos números ímpares,
#quantos números positivos e quantos números negativos foram digitados
#pelo usuário. O programa só deve parar de rodar quando o
#usuário responder "S" na seguinte pergunta, "Deseja encerrar o programa?".

import sys

pares = 0
impares = 0
positivos = 0
negativos = 0

while True:
    for i in range(1, 11):
        numbers = int(input("Digite o {0}º número (Digite '0' para sair): ".format(i)))
        if numbers % 2 == 0:
            pares = pares + 1
        if numbers % 2 != 0:
            impares = impares + 1
        if numbers > 0:
            positivos = positivos + 1
        if numbers < 0:
            negativos = negativos + 1
        if numbers == 0:
            break
    print("\nNúmeros pares: {0}\nNúmeros ímpares: {1}\nNúmeros positivos: {2}\nNúmeros negativos: {3}".format(pares, impares, positivos, negativos))
    sys.exit()
            
