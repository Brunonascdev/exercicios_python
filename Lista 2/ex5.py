#Exercício 5: Escreva um programa que leia 15 números inteiros e exiba na tela
#ao final, o maior número que foi digitado pelo usuário.

numbers = []

for n in range(1,16):
    numbers.append(int(input("Digite um número: ")))

print("O maior número é: ", max(numbers))
    
